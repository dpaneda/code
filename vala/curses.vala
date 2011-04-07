using GLib;
using Curses;

namespace Test {
        class HelloWorld {
                public static int main(string[] args) {
                        initscr();
                        start_color();

                        init_pair((short)1, Color.GREEN, Color.RED);

                        var win = new Window(LINES - 8, COLS - 8, 4, 4);
                        win.bkgdset(COLOR_PAIR(1) | Attribute.BOLD);
                        win.addstr("Hello world!");
                        win.clrtobot();
                        win.getch();

                        endwin();

                        return 0;
                }
        }
}

// Local Variables:
// compile-command: "valac --pkg curses ex-curses.vala -X -lncurses"
// End:
