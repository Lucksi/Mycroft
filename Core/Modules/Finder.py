# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class OBJECT:
    
    @staticmethod
    def FOUND(text,term):
        count = 0
        line_c = 0
        f_lines = []
        f = open(text,"r")
        reader = f.readlines()
        for line in reader:
            line_c = line_c + 1
            if term in line:
                count = count + 1
                f_lines.append(line_c)
        if count > 0:
            is_found = str(count)
        else:
            is_found = "Not Found"
        return is_found,str(f_lines)