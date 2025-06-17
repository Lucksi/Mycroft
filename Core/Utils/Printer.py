# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Formatting
from Core.Utils import Write_File

class GENERATE:

    @staticmethod
    def Sentence(var,nochar,placeholder,w_file,out_file,d_char,var2,display):
        if placeholder == "LINE":
            print("")
        if placeholder == "Password-Protected":
            if display == 1:
                if var != nochar:
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Password-Protected: " + Colors.Color.GREEN + "True" + Colors.Color.WHITE + " Encoded-Base64Binary-Password: " + Colors.Color.GREEN +  var)
                else:
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Password-Protected: " + Colors.Color.GREEN + "False" )
            format = 1
        if var != nochar:
            if placeholder != "Revision: " and placeholder != "Metadata-Order: " and placeholder != "Toolkit: " and placeholder != "Focus-Mode: " and placeholder != "Flash-Compensation: " and placeholder != "Altitude: ":
                if display == 1:
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + placeholder + Colors.Color.GREEN + Formatting.TEXT.FORMATTED(var))
                format = 1
            elif placeholder == "Revision: ":
                if display == 1:
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + placeholder + Colors.Color.GREEN + Formatting.TEXT.FORMATTED(var) + " Times")
                format = 4
            elif placeholder == "Metadata-Order: " or placeholder == "Focus-Mode: " or placeholder == "Altitude: ":
                if display == 1:
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + placeholder + Colors.Color.GREEN + "{}".format(var))
                format = 2
            elif placeholder == "Toolkit: " or placeholder == "Flash-Compensation: ":
                if display == 1:
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + placeholder + Colors.Color.GREEN + Formatting.TEXT.FORMATTED_EV(var))
                format = 3
        else:
            format = 0
        if w_file == 1:
            f = open(out_file,"a")
            if placeholder == "LINE":
                f.write("\n")
            else:
                if d_char == 1:
                    if format == 1:
                        Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(var),f,placeholder)
                    elif format == 2:
                        Write_File.OUTPUT.LINE(var,f,placeholder)
                    elif format == 3:
                        Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED_EV(var),f,placeholder)
                    else:
                        pass
                else:
                    Write_File.OUTPUT.D_LINE(str(var),str(var2),f,placeholder)
            f.close()
    
    @staticmethod
    def Comment_Sentence(var,nochar,placeholder,w_file,out_file,d_char,var2,display):
        if var != nochar:
            if display == 1:
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + placeholder + Colors.Color.GREEN + var)
        if w_file == 1:
            f = open(out_file,"a")
            if d_char == 1:
                Write_File.OUTPUT.LINE(var,f,placeholder)
            else:
                Write_File.OUTPUT.D_LINE(str(var),str(var2),f,placeholder)
            f.close()