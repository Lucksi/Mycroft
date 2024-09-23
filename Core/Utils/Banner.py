# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Clear

class GET_BANNER:

    @staticmethod
    def Banner(clear_mode):
        if clear_mode == 1:
            Clear.SCREEN.Clear()
        f = open("Banner/Banner.txt", "r", newline=None)
        for line in f:
            print(Colors.Color.ORANGE + line.replace("\n", ""))
        f.close()
        print(Colors.Color.WHITE + "\nA File Analyzer and Metadata Scraper\t  Coded by Lucksi")
        print(Colors.Color.ORANGE + "____________________________________________________")
        print(Colors.Color.ORANGE + "|" + Colors.Color.WHITE + " Instagram:lucks_022" +
              Colors.Color.ORANGE + "                              |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.WHITE + " Email:lukege287@gmail.com" +
              Colors.Color.ORANGE + "                        |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.WHITE + " GitHub:Lucksi" +
              Colors.Color.ORANGE + "                                    |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.WHITE + " Twitter:@Lucksi_22" +
              Colors.Color.ORANGE + "                               |")
        print(Colors.Color.ORANGE + "|" + Colors.Color.WHITE +
              " Linkedin:https://www.linkedin.com/in/lucksi" + Colors.Color.ORANGE + "      |")
        print(Colors.Color.ORANGE + "----------------------------------------------------")
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} For quitting the program".format(Colors.Color.GREEN + "exit" + Colors.Color.WHITE))
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} For opening the help menu".format(Colors.Color.GREEN + "help" + Colors.Color.WHITE))
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} For listing files".format(Colors.Color.GREEN + "list" + Colors.Color.WHITE))