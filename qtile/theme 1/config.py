# 1
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "v", lazy.next_layout()),
    Key([mod], "space", lazy.spawn("rofi -show run")),
    #Key([mod], "z", lazy.span("rofi -show window")),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            Key([mod], "Tab", lazy.screen.next_group()),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
     layout.Columns(
         border_focus = "#A77AC4",
         border_normal = "#808080",
         border_width=3,
         margin=8,
         border_on_single=True,
         margin_on_single=20,
    ),
    layout.Max(),
    layout.MonadTall(
        # border_focus = colors[6],
        # border_normal = colors[4],
        border_width=3,
        margin=5,
        border_on_single=True,
        margin_on_single=10,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# these colours have no use here tho
colors = [
    ["#293136", "#293136"],  # color 0
    ["#3b4252", "#3b4252"],  # color 1
    ["#8c8c8c", "#8c8c8c"],  # color 2
    ["#565b78", "#565b78"],  # color 3
    ["#a1acff", "#a1acff"],  # color 4
    ["#ffffff", "#ffffff"],  # color 5
    ["#9293d2", "#9293d2"],  # color 6
    ["#89b8fd", "#89b8fd"],  # color 7
    ["#e2c5dc", "#e2c5dc"],  # color 8
    ["#0ee9af", "#0ee9af"],  # color 9
    ["#e9c46a", "#e9c46a"],  # color 10
    ["#4f76c7", "#4f76c7"],  # color 11
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=2,
    rounded=True,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=20,
                    background='#1F1D2E'
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/launch_Icon.png",
                    margin=2,
                    background='#1F1D2E'
                ),
                widget.Image(filename="~/.config/qtile/Assets/6.png"),
                widget.GroupBox(
                    fontsize=20,
                    borderwidth=3,
                    highlight_method='block',
                    active='#7F61A7',
                    block_highlight_text_color="#CFB3E5",
                    highlight_color='#4B427E',
                    inactive='#BD85CB',
                    foreground='#4B427E',
                    background='#4B427E',
                    this_current_screen_border='#52548D',
                    this_screen_border='#52548D',
                    other_current_screen_border='#52548D',
                    other_screen_border='#52548D',
                    urgent_border='#52548D',
                    disable_drag=True,
                ),
                widget.Image(filename="~/.config/qtile/Assets/5.png"),
                widget.CurrentLayoutIcon(
                    background='#52548D',
                    padding=0,
                    scale=0.5,
                ),
                widget.CurrentLayout(
                    background="#52548D",
                    font='JetBrains Mono Bold'
                ),
                widget.Image(filename="~/.config/qtile/Assets/4.png"),
                widget.Prompt(
                    background='#6a6aa0',
                    font='JetBrains Mono Bold',
                ),
                widget.WindowName(
                    background='#7676B2',
                    format="{name}",
                    font='JetBrains Mono Bold',
                    empty_group_string='Desktop',
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free Solid",
                    fontsize=20,
                    background='#7676B2',
                ),
                widget.CheckUpdates(
                    distro="Fedora",
                    background='#7676B2',
                    no_update_string="0",
                    font="JetBrains Mono Bold",
                    padding=5
                ),
                widget.Image(filename="~/.config/qtile/Assets/3.png"),
                widget.Systray(background='#52548D', padding=5),
                widget.Spacer(length=10, background='#52548D'),
                widget.Image(filename="~/.config/qtile/Assets/2.png"),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=20,
                    background='#4B427E',
                ),
                widget.Net(
                    prefix="M",
                    measure_mem='G',
                    font="JetBrains Mono Bold",
                    background='#4B427E',
                    interface="wlp6s0"
                ),
                widget.Spacer(length=10, background='#4B427E'),
                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free Solid",
                    fontsize=20,
                    background='#4B427E',
                ),
                widget.CPU(
                    format="{load_percent}%",
                    measure_mem='G',
                    font="JetBrains Mono Bold",
                    fontsize=12,
                    background='#4B427E',
                ),
                widget.Spacer(length=10, background='#4B427E'),
                widget.TextBox(
                    text="﬙",
                    font="Font Awesome 6 Free Solid",
                    fontsize=20,
                    background='#4B427E',
                ),
                widget.Memory(
                    measure_mem='G',
                    font="JetBrains Mono Bold",
                    fontsize=12,
                    background='#4B427E',
                ),
                widget.Spacer(length=10, background='#4B427E'),
                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free Solid",
                    fontsize=25,
                    background='#4B427E',
                ),
                widget.PulseVolume(
                    font='JetBrains Mono Bold',
                    fontsize=12,
                    background='#4B427E',
                ),
                widget.Image(filename="~/.config/qtile/Assets/1.png"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=20,
                    background='#1F1D2E',
                ),
                widget.Clock(
                    format='%I:%M %p',
                    background='#1F1D2E',
                    font="JetBrains Mono Bold",
                ),
                widget.Spacer(length=10, background='#1F1D2E'),
                widget.QuickExit(
                    background='#1F1D2E',
                    font="JetBrains Mono Bold",
                ),
            ],
            28,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Picture-in-Picture"), #picture in picture
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

def autostart_once():
    subprocess.run('~/.config/qtile/autostart_once.sh')# path to my script, under my user directory
    subprocess.call([home])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


