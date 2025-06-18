# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core import Menu
from Core.Utils import Database

if __name__ == "__main__":
    try:
        Database.DATABASE.CREATE()
        Menu.MAIN.Static()
    except KeyboardInterrupt:
        print("\n\nCtrl c detected Quitting the Program\n")
