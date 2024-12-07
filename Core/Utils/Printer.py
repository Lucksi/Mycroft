# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Formatting

class GENERATE:

    def Sentence(var,nochar,placeholder):
        if placeholder == "Password-Protected":
            if var != nochar:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Password-Protected: " + Colors.Color.GREEN + "True" + Colors.Color.WHITE + " Encoded-Base64Binary-Password: " + Colors.Color.GREEN +  var)
            else:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Password-Protected: " + Colors.Color.GREEN + "False" )
        if var != nochar:
            if placeholder != "Revision":
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + placeholder + Colors.Color.GREEN + Formatting.TEXT.FORMATTED(var))
            else:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + placeholder + Colors.Color.GREEN + Formatting.TEXT.FORMATTED(var) + "Times")