# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from Core.Utils import Colors

class GET:

    @staticmethod
    def Files(list):
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Listing Files...\n")
        if list == "":
            name = "Files"
        else:
            name = list
        if os.path.isdir(name):
            d = 0
            f = 0
            for file in os.listdir(name):
                if os.path.isfile(name + "/" + file):
                    f = f +1
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "File n°{}: {}".format(Colors.Color.GREEN + str(f) + Colors.Color.WHITE,Colors.Color.GREEN + file))
                else:
                    d = d +1 
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Directory n°{}: {}".format(Colors.Color.GREEN + str(d) + Colors.Color.WHITE,Colors.Color.GREEN + file))
        else:
            print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "Folder: {} not found".format(Colors.Color.GREEN + name + Colors.Color.WHITE))
