# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Write_File
from time import sleep
import hashlib

class GET_HASHES:

    @staticmethod
    def Hashing_zip(file,algorithm):
        if algorithm == "Md5":
            hashed_string = hashlib.md5(file)
        elif algorithm == "Sha1":
            hashed_string = hashlib.sha1(file)
        elif algorithm == "Sha256":
            hashed_string = hashlib.sha256(file)
        elif algorithm == "Sha384":
            hashed_string = hashlib.sha384(file)
        elif algorithm == "Sha512":
            hashed_string = hashlib.sha512(file)
        return hashed_string.hexdigest()

    @staticmethod
    def Hashing(file,algorithm):
        with open(file,'rb') as f:
            if algorithm == "Md5":
                hashed_string = hashlib.md5()
            elif algorithm == "Sha1":
                hashed_string = hashlib.sha1()
            elif algorithm == "Sha256":
                hashed_string = hashlib.sha256()
            elif algorithm == "Sha384":
                hashed_string = hashlib.sha384()
            elif algorithm == "Sha512":
                hashed_string = hashlib.sha512()
            while raw := f.read(8192) :
                hashed_string.update(raw)
        return hashed_string.hexdigest()
    
    @staticmethod
    def Converter(file,vrb,out,output):
        print(Colors.Color.BLUE + "\n[I]" +Colors.Color.WHITE + "Get different Hashes:")
        sleep(2)
        md5 = GET_HASHES.Hashing(file,"Md5")
        sha1 = GET_HASHES.Hashing(file,"Sha1")
        sha256 = GET_HASHES.Hashing(file,"Sha256")
        sha384 = GET_HASHES.Hashing(file,"Sha384")
        sha512 = GET_HASHES.Hashing(file,"Sha512")
        if out == 1:
            f = open(output,"a")
            f.write("\nGet different Hashes:\n\n")
            Write_File.OUTPUT.LINE(md5,f,"Md5-Hash: ")
            Write_File.OUTPUT.LINE(sha1,f,"Sha1-Hash: ")
            Write_File.OUTPUT.LINE(sha256,f,"Sha256-Hash: ")
            Write_File.OUTPUT.LINE(sha384,f,"Sha384-Hash: ")
            Write_File.OUTPUT.LINE(sha512,f,"Sha512-Hash: ")
            f.write("-----------------------------------------------------------------------------------------------------------------------------------------------------")
            f.close()
        if vrb == 1:
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Md5-Hash: {}".format(Colors.Color.GREEN + md5))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha1-Hash: {}".format(Colors.Color.GREEN + sha1))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha256-Hash: {}".format(Colors.Color.GREEN + sha256))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha384-Hash: {}".format(Colors.Color.GREEN + sha384))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha512-Hash: {}".format(Colors.Color.GREEN + sha512))
        else:
            print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Process completed")