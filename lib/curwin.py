# Simple window and layout support over the curses library making it easy to
# layout resizing windows in terminal output.

import os
from lib.printd import printd
from dataclasses import dataclass

# Size and location of a Comp(ononent) in it's parent window.
@dataclass
class Pos:
    y: int = 0
    x: int = 0

    def __repr__(self):
        return '{},{}'.format(self.y, self.x)

    def yx(self, orient):
        if orient == Orient.HORIZONTAL: return self.x
        if orient == Orient.VERTICAL: return self.y
        raise ValueError("unknown orientation: " + orient)

    def invert(self):
        return Pos(self.x, self.y)

# Width and Height of a Comp(onent).
@dataclass
class Dim:
    h: int = 0
    w: int = 0

    def __repr__(self):
        return '{},{}'.format(self.h, self.w)

    def invert(self):
        return Dim(self.w, self.h)

    def hw(self, orient):
        if orient == Orient.HORIZONTAL: return self.w
        if orient == Orient.VERTICAL: return self.h
        raise ValueError("unknown orientation: " + orient)

    # calculate dimensions of a component from constraints, position and parent dimensions
    def child_dim(self, con, pos):
        printd('Dim.child_dim(self[{}],con[{}],pos[{}])'.format(self, con, pos))
        pdim = self
        if con.hmax == 0 or con.hmin > pdim.h - pos.y:
            reth = pdim.h - pos.x
        else:
            reth = min(con.hmax, pdim.h - pos.y)

        if con.wmax == 0 or con.wmin > pdim.w - pos.x:
            retw = pdim.w - pos.x
        else:
            retw = min(con.wmax, pdim.w - pos.x)

        ret = Dim(reth, retw)
        printd('...Dim.child_dim() return', ret)
        return ret


# Constraint application strategy - dictates how constraints are merged
class ConApply:
    STACK = 'stack',       # add the applied constraint, as with width constraints added horizontally across
    CONTAIN = 'contain',   # create the most constraining result of the two, as with a parent and it's content constraints
    ADJACENT = 'adjacent', # use the greatest of lower bound and upper bound, as with height constraints of adjacent components

class Orient:
    VERTICAL = 'vertical',
    HORIZONTAL = 'horizontal'

    @staticmethod
    def invert(orient):
        if orient == Orient.HORIZONTAL: return Orient.VERTICAL
        if orient == Orient.VERTICAL: return Orient.HORIZONTAL
        raise ValueError("unknown orientation: " + orient)

# Constraint defines Comp(onent) min and max width and height. It us used for calculating
# Comp(ononet) Dim(ensions) in flow layouts
#
# zero indicates no constraint (min or max)
@dataclass
class Con:
    hmin: int = 0
    wmin: int = 0
    hmax: int = 0
    wmax: int = 0

    def __post_init__(self):
        if self.hmax and self.hmax < self.hmin:
            self.hmax = self.hmin
        if self.wmax and self.wmax < self.wmin:
            self.wmax = self.wmin

    def __repr__(self):
        return '{},{},{},{}'.format(self.hmin, self.wmin, self.hmax, self.wmax)

    def hwmin(self, orient):
        if orient == Orient.HORIZONTAL: return self.wmin
        if orient == Orient.VERTICAL: return self.hmin
        raise ValueError("unknown orientation: " + orient)

    def hwmax(self, orient):
        if orient == Orient.HORIZONTAL: return self.wmax
        if orient == Orient.VERTICAL: return self.hmax
        raise ValueError("unknown orientation: " + orient)

    def invert(self):
        return Con(self.wmin, self.hmin, self.wmax, self.hmax)

    def dup(self):
        return Con(self.hmin, self.wmin, self.hmax, self.wmax)

    # add the given constraints resulting in most constrained value: greatest minimum and least maximum
    def apply(self, con, h_apply, w_apply):
        if h_apply == ConApply.CONTAIN:
            self.hmin = max(self.hmin, con.hmin)
            self.hmax = max(self.hmax, con.hmax) if self.hmax==0 or con.hmax==0 else min(self.hmax, con.hmax)
        elif h_apply == ConApply.ADJACENT:
            self.hmin = max(self.hmin, con.hmin)
            self.hmax = 0 if self.hmax == 0 or con.hmax == 0 else max(self.hmax, con.hmax)
        elif h_apply == ConApply.STACK:
            self.hmin += con.hmin
            self.hmax = 0 if self.hmax == 0 or con.hmax == 0 else self.hmax + con.hmax
        else:
            raise RuntimeError(str(h_apply) + ' not handled')

        if w_apply == ConApply.CONTAIN:
            self.wmin = max(self.wmin, con.wmin)
            self.wmax = max(self.wmax, con.wmax) if self.wmax==0 or con.wmax==0 else min(self.wmax, con.wmax)
        elif w_apply == ConApply.ADJACENT:
            self.wmin = max(self.wmin, con.wmin)
            self.wmax = 0 if self.wmax == 0 or con.wmax == 0 else max(self.wmax, con.wmax)
        elif w_apply == ConApply.STACK:
            self.wmin += con.wmin
            self.wmax = 0 if self.wmax == 0 or con.wmax == 0 else self.wmax + con.wmax
        else:
            raise RuntimeError(str(w_apply) + ' not handled')

# Base component class.
#
# Comp instances resolve, in order:
#   con(straints) of children and then themselves (bottom-up)
#   dim(ensions) of themselves and sometimes their children (panel layout) (top-down)
#   paint for themselves, then their children (top-down)
#
class Comp:
    def __init__(self, parent, pos, con):
        self.parent = parent
        self._pos = pos     # upper-left location, fixed or managed by parent prior to calling paint()
        self._con = con     # constraints used to calculate _dim
        self._dim = None    # width and height, managed by parent prior to calling paint(), or sized to parent
        self.children = []  # child Comp(onents) painted after parent

    def __repr__(self, **kwargs):
        chlen = ',#' + str(len(self.children)) if self.children else ''

        return '{}[P[{}],D[{}],C[{}]{}]'.format(type(self).__name__, self._pos, self._dim, self._con, chlen)

    # Panels manage their children pos(ition) as well as their own
    def pos(self):
        if not self._pos:
            self._pos = self._calc_pos()
        return self._pos

    # Panels manage their children dim(ension) as well as their own
    def dim(self):
        printd('Comp.dim({})'.format(self))
        if not self._dim:
            self._dim = self._calc_dim()
        return self._dim

    def con(self):
        if not self._con:
            self._con = self._calc_con()
        return self._con

    def root(self):
        ret = self
        while ret.parent:
            ret = ret.parent
        return ret

    # return first parent that is a Win instance, or None, if this component has no parent window
    def parent_win(self):
        ret = self.parent
        while ret and not isinstance(ret, Win):
            ret = ret.parent
        return ret

    # re-paint from root. later, this may be optimized to refresh just the component painted
    def paint(self):
        self.root()._paint()

    ###########################
    # virtual methods
    ###########################
    # managed by parent container or defaults to 0,0 (none)
    def _calc_con(self):
        return Con()

    # managed by parent container or defaults to 0,0
    def _calc_pos(self):
        return Pos()

    def _paint(self):
        printd('Comp._paint({})'.format(self))
        for c in self.children:
            c._paint()

    # by default, derive dim from parent size, constraints and position.
    #
    #      | <-   parent.w   -> |
    #                           |
    #      | <-   dim.w  ->  |  |
    #      +-----------------+--+ ---    ---
    #      |                 |  |  ^      ^
    #      |     +-----------+  |  |      |
    #      |     |           |  |
    #      |     |           |  | dim.h  parent.h
    #      |     | component |  |
    #      |     |           |  |  |      |
    #      |     |           |  |  v      |
    #      | - - +-----------+  | ----    |
    #      |                    |         |
    #      |                    |         v
    #      +--------------------+        --- 
    def _calc_dim(self):
        printd('Comp._calc_dim({})'.format(self))
        pdim = self.parent.dim()
        if self._dim:
            # dim was parent-generated
            return self._dim

        return pdim.child_dim(self.con(), self.pos())

    # components that manage layout of children will implement this method to know when recalculation is needed
    def _child_added(self, comp):
        pass

class Win(Comp):
    # if not passed in, scr is created later when dimensions are known.
    def __init__(self, parent, pos, con, scr=None):
        super().__init__(parent, pos, con)
        self._scr = scr

    def __repr__(self):
        scr = 'scr' if self._scr else 'x'
        return 'Win[{}]->{}'.format(scr, super().__repr__())

    def addwin(self, con=None, pos=None):
        ret = Win(self, pos, con)
        self.children.append(ret)
        return ret

    def addrow(self, con=None, pos=None):
        ret = Panel(self, pos, con, Orient.HORIZONTAL)
        self.children.append(ret)
        return ret

    def addcol(self, con=None, pos=None):
        ret = Panel(self, pos, con, Orient.VERTICAL)
        self.children.append(ret)
        return ret

    def _paint(self):
        printd('Win._paint({})'.format(self))
        if not self._scr:
            dim = self.dim()
            printd('...Win._paint() no scr', dim)
            pos = self.pos()
            self._scr = self.parent_win()._scr.derwin(dim.h, dim.w, pos.y, pos.x)
            self._scr.border()

        for c in self.children:
            c._paint()

# A row adds constraints horizontally and merges vertical constraints, for example:
#
#   w hen: sum(wmin) > parent.w, dimensions should contract to panel.w
#
#       ->      wmin         <-
#      +------+------+----+----+
#      |      |      |         |
#      +------+------+----|----+
#      |                  |
#      +------------------+
#
#    vertical constraints are max(hmin) and min(hmax), handling zero as a non-constraint
#
#    when: sum(wmin) < parent.w, dimensions should expand to min(wmax, panel.w)
#
#       <- wmin ->     | <- wmax, when less than panel.w, is the constraint.
#      +--+--+----+----+--+
#      |  |  |    |    |  |
#      +--+--+----+    |  |
#      |               |  |
#      +------------------+
#
# A column works the same way but add constraints vertically instead of horizontally.
#

class Panel(Comp):
    def __init__(self, parent, pos, con, orient):
        super().__init__(parent, pos, None) # con is always calculated from children
        self.orient = orient
        self._panel_con = con if con else Con()   # self.con() will derive from self._panel_con and children

    def __repr__(self):
        orient = 'VER' if self.orient == Orient.VERTICAL else 'HOR'
        return 'Panel[{},pcon[{}]->{}'.format(orient, self._panel_con, super().__repr__())

    def _calc_dim(self):
        printd('Panel._calc_dim({})'.format(self))
        dim = super()._calc_dim()
        if not self.children:
            return dim

        ccon = self.con()
        orient = self.orient

        space = dim.hw(orient) - ccon.hwmin(orient)           # extra space (negative means overage to shrink)
        pos = self.pos()
        yxoffset = pos.yx(orient)
        children = self.children
        nchildren = len(children)
        for ci in range(nchildren):
            child = children[ci]
            ccon = child.con()
            csize = ccon.hwmin(orient)
            c_hwmax = ccon.hwmax(orient)
            adj = int(space/(nchildren-ci))     # adj is positive to expand, negative to shrink
            if csize + adj < 0:
                adj = csize
                csize = 0
            elif c_hwmax and csize + adj > c_hwmax:
                adj = c_hwmax - csize
                csize = c_hwmax
            else:
                csize += adj

            space -= adj

            orient2 = Orient.invert(orient)
            cmax2 = ccon.hwmax(orient2)
            csize2 = dim.hw(orient2)
            if cmax2 and cmax2 < csize2:
                csize2 = cmax2

            if orient == Orient.HORIZONTAL:
                child._pos = Pos(pos.y, yxoffset)
                child._dim = Dim(csize2, csize)
            elif orient == Orient.VERTICAL:
                child._pos = Pos(yxoffset, pos.x)
                child._dim = Dim(csize, csize2)
            else:
                raise ValueError("unknown orientation: " + orient)

            printd('...Panel._calc_dim() child[{}]: pos[{}], dim[{}]'.format(ci, child._pos, child._dim))

            yxoffset += csize

        return dim

    def addwin(self, con=None):
        ret = Win(self, None, con)
        self.children.append(ret)
        self._con = None
        self._dim = None
        return ret

    def addrow(self, con=None):
        ret = Panel(self, None, con, Orient.HORIZONTAL)
        self.children.append(ret)
        self._con = None
        self._dim = None
        return ret

    def addcol(self, con=None):
        ret = Panel(self, None, con, Orient.VERTICAL)
        self.children.append(ret)
        self._con = None
        self._dim = None
        return ret

    # derive constraints from children and self._panel_con
    def _calc_con(self):
        if self.orient == Orient.VERTICAL:
            h_apply = ConApply.STACK
            w_apply = ConApply.ADJACENT
        elif self.orient == Orient.HORIZONTAL:
            h_apply = ConApply.ADJACENT
            w_apply = ConApply.STACK
        else:
            raise ValueError("unknown orientation: " + self.orient)

        if len(self.children):
            ret = self.children[0].con().dup()
            for c in self.children[1:]:
                ret.apply(c.con(), h_apply, w_apply)
        else:
            ret = Con()

        ret.apply(self._panel_con, ConApply.CONTAIN, ConApply.CONTAIN)
        return ret

class RootWin(Win):

    def __init__(self, scr):
        super().__init__(None, None, None, scr)

    def __repr__(self):
        return 'Root->{}'.format(super().__repr__())

    # @override the default which uses parent.dim()
    #
    # Note that we can test with RootWin instance by setting _dim directly to control the results of this method, which
    # will prevent calls to os.get_terminal_size()
    def _calc_dim(self):
        w, h = os.get_terminal_size()
        return Dim(h, w)

def rootwin(scr):
    return RootWin(scr)
