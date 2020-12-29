#!/bin/sh

picom &
nm-applet &
blueman-applet &
feh --randomize --bg-fill ~/Imagens/Backgrounds/* &
xfce4-power-manager &
light-locker &
synclient TouchpadOff=1 &

# código para configurar o teclado do note /? no ctrl direito 
# sudo sed -i '30s|.*|key <RCTL>{[slash,question,degree]};|' \
#/usr/share/X11/xkb/symbols/pc 