# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Write_File
from time import sleep
import binascii
import zlib

class GET:

    @staticmethod
    def CRC32_Archive(content):
        crc = zlib.crc32(content)
        crc_code = f"{binascii.crc32(str(crc).encode()):08x}"
        return str(crc),str(crc_code)

    @staticmethod
    def ADLER32_Archive(content):
        adl = zlib.adler32(content)
        return str(adl)

    @staticmethod
    def CRC32(file):
        f = open(file,"rb")
        content = f.read()
        f.close()
        crc = zlib.crc32(content)
        crc_code = f"{binascii.crc32(str(crc).encode()):08x}"
        return str(crc),str(crc_code)

    @staticmethod
    def ADLER32(file):
        f = open(file,"rb")
        content = f.read()
        f.close()
        adl = zlib.adler32(content)
        return str(adl)
    
    @staticmethod
    def CHECKSUM(file,vrb,out,output):
        print(Colors.Color.BLUE + "\n[I]" +Colors.Color.WHITE + "Get different Checksum")
        sleep(2)
        crc32 = GET.CRC32(file)[0]
        crc32_c = GET.CRC32(file)[1]
        adl32 = GET.ADLER32(file)
        if out == 1:
            f = open(output,"a")
            f.write("\nGet different Checksum:\n\n")
            Write_File.OUTPUT.LINE(crc32,f,"Crc32-Checksum: ")
            Write_File.OUTPUT.LINE(crc32_c,f,"Crc32-Control-Code: ")
            Write_File.OUTPUT.LINE(adl32,f,"Adler32-Checksum: ")
            f.write("-----------------------------------------------------------------------------------------------------------------------------------------------------")
            f.close()
        if vrb == 1:
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Crc32-Checksum: {}".format(Colors.Color.GREEN + crc32))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Crc32-Control-Code: {}".format(Colors.Color.GREEN + crc32_c))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Adler32-Checksum: {}".format(Colors.Color.GREEN + adl32))
        else:
            print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")