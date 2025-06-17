# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os

Windows = "nt"


class SCREEN:

    def Clear():
        os.system("cls" if os.name == Windows else "clear")
