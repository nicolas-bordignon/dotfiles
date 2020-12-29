import os, subprocess
import re
from libqtile import hook
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile.dgroups import simple_key_binder
from Xlib import display as xdisplay

# ----------------------------
# -------- Hotkeys -----------
# ----------------------------

mod = "mod4"
keys =[
    # Layout hotkeys
    Key([mod, "control"], "l", lazy.layout.grow()),
    Key([mod, "control"], "h", lazy.layout.shrink()),
    Key([mod, "mod1"], "j", lazy.layout.grow_down()),
    Key([mod, "mod1"], "k", lazy.layout.grow_up()),
    Key([mod, "mod1"], "h", lazy.layout.grow_left()),
    Key([mod, "mod1"], "l", lazy.layout.grow_right()),
    Key([mod, "mod1"], "Return", lazy.layout.toggle_split()),
    Key([mod], "h",
        lazy.layout.left()),
    Key([mod], "l",
        lazy.layout.right()), 
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.layout.flip()),
    Key([mod], "minus", lazy.layout.normalize()),
    Key([mod], "equal", lazy.layout.maximize()),
    Key([mod], 'b', lazy.hide_show_bar()),

    # Window hotkeys
    Key([mod], "space", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),

    # Spec hotkeys
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show window")),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Apps hotkeys
    Key([mod], "Return", lazy.spawn("kitty")),
    Key([mod], "a", lazy.spawn("gnome-calendar")),
    Key([mod], "w", lazy.spawn("webstorm")),
    Key([mod, "shift"], "w", lazy.spawn("pycharm")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod, "shift"], "c", lazy.spawn("gitkraken")),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod], "e", lazy.spawn("evolution")),
    Key([mod], "f", lazy.spawn("firefox-developer-edition")),
    Key([mod, "shift"], "f", lazy.spawn("firefox-developer-edition -private-window")),
    Key([mod], "g", lazy.spawn("lutris")),
    Key([mod, "shift"], "g", lazy.spawn("retroarch")),
    Key([mod], "m", lazy.spawn("speedcrunch")),
    Key([mod], "n", lazy.spawn("nautilus")),
    Key([mod, "shift"], "n", lazy.spawn("notion-app")),
    Key([mod], "o", lazy.spawn("libreoffice")),
    Key([mod], "s", lazy.spawn("steam-native")),
    Key([mod], "t", lazy.spawn("telegram-desktop")),
    Key([mod, "shift"], "t", lazy.spawn("transmission-gtk")),
    Key([mod], "z", lazy.spawn("zotero")),  

    # System hotkeys
    Key([mod, "shift", "control"], "F11", lazy.spawn("reboot")),
    Key([mod, "shift", "control"], "F12", lazy.spawn("poweroff")),
    Key([], "Print", lazy.spawn("flameshot full -p /home/nicolas-bordignon/Imagens/Screenshots")),
    Key(["shift"], "Print", lazy.spawn("flameshot gui -p /home/nicolas-bordignon/Imagens/Screenshots")),
    Key([mod],"p", lazy.spawn('.config/rofi/monitorselector.sh')),
    Key([], 'XF86TouchpadToggle', lazy.spawn('.config/qtile/touchpadtoggle.sh')),

    # Media hotkeys
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +5%')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -5%')),
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
]


groups = [
    Group(name ='Dev', 
          init = True, 
          persist = True, 
          matches = [Match(wm_instance_class =
                           ['code-oss','jetbrains-webstorm','jetbrains-pycharm', 'libreoffice', 'libreoffice-writer', 'libreoffice-calc','libreoffice-base','libreoffice-math','libreoffice-draw','libreoffice-impress', 'soffice', 'Eclipse', 'notion'])],
          layout ='monadtall',
          position = 1,
          exclusive = False,
          ),
    Group(name ='Dev2', 
          init = True, 
          persist = True, 
          screen_affinity= 1,
          matches = [Match(wm_instance_class = ['evince', 'org.pwmt.zathura'])],
          layout ='monadtall',
          position = 2,
          exclusive = False,
          ),
    Group(name ='Dev3', 
          init = True, 
          persist = True, 
          screen_affinity= 1,
          matches = [Match(wm_instance_class = ['Inkscape','org.inkscape.Inkscape', 'gimp-2.10', 'dia'])],
          layout ='monadtall',
          position = 3,
          exclusive = False,
          ),
    Group(name ='www', 
          init = False, 
          persist = False, 
          matches = [Match(wm_class = ["firefoxdeveloperedition",'Transmission-gtk'])],
          position = 4,
          layout = 'max',
          exclusive = False,
          ),
    Group(name ='Ref',
          init = False,
          persist = False,
          screen_affinity= 1, 
          matches = [Match(wm_class = ['Zotero'])],
          layout ='max',
          position = 5,
          exclusive = False,
          ),
    Group(name ='Git', 
          init = False, 
          persist = False, 
          matches = [Match(wm_instance_class = ['gitkraken'])],
          layout ='max',
          position = 6,
          exclusive = False,
          ),
    Group(name ='Files', 
          init = False, 
          persist = False, 
          matches = [Match(wm_instance_class = ['org.gnome.Nautilus'])],
          layout ='monadtall',
          position = 7,
          exclusive = False,
          ),
    Group(name ='Mail', 
          init = False, 
          persist = False, 
          matches = [Match(wm_instance_class = ['evolution','gnome-calendar'])],
          layout ='monadwide',
          position = 8,
          exclusive = False,
          ),
    Group(name ='Chat', 
          init = False, 
          persist = False, 
          matches = [Match(wm_instance_class = ['skypeforlinux', 'discord', 'slack', 'telegram-desktop'])],
          layout ='monadtall',
          position = 9,
          exclusive = False,
          ),
    Group(name ='Game', 
          init=False, 
          persist=False, 
          layout='monadtall',
          matches=[Match(wm_class=['Steam', 'lutris', 'Lutris', 'retroarch'])],
          position=10, 
          exclusive=False,
          ),
    Group(name ='Run', 
          init=False, 
          persist=False, 
          layout='max',
          matches=[Match(wm_class=['steam_app_1286830'])],
          position=11, 
          exclusive=False,
          ),
    Group(name ='Video', 
          init = False, 
          persist = False, 
          screen_affinity= 1,
          matches = [Match(wm_instance_class = ['io.github.celluloid_player.Celluloid'])],
          layout ='max',
          position = 12,
          exclusive = False,
          ),
    ]

# auto bind keys to dgroups mod+1 to 9
dgroups_key_binder = simple_key_binder(mod)

# ---------------------------
# ---- Layouts & Widgets ----
# ---------------------------
colors = {
    'background': '282a36',
    'foreground': 'f8f8f2',
    'border' : '6272a4',
    'alert':'ff5555',
    'select': '50fa7b'
}
# Layout Theme
layout_theme = {
    "border_width": 2,
    "margin": 2,
    "border_focus": colors['border'],
    "border_normal": colors['background']
    }
layout_theme_bsp = {
    "grow_amount":2,
    "border_focus": colors['border'],
    "border_normal": colors['background']
    }

layouts = [
    layout.MonadTall(
        **layout_theme,
        ratio=0.59,
        single_border_width=0,
        single_margin = 0
    ),
    layout.MonadWide(
        **layout_theme,
        ratio=0.55,
        single_border_width=0,
        single_margin = 0
    ),
    layout.Bsp(
    **layout_theme_bsp,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font ='Fira Code',
    fontsize =12,
    padding = 2,
    background = colors['background'],
    foreground = colors['foreground'],
    border = colors['border'],
)
def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

num_monitors = get_num_monitors()
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.65),
                widget.GroupBox(hide_unused = False,
                                disable_drag = True,
                                highlight_method = 'line',
                                spacing = 0,
                                borderwidth = 2,
                                highlight_color = [colors['border'],'282a36'],
                                active = colors['foreground'],
                                inactive = colors['border'],
                                this_screen_border = colors['border'],
                                this_current_screen_border = colors['border'],
                                other_screen_border = colors['foreground'],
                                other_current_screen_border = colors['foreground'],
                                urgent_alert_method = 'line',
                                urgent_text = colors['alert'],
                                urgent_border = colors['alert'] 
                                ),
                widget.TaskList(highlight_method = 'border',
                                txt_floating = '🗗',
                                txt_minimized = '🗕',
                                padding_x = 5,
                                padding_y = 1,
                                icon_size = 15,
                                title_width_method = 'uniform'),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Clock(format = '%a, %d de %b %H:%M'),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Pomodoro(prefix_inactive = 'Pomodoro', prefix_paused ='Paused', color_inactive= colors['foreground'],color_active = colors['select'],color_break = colors['alert']),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Memory(format = 'M: {MemUsed}M'),
                widget.MemoryGraph(type = 'linefill',
                                   border_color = colors['border'],
                                   graph_color = colors['border']),
                widget.TextBox(text = 'CPU:'),
                widget.ThermalSensor(tag_sensor='Package id 0', threshold = 85,
                foreground_alert = colors['alert']),
                widget.CPUGraph(type = 'linefill',
                                border_color = colors['border'],
                                graph_color = colors['border'],
                                core = 'all'),
                widget.CPU(format = '{freq_current}GHz {load_percent}%',),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.TextBox(text = 'AMD:'),
                widget.ThermalSensor(tag_sensor ='edge', threshold = 85,
                foreground_alert = colors['alert']),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Systray(padding = 10),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Volume(emoji = False,
                              theme_path = '/home/nicolas-bordignon/.config/qtile/volume-icons',
                              padding =3),
                widget.Volume(),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.BatteryIcon(theme_path = '/home/nicolas-bordignon/.config/qtile/battery-icons',
                                   update_interval = 5),
                widget.Battery(discharge_char='', charge_char='',format = '{char} {percent:2.0%}' ),
            ],
            22,
        ),
    )   
]
if num_monitors > 1:
    for m in range(num_monitors - 1):
        screens.append(
                Screen(
        top=bar.Bar(
            [
                                widget.CurrentLayoutIcon(scale=0.65),
                widget.GroupBox(hide_unused = False,
                                disable_drag = True,
                                highlight_method = 'line',
                                spacing = 0,
                                borderwidth = 2,
                                highlight_color = [colors['border'],'282a36'],
                                active = colors['foreground'],
                                inactive = colors['border'],
                                this_screen_border = colors['border'],
                                this_current_screen_border = colors['border'],
                                other_screen_border = colors['foreground'],
                                other_current_screen_border = colors['foreground'],
                                urgent_alert_method = 'line',
                                urgent_text = colors['alert'],
                                urgent_border = colors['alert'] ),
                widget.TaskList(highlight_method = 'border',
                                txt_floating = '🗗',
                                txt_minimized = '🗕',
                                padding_x = 5,
                                padding_y = 1,
                                icon_size = 15,
                                title_width_method = 'uniform'),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Clock(format = '%a, %d de %b %H:%M'),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Pomodoro(prefix_inactive = 'Pomodoro', prefix_paused ='Paused', color_inactive= 'ffffff'),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Memory(format = 'M: {MemUsed}M'),
                widget.MemoryGraph(type = 'linefill',
                                   border_color = colors['border'],
                                   graph_color = colors['border']),
                widget.TextBox(text = 'CPU:'),
                widget.ThermalSensor(tag_sensor='Package id 0', threshold = 85),
                widget.CPUGraph(type = 'linefill',
                                border_color = colors['border'],
                                graph_color = colors['border'],
                                core = 'all'),
                widget.CPU(format = '{freq_current}GHz {load_percent}%',),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.TextBox(text = 'AMD:'),
                widget.ThermalSensor(tag_sensor ='edge', threshold = 85),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.Volume(emoji = False,
                              theme_path = '/home/nicolas-bordignon/.config/qtile/volume-icons',
                              padding =3),
                widget.Volume(),
                widget.Sep(foreground = colors['border'],
                           padding = 40,
                           linewidth = 2,
                           size_percent = 30,),
                widget.BatteryIcon(theme_path = '/home/nicolas-bordignon/.config/qtile/battery-icons',
                                   update_interval = 5),
                widget.Battery(discharge_char='', charge_char='',format = '{char} {percent:2.0%}' ),
            ],
            22,
        ),
    )
        )

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
]

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
# floating_layout = layout.Floating(
#     border_width = 2,
#     border_focus = colors['border'],
#     border_normal = colors['background'],
#     auto_float_types=[
#   "notification",
#   "toolbar",
#   "splash",
#   "dialog",
# ],
#     float_rules=[
#     # Run the utility of `xprop` to see the wm class and name of an X client.
#     {'wmclass': 'confirm'},
#     {'wmclass': 'dialog'},
#     {'wmclass': 'download'},
#     {'wmclass': 'error'},
#     {'wmclass': 'file_progress'},
#     {'wmclass': 'notification'},
#     {'wmclass': 'splash'},
#     {'wmclass': 'toolbar'},
#     {'wmclass': 'confirmreset'},  # gitk
#     {'wmclass': 'makebranch'},  # gitk
#     {'wmclass': 'maketag'},  # gitk
#     {'wname': 'branchdialog'},  # gitk
#     {'wname': 'pinentry'},  # GPG key password entry
#     {'wmclass': 'ssh-askpass'},  # ssh-askpass
#     {'wmclass': 'Gnome-keyring-prompt'},
#     {'wmclass': 'SpeedCrunch'},
#     # {'wmclass': 'evolution-alarm-notify'},
#     {'wmclass': 'gcr-prompter'},
#     {'wmclass': 'Gcr-prompter'},
# ])
auto_fullscreen = True
focus_on_window_activation = "focus"
extentions = []
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

