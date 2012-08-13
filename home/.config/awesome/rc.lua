-- Standard awesome library
require("awful")
require("awful.autofocus")
require("awful.rules")
-- Theme handling library
require("beautiful")
-- Notification library
require("naughty")
require("vicious")
require("blingbling")

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

socket = require "socket"
hostname = socket.dns.gethostname()

-- {{{ Variable definitions
-- Themes define colours, icons, and wallpapers
config = awful.util.getdir("config")
beautiful.init(config .. "/themes/black_blue/theme.lua")

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

-- This is used later as the default terminal and editor to run.
terminal = "urxvtcd"
editor = os.getenv("EDITOR") or "vim"
editor_cmd = terminal .. " -e " .. editor
browser = "google-chrome"
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

--pango
pango_small="size=\"small\""
pango_x_small="size=\"x-small\""
pango_xx_small="size=\"xx-small\""
pango_bold="weight=\"bold\""

--Separator
spacer = widget({ type = "textbox" })
spacer.text = " "
spicon = widget({ type = "textbox" })
spicon.text = "<span color='#EEEE66'> | </span>"

-- {{{ CPU usage
-- Initialize widgets
cpugraph=blingbling.classical_graph.new()
cpugraph:set_width(100)
cpugraph:set_tiles_color("#00000022")
cpugraph:set_show_text(true)
cpugraph:set_label("CPU $percent %")
vicious.register(cpugraph, vicious.widgets.cpu,'$1',2)

corelabel=widget({ type = "textbox" })
corelabel.text="<span color=\""..beautiful.textbox_widget_as_label_font_color.."\" "..pango_small..">Cores:</span>"

function my_core(core)
  corewidget = blingbling.progress_graph.new()
  corewidget:set_height(18)
  corewidget:set_width(6)
  corewidget:set_filled(true)
  corewidget:set_h_margin(1)
  corewidget:set_filled_color("#00000033")
  vicious.register(corewidget, vicious.widgets.cpu, core)
  
  return corewidget
end

netspeed_widget = blingbling.net.new()
netspeed_widget:set_height(18)
netspeed_widget:set_show_text(true)
netspeed_widget:set_v_margin(3)

if hostname == "delorean" then
    netspeed_widget:set_interface("wlan0")
else
    netspeed_widget:set_interface("eth0")
end

if hostname ~= "windy" then
    --Volume
    volume_label = widget({ type = "textbox"})
    volume_label.text='<span '..pango_small..'><span color="'..beautiful.textbox_widget_as_label_font_color..'">Vol.: </span></span>'
    my_volume=blingbling.volume.new()
    my_volume:set_height(16)
    my_volume:set_v_margin(3)
    my_volume:set_width(20)
    my_volume:update_master()
    my_volume:set_master_control()
    my_volume:set_bar(true)
    my_volume:set_background_graph_color("#00000099")
    my_volume:set_graph_color("#00ccffaa")
end

--udisks-glue menu
  udisks_glue=blingbling.udisks_glue.new(beautiful.udisks_glue)
  udisks_glue:set_mount_icon(beautiful.accept)
  udisks_glue:set_umount_icon(beautiful.cancel)
  udisks_glue:set_detach_icon(beautiful.cancel)
  udisks_glue:set_Usb_icon(beautiful.usb)
  udisks_glue:set_Cdrom_icon(beautiful.cdrom)
  awful.widget.layout.margins[udisks_glue.widget]= { top = 4}
  udisks_glue.widget.resize= false

if hostname == "delorean" then
    -- Wifiwidget -- Shows connected wlan and signal quality
    wifiwidget = widget({ type = "textbox" })
    wifiwidget.align = "right"
    wifiwidget.bg_image = image(config .. "/icons/wifi.png")
    wifiwidget.bg_align = "left"
    wifiwidget.bg_resize = true
    vicious.register(wifiwidget, vicious.widgets.wifi, "    ${ssid}  ${link}/70", 5, "wlan0")
end

if hostname == "windy" then
    -- Create a battery widget
    baticon = widget({ type = "imagebox" })
    baticon.image = image(config .. "/icons/dust/bat.png")
    --Initialize widget
    batwidget = widget({ type = "textbox" })
    vicious.register(batwidget,  vicious.widgets.bat, "$1$2", 32, "BAT1")
end

--Calendar widget and date
calendar = blingbling.calendar.new({type = "imagebox", image = beautiful.calendar})
calendar:set_cell_padding(2)
calendar:set_title_font_size(9)
calendar:set_font_size(8)
calendar:set_inter_margin(1)
calendar:set_columns_lines_titles_font_size(8)
calendar:set_columns_lines_titles_text_color("#d4aa00ff")

datewidget = widget({ type = "textbox" })
vicious.register(datewidget, vicious.widgets.date, 
    '<span color="' .. beautiful.text_font_color_1 .. '" ' .. pango_small ..">%b %d, %R</span>", 60)

--Register widgets

-- Shutdown and reboot
shutdown=blingbling.system.shutdownmenu(beautiful.shutdown, beautiful.accept, beautiful.cancel)
shutdown.resize = false
awful.widget.layout.margins[shutdown] = {top=4}
reboot=blingbling.system.rebootmenu(beautiful.reboot, beautiful.accept, beautiful.cancel)
reboot.resize = false
awful.widget.layout.margins[reboot] = {top=4}

-- Create a systray
mysystray = widget({ type = "systray" })

-- Create a wibox for each screen and add it
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


function get_widgets (s)
    leftwidgets = {
        taglist[s], spacer, layoutbox[s], spacer, 
        promptbox[s],
        layout = awful.widget.layout.horizontal.leftright
    }

    local widgets
    if hostname == "windy" then
        widgets = {
            leftwidgets,
            spacer, udisks_glue.widget, 
            s == 1 and mysystray or nil,
            spicon, datewidget, spacer, calendar.widget,
            spicon, netspeed_widget.widget,
            spicon, spacer, cpugraph.widget,
            spicon, batwidget, baticon,
            mytasklist[s],
            layout = awful.widget.layout.horizontal.rightleft,
        }
    else
        widgets = {
            leftwidgets,
            spacer, shutdown, spacer, reboot, spacer, udisks_glue.widget, 
            s == 1 and mysystray or nil,
            my_volume.widget, volume_label,
            spicon, datewidget, spacer, calendar.widget,
            spicon, netspeed_widget.widget,
            spicon, spacer, cpugraph.widget,
            spicon, wifiwidget,
            mytasklist[s],
            layout = awful.widget.layout.horizontal.rightleft,
        }
    end

    return widgets
end

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
    wibox[s] = awful.wibox({ position = "top", screen = s, bg = theme.bg_normal})
    -- Add widgets to the wibox - order matters
    wibox[s].widgets = get_widgets(s)
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
    { rule = { class = "feh" },
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
-- vim: ts=4:sw=4:softtabstop=4
