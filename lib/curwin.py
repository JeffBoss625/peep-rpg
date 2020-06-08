# Simple window and layout support over the curses library making it easy to
# layout resizing windows in terminal output.

import os
from dataclasses import dataclass
from functools import reduce

# Size and location of a Comp(ononent) in it's parent window.
@dataclass
class Pos:
    y: int = 0
    x: int = 0

    def invert(self):
        return Pos(self.x, self.y)

# Width and Height of a Comp(onent).
@dataclass
class Dim:
    h: int = 0
    w: int = 0

    def invert(self):
        return Dim(self.w, self.h)

    # calculate dimensions of a component from constraints, position and parent dimensions
    def child_dim(self, con, pos):
        pdim = self
        if con.hmax == 0 or con.hmin > pdim.h - pos.y:
            reth = pdim.h - pos.x
        else:
            reth = min(con.hmax, pdim.h - pos.y)

        if con.wmax == 0 or con.wmin > pdim.w - pos.x:
            retw = pdim.w - pos.x
        else:
            retw = min(con.wmax, pdim.w - pos.x)

        return Dim(reth, retw)


# Constraint application strategy - dictates how constraints are merged
class ConApply:
    STACK = 'stack',       # add the applied constraint, as with width constraints added horizontally across
    CONTAIN = 'contain',   # create the most constraining result of the two, as with a parent and it's content constraints
    ADJACENT = 'adjacent', # use the greatest of lower bound and upper bound, as with height constraints of adjacent components

class Orient:
    VERTICAL = 'vertical',
    HORIZONTAL = 'horizontal'

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

    # Panels manage their children pos(ition) as well as their own
    def pos(self):
        if not self._pos:
            self._pos = self._calc_pos()
        return self._pos

    # Panels manage their children dim(ension) as well as their own
    def dim(self):
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
        ret = self
        while ret.parent is not None and not isinstance(ret.parent, Win):
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

    # by default, derive dim from parent size, constraints and position.
    #
    #      | <-   parent.w  --> |
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
        return self.parent.dim().child_dim(self.con(), self.pos())

    # components that manage layout of children will implement this method to know when recalculation is needed
    def _child_added(self, comp):
        pass

    def _paint(self):
        pass


class Win(Comp):
    # if not passed in, scr is created later when dimensions are known.
    def __init__(self, parent, pos, con, scr=None):
        super().__init__(parent, pos, con)
        self._scr = scr

    def addwin(self, pos=None, con=None):
        ret = Win(self, pos, con)
        self.children.append(ret)
        return ret

    def addrow(self, pos=None, con=None):
        ret = Panel(self, pos, con, Orient.HORIZONTAL)
        self.children.append(ret)
        return ret

    def addcol(self, pos=None, con=None):
        ret = Panel(self, pos, con, Orient.VERTICAL)
        self.children.append(ret)
        return ret

    def _paint(self):
        if not self._scr:
            h, w = self.dim()
            y, x = self.pos()
            win = self.parent_win().scr.derwin(h, w, y, x)
            win.border()
            self._scr = win
        return self._scr


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

    def _calc_dim(self):
        ret = super()._calc_dim()

        return ret

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
        else:
            h_apply = ConApply.ADJACENT
            w_apply = ConApply.STACK

        if not len(self.children):
            return self._panel_con

        ret = self.children[0].con().dup()
        for c in self.children[1:]:
            ret.apply(c.con(), h_apply, w_apply)

        ret.apply(self._panel_con, ConApply.CONTAIN, ConApply.CONTAIN)
        return ret

    # noinspection PyProtectedMember
    def _paint(self):
        for c in self.children:
            c._paint()

class RootWin(Win):
    def __init__(self, scr):
        super().__init__(None, None, None, scr)

    # @override the default which uses parent.dim()
    #
    # Note that we can test with RootWin instance by setting _dim directly to control the results of this method, which
    # will prevent calls to os.get_terminal_size()
    def _calc_dim(self):
        w, h = os.get_terminal_size()
        return Dim(h, w)

def rootwin(scr):
    return RootWin(scr)
