# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0 

 
class FINDER:

    @staticmethod
    def ENCRYPTION_PDF(character,file):
        i = 0
        index = 0
        char = character.replace("0 R","0 obj").lstrip().rstrip().encode()
        for line in file:
            try:
                if b"<< " in line:
                    line = line.split(b"<< ",1)[1]
            except Exception as e:
                continue
            if char in line:
                if b"\n" in line:
                    index = i + 1
                else:
                    index = i
            i = i + 1
        return index