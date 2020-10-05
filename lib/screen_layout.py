# Simple window and layout support over the curses library making it easy to
# layout resizing windows in terminal output.
import os
from dataclasses import dataclass, field


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

    def dup(self):
        return Dim(self.h, self.w)


# Constraint application strategy - dictates how constraints are merged
class ConApply:
    STACK = 'stack',  # add the applied constraint, as with width constraints added horizontally across
    CONTAIN = 'contain',  # create the most constraining result of the two, as with a parent and it's content constraints
    ADJACENT = 'adjacent',  # use the greatest of lower bound and upper bound, as with height constraints of adjacent components


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

    # adjust this constraint by the given rule along the specified orientation, bounding it by lo and hi bounds
    def constrain(self, rule, orient, vmin, vmax):
        if orient == Orient.VERT:
            pmin = 'hmin'
            pmax = 'hmax'
        else:
            pmin = 'wmin'
            pmax = 'wmax'

        slfmin = getattr(self, pmin)
        slfmax = getattr(self, pmax)
        if rule == ConApply.CONTAIN:
            setattr(self, pmin, max(slfmin, vmin))  # constrain to least minimum
            setattr(self, pmax, max(slfmax, vmax) if slfmax == 0 or vmax == 0 else min(slfmax, vmax)) # constrain to smallest
        elif rule == ConApply.ADJACENT:
            setattr(self, pmin, max(slfmin, vmin))
            setattr(self, pmax, 0 if slfmax == 0 or vmax == 0 else max(slfmax, vmax))  # expand to greatest max
        elif rule == ConApply.STACK:
            setattr(self, pmin, slfmin + vmin)
            setattr(self, pmax, 0 if slfmax == 0 or vmax == 0 else slfmax + vmax)      # no max if any is 0
        else:
            raise RuntimeError(f'rule {rule} not handled')


# Base component class.
#
# Comp instances resolve, in order:
#   con(straints) of children and then themselves (bottom-up)
#   dim(ensions) of themselves and sometimes their children (panel layout) (top-down)
#   paint for themselves, then their children (top-down)
#
class Layout:
    def __init__(self, parent, name, pos, con, **params):
        self.parent = parent
        self.name = name
        self.pos = pos  # position within parent. children of panels have this managed by parent.do_layout()
        self.con = con  # constraints used to calculate dim
        self.params = params if params else {}
        self.dim = params.get('dim', None)  # managed by parent panel and constrained by parent dim - see do_layout()

        # border and margins are used in both layouts and in window delegates
        self.border = params.get('border', 1)
        self.x_margin = params.get('x_margin', self.border)
        self.y_margin = params.get('y_margin', self.border)

        self.children = []
        self._logger = params.get('logger', None)

        # store consolidated window information in the root object
        root = self.root()
        root.info.comp_count += 1
        self.id = root.info.comp_count
        if not self.name:
            self.name = f'comp{self.id}'
        if hasattr(root.info.comp_by_name, self.name):
            raise ValueError(f'multiple components with the same name: "{self.name}"')

        root.info.comp_by_name[self.name] = self

    # Called from root down
    def clear_layout(self):
        raise NotImplementedError()

    def calc_constraints(self):
        raise NotImplementedError()

    def root(self):
        p = self
        while p.parent:
            p = p.parent
        return p

    def logger(self):
        if not self._logger:
            self._logger = self.root()._logger
        return self._logger

    def log(self, s):
        self.logger().log(s)

    def apply_ddf(self, fn, v=None):
        for c in self.children:
            v = c.apply_ddf(fn, v)
        return fn(self, v)

    def iterate_win(self, fn, v=None, d=0):
        if isinstance(self, WinLayout):
            v = fn(self, v, d)
            d += 1

        for c in self.children:
            v = c.iterate_win(fn, v, d)

        return v

    def calc_child_dim(self):
        raise NotImplementedError()

@dataclass
class RootInfo:
    comp_count: int = 0
    comp_by_name: dict = field(default_factory=dict)


class Window:
    def update_layout(self, pos, dim):
        raise NotImplementedError()

# a component with fixed position children (relative to parent).
# Windows also have an id counter and an assignable name.
class WinLayout(Layout):
    # if not passed in, scr is created later when dimensions are known.
    def __init__(self, parent, name, pos, con, **params):
        if con is None:
            con = Con()
        super().__init__(parent, name, pos, con, **params)
        self.window = None              # externally-managed window (e.g. curses window)
        self._is_resizing = False       # track concurrent resizing callbacks to prevent redundant window resizing
        self._last_layout_update = (self.pos, self.dim)   # track last published pos/dim for this layout

        # store parent window
        wp = parent
        while wp and not isinstance(wp, WinLayout):
            wp = wp.parent
        self.winparent = wp


    def __repr__(self):
        return '"{}":[P[{}],D[{}],C[{}]]'.format(self.name, self.pos, self.dim, self.con)

    def window(self, name, pos, con, **kwds):
        if not pos:
            pos = Pos(0, 0)
        ret = WinLayout(self, name, pos, con, **kwds)
        self.children.append(ret)
        return ret

    def panel(self, name, orient, pos, con):
        if not pos:
            pos = Pos(0, 0)
        ret = FlowLayout(self, name, orient, pos, con)
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
        self.dim = None
        for c in self.children:
            c.clear_layout()

    # This is called from root down after clear_layout(). Panel instances override this to layout children
    # and update their own dimension and constraints
    def do_layout(self):
        # self.log(f'do_layout({self.name}, {self.dim})')
        self.clear_layout()

        # calculate missing constraints (bottom-up)
        def calc_con(comp, _v):
            if not comp.con:
                comp.calc_constraints()

        self.apply_ddf(calc_con)

        self.calc_child_dim()

        for c in self.children:
            c.iterate_win(update_win_layout)

    def calc_constraints(self):
        raise NotImplementedError("constraints for non-panels should be set explicitly")

# initialize window delegates of children of position or dimension changes
def update_win_layout(layout, _v, _d):
    posdim = (layout.pos, layout.dim)
    if posdim == layout._last_layout_update:
        return  # no change

    pwin = layout.winparent.window if layout.winparent else None
    layout._last_layout_update = posdim
    layout.window.layout_change(pwin, layout.pos, layout.dim)

class RootLayout(WinLayout):
    def __init__(self, dim, **params):
        self.info = RootInfo()          # info needs to be in place for super() init to register name
        super().__init__(None, 'main', Pos(0,0), Con(dim.h,dim.w,dim.h,dim.w), **params)

        self.dim = dim
        self._is_resizing = False       # track concurrent resizing callbacks to prevent redundant window resizing

    def clear_layout(self):
        # root dim does not get cleared
        for c in self.children:
            c.clear_layout()

    def calc_constraints(self):
        raise NotImplementedError("window constraints should be set explicitly")

    # Handle a series of resizing calls (rubber-banding like calls as the user drags the terminal window boundary),
    def handle_resizing(self):
        if self._is_resizing:
            return False

        self._is_resizing = True
        term_size = os.get_terminal_size()
        # self.log(f'handle_resizing({os.get_terminal_size()})')
        if term_size != (self.dim.w, self.dim.h):
            w, h = term_size
            self.dim = Dim(h, w)
            self.con = Con(h, w, h, w)
            self.window.handle_resizing(h, w)
            self.do_layout()

        self._is_resizing = False
        return True

# A FlowLayout positions child components adjacent to each other horizontally (Orient.HORI) or
# vertically (Orient.VERT). In the stacked direction, child components are assigned wmin size plus
# an even distribution among growable children of any extra space available.
#
# children dimensions expand to min(wmax, panel.w)
#
# e.g. for a horizontal panel when sum(wmin) < parent.w:
#                                parent wmax
#       children:   wmin  wmax     |
#                    |    |        |
#      +---+----+----+----+--------+
#      | A | B  | C  |             |
#      +---|    |----+             |  <- C child hmax
#      |   +----+                  |  <- A and B child hmax
#      +---------------------------+
#
# ... children grow to their collective max size
#
#                                parent wmax
#       children:   wmin  wmax     |
#                    |    |        |
#      +----+-----+-------+--------+
#      | A  |  B  |   C   |        |
#      |    |     +-------+        |  <- C child hmax
#      +----+-----+                |  <- A and B child hmax
#      +---------------------------+
#
#   when: sum(wmin) < parent.w and sum(wmax) >= parent.w (in this case, C has no max, for example):
#
#                                parent wmax
#       children:   wmin  wmax     |
#                    |    |        |
#      +----+-----+----------------+
#      | A  |  B  |      C         |
#      |    |     +----------------|  <- C child hmax
#      +----+-----+                |  <- A and B child hmax
#      +---------------------------+
#
#   when: sum(wmin) > parent.w, dimensions of the children are shrunk to panel.w starting with the RIGHT-most or
#   BOTTOM-most component. That is, the minimum sizes of first-added components are kept and all of the adjustment is
#   made on the last component. The reasoning for this is that going below min size is avoided as long as possible
#   for prioritized (left or top) components.
#
class FlowLayout(Layout):
    def __init__(self, parent, name, orient, pos, panel_con):
        super().__init__(parent, name, pos, None)  # con is calculated from children do_layout()

        if not panel_con:
            panel_con = Con()

        self.orient = orient
        self.panel_con = panel_con  # further constratins applied to aggregate of child constraints

    def __repr__(self):
        return 'Panel "{}":{}:[P[{}],D[{}],C[{}]]'.format(self.name, self.orient, self.pos, self.dim, self.con)

    # panels derive their constraints from children and self.panel_con and set child positions
    def clear_layout(self):
        self.dim = None
        self.con = None
        for c in self.children:
            c.pos = None        # manage child positions
            c.clear_layout()

    # First calculate constraints based on child constraints (set from bottom-up) and panel_con.
    # Then calculate dimensions based on parent.dim and constraints
    def calc_constraints(self):
        # self.log('calc_constraints({})'.format(self))
        if self.orient == Orient.VERT:
            vert_rule = ConApply.STACK
            hori_rule = ConApply.ADJACENT
        else:
            vert_rule = ConApply.ADJACENT
            hori_rule = ConApply.STACK

        self.con = self._calc_constraints(vert_rule, hori_rule)  # calculate AND SET child constraints (bottom up)
        # self.log('...calc_constraints({})'.format(self))

    # calculate constraints from bottom-up for all constraints that are not set
    def _calc_constraints(self, vert_rule, hori_rule):
        if not self.children:
            return self.panel_con

        # for c in self.children:
        #     if not c.con:
        #         c.con = c._calc_constraints(h_apply, w_apply)   # all components must have con or _calc_constraints()

        ret = self.children[0].con.dup()
        for c in self.children[1:]:
            ret.constrain(vert_rule, Orient.VERT, c.con.hmin, c.con.hmax)
            ret.constrain(hori_rule, Orient.HORI, c.con.wmin, c.con.wmax)

        ret.constrain(ConApply.CONTAIN, Orient.VERT, self.panel_con.hmin, self.panel_con.hmax)
        ret.constrain(ConApply.CONTAIN, Orient.HORI, self.panel_con.wmin, self.panel_con.wmax)
        return ret

    def window(self, name, con, **kwds):
        ret = WinLayout(self, name, None, con, **kwds)
        self.children.append(ret)
        self.con = None
        self.dim = None
        return ret

    def panel(self, name, orient, con):
        ret = FlowLayout(self, name, orient, None, con)
        self.children.append(ret)
        self.con = None
        self.dim = None
        return ret

    def calc_child_dim(self):
        orient = self.orient
        con = self.con
        dim = self.dim
        children = self.children

        avail_space = min0(con.max(orient), dim.hw(orient))
        ccon_mins = list(c.con.min(orient) for c in children)
        ccon_maxs = list(c.con.max(orient) for c in children)

        c_sizes = flow_calc_sizes(avail_space, ccon_mins, ccon_maxs)

        fixed_avail_space = dim.hw(Orient.invert(orient))

        offset_flow = self.pos.yx(orient)
        offset_fixed = self.pos.yx(Orient.invert(orient))

        for i, c in enumerate(children):
            c_size = c_sizes[i]
            c_size_fixed = min0(c.con.max(Orient.invert(orient)), fixed_avail_space)
            if orient == Orient.HORI:
                c.pos = Pos(offset_fixed, offset_flow)
                c.dim = Dim(c_size_fixed, c_size)
            elif orient == Orient.VERT:
                c.pos = Pos(offset_flow, offset_fixed)
                c.dim = Dim(c_size, c_size_fixed)
            else:
                raise ValueError("unknown orientation: " + orient)

            offset_flow += c_size

        for c in self.children:
            c.calc_child_dim()


def min0(*a):
    ret = a[0]
    for v in a:
        if ret == 0:
            ret = v
        elif v != 0 and v < ret:
            ret = v
    return ret


def sum_max0(a):
    ret = 0
    for v in a:
        if v == 0:
            return 0
        ret += v
    return ret


# place min-sized childrent and truncate the last child and children to fit
def flow_calc_size_trunc(avail, ccon_mins):
    ret = []
    for ccon_min in ccon_mins:
        c_size = ccon_min

        if avail > 0:
            if avail >= c_size:
                avail -= c_size
            else:
                c_size = avail
                avail = 0
        else:
            c_size = 0

        ret.append(c_size)

    return ret


# expand children from min size to evenly distribute extra allowed space to children
def flow_calc_size_fill(required, avail, ccon_mins, ccon_maxs):
    ret = []
    extra = avail - required  # extra space to distribute among children
    num_children = len(ccon_mins)
    for ci, c_min in enumerate(ccon_mins):
        c_max = min0(ccon_maxs[ci], c_min + extra)
        adj = int(extra / (num_children - ci))
        if 0 < c_max < c_min + adj:
            # more adjustment than can be taken - only consume the needed adjustment
            adj = c_max - c_min

        extra -= adj
        ret.append(c_min + adj)

    return ret


# calculate dimension size in a flow layout (e.g. left-to-right or top-to-bottom) for
# a given list of min and max constraints in an available amount of space.
# Return the list of sizes, one per constraint pair
def flow_calc_sizes(avail, mins, maxs):
    required_space = sum(mins)  # min space required
    avail_space = min0(sum_max0(maxs), avail)  # ...bound by panel and dim

    if avail_space < required_space:
        c_sizes = flow_calc_size_trunc(avail_space, mins)
    else:
        c_sizes = flow_calc_size_fill(required_space, avail_space, mins, maxs)

    return c_sizes
