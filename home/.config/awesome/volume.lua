--function update_volume(widget)
--    local fd = io.popen("amixer sget Master")
--    local status = fd:read("*all")
--    fd:close()
--    
--    local volume = tonumber(string.match(status, "(%d?%d?%d)%%")) / 100
--    -- volume = string.format("% 3d", volume)
--
--    status = string.match(status, "%[(o[^%]]*)%]")
--
--    -- starting colour
--    local sr, sg, sb = 0x3F, 0x3F, 0x3F
--    -- ending colour
--    local er, eg, eb = 0xDC, 0xDC, 0xCC
--
--    local ir = volume * (er - sr) + sr
--    local ig = volume * (eg - sg) + sg
--    local ib = volume * (eb - sb) + sb
--    interpol_colour = string.format("%.2x%.2x%.2x", ir, ig, ib)
--    if string.find(status, "on", 1, true) then
--        volume = " <span background='#" .. interpol_colour .. "'>   </span>"
--    else
--        volume = " <span color='red' background='#" .. interpol_colour .. "'> M </span>"
--    end
--    widget.text = volume
-- end
--

function volume_up()
    awful.util.spawn("amixer -q set Master 9%+")
end

function volume_down()
    awful.util.spawn("amixer -q set Master 9%-")
end

function volume_mute()
    awful.util.spawn("amixer -q set Master toggle")
end
--
--volume_widget = widget({ type = "textbox" })
--update_volume(volume_widget)

-- {{{ Volume level
volicon = widget({ type = "imagebox" })
volicon.image = image(beautiful.widget_vol)
-- Initialize widgets
volbar    = awful.widget.progressbar()
volwidget = widget({ type = "textbox" })
-- Progressbar properties
volbar:set_vertical(true):set_ticks(true)
volbar:set_height(12):set_width(8):set_ticks_size(2)
volbar:set_background_color(beautiful.fg_off_widget)
volbar:set_gradient_colors({ beautiful.fg_widget,
   beautiful.fg_center_widget, beautiful.fg_end_widget
}) -- Enable caching
vicious.cache(vicious.widgets.volume)
-- Register widgets
vicious.register(volbar,    vicious.widgets.volume,  "$1",  2, "PCM")
vicious.register(volwidget, vicious.widgets.volume, " $1%", 2, "PCM")
-- Register buttons
volbar.widget:buttons(awful.util.table.join(
   awful.button({ }, 1, function () exec("kmix") end),
   awful.button({ }, 4, function () exec("amixer -q set PCM 2dB+", false) end),
   awful.button({ }, 5, function () exec("amixer -q set PCM 2dB-", false) end)
)) -- Register assigned buttons
volwidget:buttons(volbar.widget:buttons())
-- }}}
