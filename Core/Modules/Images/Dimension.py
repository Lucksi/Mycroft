# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import struct

class IMAGE:

    @staticmethod
    def Megapixel(width,height):
        megapixel = width * height / 1000000
        return round(megapixel,3)
    
    @staticmethod
    def Size(extension,origfile):
        byte_order = "None"
        width = 0
        height = 0
        megapixel = 0
        img = open(origfile,"rb")
        reader = img.read()
        img.close()
        if extension == "png":
            img = open(origfile,"rb")
            reader = img.read()
            if b"IHDR" in reader:
                width, height = struct.unpack(">LL", reader[16:24])
            else:
                width, height = struct.unpack(">LL", reader[8:16])
            byte_order = "Big-Endian"
        elif extension == "jpeg" or extension == "jpg":
            img = open(origfile,"rb")
            reader = img.read(2)
            pointer = img.read(1)
            while pointer and ord(pointer) != 0xDA:
                while ord(pointer) != 0xFF:
                    pointer = img.read(1)
                while ord(pointer) == 0xFF:
                    pointer = img.read(1)
                if ord(pointer) >= 0xC0 and ord(pointer) <= 0xC3:
                    img.read(3)
                    height, width = struct.unpack(">HH", img.read(4))
                    break
                else:
                    img.read(
                        int(struct.unpack(">H", img.read(2))[0]) - 2)
                    pointer = img.read(1)
            byte_order = "Big-Endian"
        elif extension == "gif":
            img = open(origfile,"rb")
            reader = img.read()
            if b'GIF87a' in reader or b'GIF89a' in reader:
                width, height = struct.unpack("<HH", reader[6:10])
                byte_order = "Little-Endian"
        width = int(width)
        height = int(height)
        megapixel = IMAGE.Megapixel(width,height)
        return width,height,byte_order,round(megapixel,3)