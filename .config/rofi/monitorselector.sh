#!/bin/bash



## Monitor Selector



MENU="$(rofi -sep "|" -dmenu -i -p 'Monitor Selector' -width 12 -hide-scrollbar -line-padding 4 -padding 20 -lines 7 -font "Misc Termsyn 12" <<< "1-Notebook|2-HDMI|3-HDMI+Notebook|4-Notebook+HDMI|5-VGA|6-VGA+Notebook|7-Notebook+VGA")"

            case "$MENU" in

                *1-Notebook) echo Notebook && xrandr --output LVDS1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP1 --off --output HDMI1 --off --output VGA1 --off --output VIRTUAL1 --off && qtile-cmd -o cmd -f restart;;

                *2-HDMI) echo HDMI && xrandr --output LVDS1 --off --output DP1 --off --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VGA1 --off --output VIRTUAL1 --off && qtile-cmd -o cmd -f restart;;

                *3-HDMI+Notebook) echo HDMI+Notebook && xrandr --output LVDS1 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output DP1 --off --output HDMI1 --mode 1920x1080 --pos 0x0 --rotate normal --output VGA1 --off --output VIRTUAL1 --off && qtile-cmd -o cmd -f restart;;

                *4-Notebook+HDMI) echo Notebook+HDMI && xrandr --output LVDS1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP1 --off --output HDMI1 --mode 1920x1080 --pos 1920x0 --rotate normal --output VGA1 --off --output VIRTUAL1 --off && qtile-cmd -o cmd -f restart;;

                *5-VGA) echo VGA && xrandr --output LVDS1 --off --output DP1 --off --output HDMI1 --off --output VGA1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off && qtile-cmd -o cmd -f restart;;

                *6-VGA+Notebook) echo VGA+Notebook && xrandr --output LVDS1 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output DP1 --off --output HDMI1 --off --output VGA1 --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off && qtile-cmd -o cmd -f restart;;

                *7-Notebook+VGA) echo Notebook+VGA && xrandr --output LVDS1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP1 --off --output HDMI1 --off VGA1 --mode 1920x1080 --pos 1920x0 --rotate normal --output --output VIRTUAL1 --off && qtile-cmd -o cmd -f restart

            esac