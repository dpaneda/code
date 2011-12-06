-- Standard awesome library
require("awful")
require("awful.autofocus")
require("awful.rules")
-- Theme handling library
require("beautiful")
-- Notification library
require("naughty")
require("vicious")

function run_once(prg,arg_string,pname,screen)
    if not prg then
        do return nil end
    end

    if not pname then
       pname = prg
    end

    if not arg_string then 
        awful.util.spawn_with_shell("pgrep -f -u $USER -x '" .. pname .. "' || (" .. prg .. ")",screen)
    else
        awful.util.spawn_with_shell("pgrep -f -u $USER -x '" .. pname .. "' || (" .. prg .. " " .. arg_string .. ")",screen)
    end
end

local exec   = awful.util.spawn
local sexec  = awful.util.spawn_with_shell
local scount = screen.count()

-- {{{ Variable definitions
-- Themes define colours, icons, and wallpapers
config = awful.util.getdir("config")
beautiful.init(config .. "/themes/dust/theme.lua")

-- {{{ Memory usage
memicon = widget({ type = "imagebox" })
memicon.image = image(beautiful.widget_mem)
-- Initialize widget
membar = awful.widget.progressbar()
-- Pogressbar properties
membar:set_width(10)
membar:set_height(12)
membar:set_vertical(true)
membar:set_background_color(beautiful.fg_off_widget)
membar:set_border_color(beautiful.border_widget)
membar:set_color(beautiful.fg_widget)
membar:set_gradient_colors({ beautiful.fg_widget,
   beautiful.fg_center_widget, beautiful.fg_end_widget
})
-- }}}

---- {{{ Volume level

function volume_up()
    awful.util.spawn("amixer -q set Master 10%+")
    vicious.force({volbar, volstate})
end

function volume_down()
    awful.util.spawn("amixer -q set Master 10%-")
    vicious.force({volbar, volstate})
end

function volume_mute()
    awful.util.spawn("amixer -q set Master toggle")
    vicious.force({volbar, volstate})
end

--volicon = widget({ type = "imagebox" })
--volicon.image = image(beautiful.widget_vol)
---- Initialize widgets
volbar   = awful.widget.progressbar()
volstate = widget({ type = "textbox" })
volstate.width = 10
-- Progressbar properties
volbar:set_width(30)
volbar:set_height(12)
volbar:set_vertical(false)
volbar:set_background_color(beautiful.fg_off_widget)
volbar:set_border_color(beautiful.border_widget)
volbar:set_color(beautiful.fg_widget)
volbar:set_gradient_colors({ beautiful.fg_widget,
   beautiful.fg_center_widget, beautiful.fg_end_widget
}) -- Enable caching
-- Register buttons
volbar.widget:buttons(awful.util.table.join(
   awful.button({ }, 1, function () exec("alsamixer") end),
   awful.button({ }, 2, volume_mute),
   awful.button({ }, 4, volume_up),
   awful.button({ }, 5, volume_down)
)) -- Register assigned buttons
volstate:buttons(volbar.widget:buttons())

-- }}}

-- This is used later as the default terminal and editor to run.
terminal = "urxvtcd"
editor = os.getenv("EDITOR") or "vim"
editor_cmd = terminal .. " -e " .. editor
browser = "chromium"
explorer = terminal .. " -e ranger"

-- Default modkey.
-- Usually, Mod4 is the key with a logo between Control and Alt.
-- If you do not like this or do not have such a key,
-- I suggest you to remap Mod4 to another key using xmodmap or other tools.
-- However, you can use another modifier like Mod1, but it may interact with others.
modkey = "Mod4"

-- Table of layouts to cover with awful.layout.inc, order matters.
layouts =
{
    awful.layout.suit.floating,
    awful.layout.suit.tile,
    awful.layout.suit.tile.bottom,
    awful.layout.suit.magnifier
}
-- }}}

-- {{{ Tags
-- Define a tag table which hold all screen tags.
tags = {}
for s = 1, screen.count() do
    -- Each screen has its own tag table.
    tags[s] = awful.tag({"A","W","E","S","O","M","E"}, s, layouts[2])
end
-- }}}

-- {{{ Menu
-- Create a laucher widget and a main menu
myawesomemenu = {
   { "manual", terminal .. " -e man awesome" },
   { "edit config", editor_cmd .. " " .. awful.util.getdir("config") .. "/rc.lua" },
   { "restart", awesome.restart },
   { "quit", awesome.quit }
}

mymainmenu = awful.menu({ items = { { "awesome", myawesomemenu, beautiful.awesome_icon },
                                    { "open terminal", terminal }
                                  }
                        })

mylauncher = awful.widget.launcher({ image = image(beautiful.awesome_icon),
                                     menu = mymainmenu })
-- }}}

--  Wibox
--Initialize widget
volbar2 = awful.widget.progressbar()
--Progressbar settings
  volbar2:set_width(8)
  volbar2:set_height(18)
  volbar2:set_vertical(true)
  volbar2:set_ticks(true)
  volbar2:set_ticks_gap(1)
  volbar2:set_ticks_size(2)
  volbar2:set_background_color("#000000")
  volbar2:set_border_color("#000000")
  volbar2:set_color("#D9D9D9")
  volbar2:set_gradient_colors({ "#D9D9D9", "#D9D9D9", "#D9D9D9" })

-- {{{ CPU usage and temperature
-- Initialize widgets
cpugraph = awful.widget.graph()
-- Graph properties
--cpugraph.bg_align = "left"
cpugraph.width = 35
cpugraph.height = 25
cpugraph:set_background_color("#333333")
cpugraph:set_gradient_angle(0)
cpugraph:set_gradient_colors({ "#FF5656", "#88A175", "#AECF96" })

--Create a cpuwidget
cpuwidget = widget({ type = "textbox" })
cpuwidget.width = 45
cpuwidget.align = "right"
cpuwidget.bg_image = image(config .. "/icons/dust/cpu.png")
cpuwidget.bg_align = "left"
cpuwidget.bg_resize = true

-- Wifiwidget -- Shows connected wlan and signal quality
wifiwidget = widget({ type = "textbox" })
wifiwidget.align = "right"
wifiwidget.bg_image = image(config .. "/icons/wifi.png")
wifiwidget.bg_align = "left"
wifiwidget.bg_resize = true

--Seperator
spacer = widget({ type = "textbox" })
spacer.text = " "
spicon = widget({ type = "textbox" })
spicon.text = "<span color='#EEEE66'> | </span>"

-- Create a netwidget (usage)
dnicon = widget({ type = "imagebox" })
upicon = widget({ type = "imagebox" })
dnicon.image = image(config .. "/icons/dust/down.png")
upicon.image = image(config .. "/icons/dust/up.png")
-- Initialize widget
netwidget = widget({ type = "textbox" })

-- Create a battery widget
baticon = widget({ type = "imagebox" })
baticon.image = image(config .. "/icons/dust/bat.png")
--Initialize widget
batwidget = widget({ type = "textbox" })

-- Create a textclock widget
mytextclock = awful.widget.textclock()

--Register widgets
vicious.register(cpugraph,   vicious.widgets.cpu, "$1")
vicious.register(cpuwidget,  vicious.widgets.cpu, "$1 %", 2)
vicious.register(volbar2,    vicious.widgets.volume, "$1", 2, "Master")
vicious.register(wifiwidget, vicious.widgets.wifi, "    ${ssid}  ${link}/70", 5, "wlan0")
vicious.register(netwidget,  vicious.widgets.net, "${wlan0 down_kb} / ${wlan0 up_kb}", 1)
vicious.register(batwidget,  vicious.widgets.bat, "$1$2", 32, "BAT1")
vicious.register(membar,     vicious.widgets.mem, "$1", 13)
vicious.register(volbar,     vicious.widgets.volume, "$1", 2, "Master")
vicious.register(volstate,   vicious.widgets.volume, "$2", 2, "Master")

-- Create a systray
mysystray = widget({ type = "systray" })

-- Create a wibox for each screen and add it
mywibox = {}
promptbox = {}
layoutbox = {}
taglist = {}
taglist.buttons = awful.util.table.join(
                    awful.button({ }, 1, awful.tag.viewonly),
                    awful.button({ modkey }, 1, awful.client.movetotag),
                    awful.button({ }, 3, awful.tag.viewtoggle),
                    awful.button({ modkey }, 3, awful.client.toggletag),
                    awful.button({ }, 4, awful.tag.viewnext),
                    awful.button({ }, 5, awful.tag.viewprev)
                    )
mytasklist = {}
mytasklist.buttons = awful.util.table.join(
                     awful.button({ }, 1, function (c)
                                              if not c:isvisible() then
                                                  awful.tag.viewonly(c:tags()[1])
                                              end
                                              client.focus = c
                                              c:raise()
                                          end),
                     awful.button({ }, 3, function ()
                                              if instance then
                                                  instance:hide()
                                                  instance = nil
                                              else
                                                  instance = awful.menu.clients({ width=250 })
                                              end
                                          end),
                     awful.button({ }, 4, function ()
                                              awful.client.focus.byidx(1)
                                              if client.focus then client.focus:raise() end
                                          end),
                     awful.button({ }, 5, function ()
                                              awful.client.focus.byidx(-1)
                                              if client.focus then client.focus:raise() end
                                          end))

for s = 1, screen.count() do
    -- Create a promptbox for each screen
    promptbox[s] = awful.widget.prompt({ layout = awful.widget.layout.horizontal.leftright })
    -- Create an imagebox widget which will contains an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    layoutbox[s] = awful.widget.layoutbox(s)
    layoutbox[s]:buttons(awful.util.table.join(
                           awful.button({ }, 1, function () awful.layout.inc(layouts, 1) end),
                           awful.button({ }, 3, function () awful.layout.inc(layouts, -1) end),
                           awful.button({ }, 4, function () awful.layout.inc(layouts, 1) end),
                           awful.button({ }, 5, function () awful.layout.inc(layouts, -1) end)))
    -- Create a taglist widget
    taglist[s] = awful.widget.taglist(s, awful.widget.taglist.label.all, taglist.buttons)

    -- Create a tasklist widget
    mytasklist[s] = awful.widget.tasklist(function(c)
                                              return awful.widget.tasklist.label.currenttags(c, s)
                                          end, mytasklist.buttons)
    -- Create the wibox
    wibox[s] = awful.wibox({ position = "top", screen = s, border_width = 0, border_color = "#FFFFFF" })
   -- Add widgets to the wibox - order matters
    wibox[s].widgets = {
        {
            taglist[s], spacer, layoutbox[s], spacer, 
            promptbox[s],
            layout = awful.widget.layout.horizontal.leftright
        },
        s == 1 and mysystray or nil, mytextclock,
        spicon, 
        cpugraph.widget, spacer, cpuwidget,
        --spicon,
        --volbar.widget,
        spicon,
        upicon, netwidget, dnicon, 
        spicon, 
        wifiwidget, 
        spicon, 
        batwidget, baticon,
        mytasklist[s],
        layout = awful.widget.layout.horizontal.rightleft
    }
end

-- {{{ Mouse bindings
root.buttons(awful.util.table.join(
    awful.button({ }, 3, function () mymainmenu:toggle() end),
    awful.button({ }, 4, awful.tag.viewnext),
    awful.button({ }, 5, awful.tag.viewprev)
))
-- }}}

-- {{{ Key bindings
globalkeys = awful.util.table.join(
    awful.key({ modkey,           }, "Left",   awful.tag.viewprev       ),
    awful.key({ modkey,           }, "Right",  awful.tag.viewnext       ),
    awful.key({ modkey,           }, "Escape", awful.tag.history.restore),

    awful.key({ modkey,           }, "j",
        function ()
            awful.client.focus.byidx( 1)
            if client.focus then client.focus:raise() end
        end),
    awful.key({ modkey,           }, "k",
        function ()
            awful.client.focus.byidx(-1)
            if client.focus then client.focus:raise() end
        end),

    -- Layout manipulation
    awful.key({ modkey, "Shift"   }, "j", function () awful.client.swap.byidx(  1)    end),
    awful.key({ modkey, "Shift"   }, "k", function () awful.client.swap.byidx( -1)    end),
    awful.key({ modkey, "Control" }, "j", function () awful.screen.focus_relative( 1) end),
    awful.key({ modkey, "Control" }, "k", function () awful.screen.focus_relative(-1) end),
    awful.key({ modkey,           }, "u", awful.client.urgent.jumpto),
    awful.key({ modkey,           }, "Tab",
        function ()
            awful.client.focus.history.previous()
            if client.focus then
                client.focus:raise()
            end
        end),

    -- Standard program
    awful.key({ modkey,           }, "Return", function () awful.util.spawn(terminal) end),
    awful.key({ modkey, "Control" }, "r", awesome.restart),
    awful.key({ modkey, "Shift"   }, "q", awesome.quit),

    awful.key({ modkey,           }, "l",     function () awful.tag.incmwfact( 0.05)    end),
    awful.key({ modkey,           }, "h",     function () awful.tag.incmwfact(-0.05)    end),
    awful.key({ modkey, "Shift"   }, "h",     function () awful.tag.incnmaster( 1)      end),
    awful.key({ modkey, "Shift"   }, "l",     function () awful.tag.incnmaster(-1)      end),
    awful.key({ modkey, "Control" }, "h",     function () awful.tag.incncol( 1)         end),
    awful.key({ modkey, "Control" }, "l",     function () awful.tag.incncol(-1)         end),
    awful.key({ modkey,           }, "space", function () awful.layout.inc(layouts,  1) end),
    awful.key({ modkey, "Shift"   }, "space", function () awful.layout.inc(layouts, -1) end),

    awful.key({ modkey, "Control" }, "n", awful.client.restore),

    -- Prompt
    awful.key({ modkey },            "r",     function () promptbox[mouse.screen]:run() end),

    awful.key({ modkey }, "x",
              function ()
                  awful.prompt.run({ prompt = "Run Lua code: " },
                  promptbox[mouse.screen].widget,
                  awful.util.eval, nil,
                  awful.util.getdir("cache") .. "/history_eval")
              end),

    -- Some apps
    awful.key({ modkey }, "b", function () awful.util.spawn(browser) end),
    awful.key({ modkey }, "e", function () awful.util.spawn(explorer) end),
    awful.key({ modkey }, "s", function () awful.util.spawn("spotify") end),
    -- .Xdefaults reload
    awful.key({ modkey }, "z", function () run_once("xrdb -load ~/.Xdefaults") end),

    -- Volume control
    awful.key({ }, "XF86AudioRaiseVolume", volume_up),
    awful.key({ }, "XF86AudioLowerVolume", volume_down),
    awful.key({ }, "XF86AudioMute",        volume_mute)
)

clientkeys = awful.util.table.join(
    awful.key({ modkey,           }, "f",      function (c) c.fullscreen = not c.fullscreen  end),
    awful.key({ modkey, "Shift"   }, "c",      function (c) c:kill()                         end),
    awful.key({ modkey, "Control" }, "space",  awful.client.floating.toggle                     ),
    awful.key({ modkey, "Control" }, "Return", function (c) c:swap(awful.client.getmaster()) end),
    awful.key({ modkey,           }, "o",      awful.client.movetoscreen                        ),
    awful.key({ modkey, "Shift"   }, "r",      function (c) c:redraw()                       end),
    awful.key({ modkey,           }, "t",      function (c) c.ontop = not c.ontop            end),
    awful.key({ modkey,           }, "n",      function (c) c.minimized = not c.minimized    end),
    awful.key({ modkey,           }, "m",
        function (c)
            c.maximized_horizontal = not c.maximized_horizontal
            c.maximized_vertical   = not c.maximized_vertical
        end)
)

-- Compute the maximum number of digit we need, limited to 9
keynumber = 0
for s = 1, screen.count() do
   keynumber = math.min(9, math.max(#tags[s], keynumber));
end

-- Bind all key numbers to tags.
-- Be careful: we use keycodes to make it works on any keyboard layout.
-- This should map on the top row of your keyboard, usually 1 to 9.
for i = 1, keynumber do
    globalkeys = awful.util.table.join(globalkeys,
        awful.key({ modkey }, "#" .. i + 9,
                  function ()
                        local screen = mouse.screen
                        if tags[screen][i] then
                            awful.tag.viewonly(tags[screen][i])
                        end
                  end),
        awful.key({ modkey, "Control" }, "#" .. i + 9,
                  function ()
                      local screen = mouse.screen
                      if tags[screen][i] then
                          awful.tag.viewtoggle(tags[screen][i])
                      end
                  end),
        awful.key({ modkey, "Shift" }, "#" .. i + 9,
                  function ()
                      if client.focus and tags[client.focus.screen][i] then
                          awful.client.movetotag(tags[client.focus.screen][i])
                      end
                  end),
        awful.key({ modkey, "Control", "Shift" }, "#" .. i + 9,
                  function ()
                      if client.focus and tags[client.focus.screen][i] then
                          awful.client.toggletag(tags[client.focus.screen][i])
                      end
                  end))
end

clientbuttons = awful.util.table.join(
    awful.button({ }, 1, function (c) client.focus = c; c:raise() end),
    awful.button({ modkey }, 1, awful.mouse.client.move),
    awful.button({ modkey }, 3, awful.mouse.client.resize))

-- Set keys
root.keys(globalkeys)
-- }}}

-- {{{ Rules
awful.rules.rules = {
    -- All clients will match this rule.
    { rule = { },
      properties = { border_width = beautiful.border_width,
                     border_color = beautiful.border_normal,
                     size_hints_honor = false,
                     focus = true,
                     keys = clientkeys,
                     buttons = clientbuttons } },
    { rule = { class = "MPlayer" },
      properties = { floating = true } },
    { rule = { class = "pinentry" },
      properties = { floating = true } },
    { rule = { class = "gimp" },
      properties = { floating = true } },
}
-- }}}

-- {{{ Signals
-- Signal function to execute when a new client appears.
client.add_signal("manage", function (c, startup)
    -- Add a titlebar
    -- awful.titlebar.add(c, { modkey = modkey })

    -- Enable sloppy focus
    c:add_signal("mouse::enter", function(c)
        if awful.layout.get(c.screen) ~= awful.layout.suit.magnifier
            and awful.client.focus.filter(c) then
            client.focus = c
        end
    end)

    if not startup then
        -- Set the windows at the slave,
        -- i.e. put it at the end of others instead of setting it master.
        -- awful.client.setslave(c)

        -- Put windows in a smart way, only if they does not set an initial position.
        if not c.size_hints.user_position and not c.size_hints.program_position then
            awful.placement.no_overlap(c)
            awful.placement.no_offscreen(c)
        end
    end
end)

client.add_signal("focus", function(c) c.border_color = beautiful.border_focus end)
client.add_signal("unfocus", function(c) c.border_color = beautiful.border_normal end)
-- }}}
