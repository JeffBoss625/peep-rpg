# Simple window and layout support over the curses library making it easy to
# layout resizing windows in terminal output.

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
        if orient == Orient.HORI: return self.x
        if orient == Orient.VERT: return self.y
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
        if orient == Orient.HORI: return self.w
        if orient == Orient.VERT: return self.h
        raise ValueError("unknown orientation: " + orient)

    # calculate dimensions of a component from constraints, position and parent dimensions
    def child_dim(self, con, pos):
        # printd('Dim.child_dim(self[{}],con[{}],pos[{}])'.format(self, con, pos))
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
        # printd('...Dim.child_dim() return', ret)
        return ret


# Constraint application strategy - dictates how constraints are merged
class ConApply:
    STACK = 'stack',       # add the applied constraint, as with width constraints added horizontally across
    CONTAIN = 'contain',   # create the most constraining result of the two, as with a parent and it's content constraints
    ADJACENT = 'adjacent', # use the greatest of lower bound and upper bound, as with height constraints of adjacent components

class Orient:
    VERT = 'VERT'
    HORI = 'HORI'

    @staticmethod
    def invert(orient):
        if orient == Orient.HORI: return Orient.VERT
        if orient == Orient.VERT: return Orient.HORI
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

    def min(self, orient):
        if orient == Orient.HORI: return self.wmin
        if orient == Orient.VERT: return self.hmin
        raise ValueError("unknown orientation: " + orient)

    def max(self, orient):
        if orient == Orient.HORI: return self.wmax
        if orient == Orient.VERT: return self.hmax
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


class Out:
    def printd(self, *args):
        printd(*args)


DEFAULT_OUT = Out()

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
        self.pos = pos        # position within parent (panels will update this in do_layout)
        self.con = con        # constraints used to calculate dim
        self.dim = None       # calculated in do_layout()
        self.children = []

    # Called from root down
    def clear_layout(self):
        raise NotImplementedError()

    def calc_constraints(self):
        raise NotImplementedError()

    def apply_ddf(self, fn, v=None):
        for c in self.children:
            v = c.apply_ddf(fn, v)
        return fn(self, v)

    def iterate_win(self, fn, v=None, xoff=0, yoff=0, d=0):
        if isinstance(self, Win):
            v = fn(self, v, xoff, yoff, d)
            d += 1

        xoff += self.pos.x
        yoff += self.pos.y
        for c in self.children:
            v = c.iterate_win(fn, v, xoff, yoff, d)

        return v

    # This is called from root down after clear_layout(). Panel instances override this to layout children
    # and update their own dimension and constraints
    def do_layout(self):
        # calculate missing constraints (bottom-up)
        def calc_con(comp, v):
            # printd('calc_con({})'.format(comp))
            if not comp.con:
                comp.calc_constraints()

        self.apply_ddf(calc_con)

        self.calc_child_dim()

    def calc_child_dim(self):
        raise NotImplementedError()

@dataclass
class Config:
    border: int = 1

# a component with fixed position children (relative to parent).
# Windows also have an id counter and an assignable name.
#
# __class__ attributes:
#    win_by_name    all windows by name
#    win_count      total number of windows created (including those deleted)
#
class Win(Comp):
    # if not passed in, scr is created later when dimensions are known.
    def __init__(self, parent, name, pos, con):
        super().__init__(parent, pos, con)
        self.name = name
        self.conf = Config()
        wp = parent
        while wp and not isinstance(wp, Win):
            wp = wp.parent
        self.winparent = wp
        self.data = None        # externally managed data (e.g. corresponding curses window)

        # class level info
        clz = self.__class__
        if not hasattr(clz, 'win_count'):
            clz.win_count = 0
            clz.win_by_name = {}

        clz.win_count += 1

        self.id = clz.win_count
        if not self.name:
            self.name = 'window_{}'.format(self.id)

        clz.win_by_name[self.name] = self

    def __repr__(self):
        return '"{}":[P[{}],D[{}],C[{}]]'.format(self.name, self.pos, self.dim, self.con)

    def window(self, name, pos, con):
        if not pos:
            pos = Pos(0,0)
        ret = Win(self, name, pos, con)
        self.children.append(ret)
        return ret

    def panel(self, orient, pos, con):
        if not pos:
            pos = Pos(0,0)
        ret = Panel(self, orient, pos, con)
        self.children.append(ret)
        return ret

    # Derive children dim from parent size, and child constraints and position.
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
    def calc_child_dim(self):
        for c in self.children:
            c.dim = self.dim.child_dim(c.con, c.pos)
            c.calc_child_dim()

    def clear_layout(self):
        if self.parent:         # root dim is static, child dim is calculated from constraints
            self.dim = None

        for c in self.children:
            c.clear_layout()

# A row adds constraints horizontally and merges vertical constraints, for example:
#
#   when: sum(wmin) > parent.w, dimensions should contract to panel.w
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
    def __init__(self, parent, orient, pos, panel_con):
        super().__init__(parent, pos, None) # con is calculated from children do_layout()

        if not panel_con:
            panel_con = Con()

        self.orient = orient
        self.panel_con = panel_con  # further constratins applied to aggregate of child constraints

    def __repr__(self):
        return 'Panel[{}->{}'.format(self.orient, super().__repr__())

    # panels derive their constraints from children and self.panel_con and set child positions
    def clear_layout(self):
        self.dim = None
        self.con = None
        for c in self.children:
            c.pos = None
            c.clear_layout()

    # First calculate constraints based on child constraints (set from bottom-up) and panel_con.
    # Then calculate dimensions based on parent.dim and constraints
    def calc_constraints(self):
        if self.orient == Orient.VERT:
            h_apply = ConApply.STACK
            w_apply = ConApply.ADJACENT
        else:
            h_apply = ConApply.ADJACENT
            w_apply = ConApply.STACK

        self.con = self._calc_constraints(h_apply, w_apply)     # calculate AND SET child constraints (bottom up)

    # calculate constraints from bottom-up for all constraints that are not set
    def _calc_constraints(self, h_apply, w_apply):
        if not self.children:
            return self.panel_con

        # for c in self.children:
        #     if not c.con:
        #         c.con = c._calc_constraints(h_apply, w_apply)   # all components must have con or _calc_constraints()

        ret = self.children[0].con.dup()
        for c in self.children[1:]:
            ret.apply(c.con, h_apply, w_apply)

        ret.apply(self.panel_con, ConApply.CONTAIN, ConApply.CONTAIN)
        return ret

    def window(self, name, con):
        ret = Win(self, name, None, con)
        self.children.append(ret)
        self.con = None
        self.dim = None
        return ret

    def panel(self, orient, con):
        ret = Panel(self, orient, None, con)
        self.children.append(ret)
        self.con = None
        self.dim = None
        return ret

    def calc_child_dim(self):
        flow_layout_place_children(self.orient, self.pos, self.dim, self.con, self.children)
        for c in self.children:
            c.calc_child_dim()

def min0(a, b):
    if a == 0: return b
    elif b == 0: return a
    else: return min(a, b)

def max0(a,b):
    if a == 0: return b
    elif b == 0: return a
    else: return max(a, b)

def sum_max0(a):
    ret = 0
    for v in a:
        if v == 0:
            return 0
        ret += v
    return ret

def flow_layout_place_children(orient, pos, dim, con, children):
    printd('flow_layout_place_children({},pos[{}],dim[{}],con[{}])'.format(orient, pos, dim, con))
    required = sum(c.con.min(orient) for c in children)             # minimum space required
    max_avail = sum_max0(c.con.max(orient) for c in children)       # max space needed
    max_avail = min0(max_avail, con.max(orient))                    # ...bound by panel
    max_avail = min0(max_avail, dim.hw(orient))                     # ...bound by dim
    space = max_avail - required
    pos_offset = 0
    nchildren = len(children)
    for ci in range(nchildren):
        child = children[ci]
        printd('...flow_layout child[{}]: ({})'.format(ci, child))
        ccon = child.con
        c_size = ccon.min(orient)
        c_max = min0(ccon.max(orient), max_avail)
        adj = int(space / (nchildren - ci))  # adj is positive to expand, negative to shrink
        if c_size + adj < 0:
            adj = c_size
            c_size = 0
        elif 0 < c_max < c_size + adj:
            adj = c_max - c_size
            c_size = c_max
        else:
            c_size += adj

        space -= adj

        orient2 = Orient.invert(orient)
        c_size2 = min0(ccon.max(orient2), dim.hw(orient2))

        if orient == Orient.HORI:
            child.pos = Pos(0,pos_offset)
            child.dim = Dim(c_size2, c_size)
        elif orient == Orient.VERT:
            child.pos = Pos(pos_offset,0)
            child.dim = Dim(c_size, c_size2)
        else:
            raise ValueError("unknown orientation: " + orient)

        printd('..->flow_layout child[{}]: ({})'.format(ci, child))

        pos_offset += c_size


def rootwin(dim):
    ret = Win(None, 'root', Pos(0,0), Con(dim.h, dim.w, dim.h, dim.w))
    ret.dim = dim
    ret.conf.border = 0
    return ret
