# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core import Menu

if __name__ == "__main__":
    try:
        Menu.MAIN.Static()
    except KeyboardInterrupt:
        print("\n\nCtrl c detected Quitting the Program\n")