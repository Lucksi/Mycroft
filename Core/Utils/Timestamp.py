# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from datetime import datetime

class GET:

    @staticmethod
    def Date(timestamp):
        intial = datetime.fromtimestamp(timestamp)
        formatted = intial.strftime("%Y-%m-%d %H:%M:%S")
        return formatted