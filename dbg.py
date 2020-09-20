from lib.prpg_main import main
from lib.screen_layout import Dim
from lib.startup import create_root

root = create_root(Dim(40, 120))
main(root, root.curses)
