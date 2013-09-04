#!/bin/bash

while [ 1 -eq 1 ]
do
    for i in $(echo /home/singlepig/pictures/wallpapers/*.*)
        do
            echo $i
            gsettings set org.gnome.desktop.background picture-uri file:///${i}
            sleep 120
    done
done
