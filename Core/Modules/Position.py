# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0 

 
class FINDER:

    @staticmethod
    def ENCRYPTION_PDF(character,file):
        i = 0
        index = 0
        char = character.replace("0 R","0 obj").lstrip().rstrip().encode()
        n_p = character.replace("0 R","").rstrip()
        n_p2 = int(n_p) + 1
        n_p2 = str(n_p2)
        char_e = n_p2 + " 0 obj"
        char_e = char_e.encode()
        ch2 = char + b"\n"
        for line in file:
            try:
                if b"<< " in line:
                    line = line.split(b"<< ",1)[1]
            except Exception as e:
                continue
            if char in line:
                if ch2 in line:
                    index = i + 1
                    break
                else:
                    index = i
            i = i + 1
        return index,char_e