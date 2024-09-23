# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import zipfile
import datetime
import os
from Core.Utils import Colors
from Core.Modules import Hashes
from Core.Utils import Formatting
from Core.Utils import Write_File
from time import sleep
import binascii

class OPERATIONS:

    @staticmethod
    def ZIP_GET_SIZE(list,archive):
        full_size = 0
        compr_size = 0
        for element in list:
            isdir = archive.getinfo(element).is_dir()
            if isdir == True:
                pass
            else:
                full_size = full_size + archive.getinfo(element).file_size
                compr_size = compr_size + archive.getinfo(element).compress_size
        return full_size, compr_size

class GET:

    @staticmethod
    def ZIP_FILE(archive,output,extr,out,vrb):
        archive_un = zipfile.ZipFile(archive,'r')
        list = archive_un.namelist()
        try:
            test = archive_un.testzip()
            isencrypt_Z = "False"
        except RuntimeError as e:
            isencrypt_Z = "True"
        i = 0
        f = 0
        d = 0
        system_0 = archive_un.getinfo(list[0]).create_system
        if system_0 == 0:
            platform = "Windows"
        elif system_0 == 3:
            platform = "Unix"
        else:
            platform = "Unknown"
        for file in list:
            isdir = archive_un.getinfo(file).is_dir()
            if isdir == True:
                d = d + 1
            else:
                f = f + 1
            i = i +1
        comment = str(archive_un.comment).replace("b","").replace("'","").lstrip()
        full = str(OPERATIONS.ZIP_GET_SIZE(list,archive_un)[0])
        compressed = str(OPERATIONS.ZIP_GET_SIZE(list,archive_un)[1])
        if out == 1:
            f2 = open(output,"a")
            f2.write("Listing Archive Properties...\n\n")
            Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(platform),f2,"Creator-System: ")
            Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(isencrypt_Z),f2,"Password-Protected: ")
            Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(full),f2,"Uncompressed-Size: ")
            Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(compressed),f2,"Compressed-Size: ")
            Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(str(i)),f2,"Total-Files: ")
            Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(str(d)),f2,"Folders: ")
            Write_File.OUTPUT.LINE(Formatting.TEXT.FORMATTED(str(f)),f2,"Files: ")
            f2.close()
        if vrb == 1:
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Listing Archive Properties...")
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Creator-System: {}".format(Colors.Color.GREEN + platform + Colors.Color.WHITE))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Password-Protected: {}".format(Colors.Color.GREEN + isencrypt_Z))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Uncompressed-Size: {} Bytes".format(Colors.Color.GREEN + full))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Compressed-Size : {} Bytes".format(Colors.Color.GREEN + compressed))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Total-Files: {}".format(Colors.Color.GREEN + str(i)))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Folders: {}".format(Colors.Color.GREEN + str(d)))
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Files: {}".format(Colors.Color.GREEN + str(f)))
            if comment != "":
                print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Comment: {}".format(Colors.Color.GREEN + str(comment)))
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Listing Archive Content...")
            sleep(5)
            i = 0
            d = 0
            for file in list:
                system = archive_un.getinfo(file).create_system
                date = str(datetime.datetime(* archive_un.getinfo(file).date_time))
                if system == 0:
                    platform = "Windows"
                elif system == 3:
                    platform = "Unix"
                else:
                    platform = "Unknown"
                encrypt = archive_un.getinfo(file).flag_bits & 0x1
                if encrypt:
                    isencrypt = "True"
                else:
                    isencrypt = "False"
                known_alg = ["Store","Deflate","AES (Advance Encryption Standard)","bzip2","JPEG","LZMA","PPMD","XZ","Wavpack","Enhanched_Deflated"]
                if archive_un.getinfo(file).compress_type == 0:
                    algorithm = known_alg[0]
                elif archive_un.getinfo(file).compress_type == 8:
                    algorithm = known_alg[1]
                elif archive_un.getinfo(file).compress_type == 9:
                    algorithm = known_alg[9]
                elif archive_un.getinfo(file).compress_type == 12:
                    algorithm = known_alg[3]
                elif archive_un.getinfo(file).compress_type == 14:
                    algorithm = known_alg[5]
                elif archive_un.getinfo(file).compress_type == 95:
                    algorithm = known_alg[8]
                elif archive_un.getinfo(file).compress_type == 96:
                    algorithm = known_alg[4]
                elif archive_un.getinfo(file).compress_type == 97:
                    algorithm = known_alg[7]
                elif archive_un.getinfo(file).compress_type == 98:
                    algorithm = known_alg[6]
                elif archive_un.getinfo(file).compress_type == 99:
                    algorithm = known_alg[2]
                else:
                    algorithm = archive_un.getinfo(file).compress_type
                if isencrypt == "False":
                    md5 = Hashes.GET_HASHES.Hashing_zip(archive_un.read(file),"Md5")
                    sha1 = Hashes.GET_HASHES.Hashing_zip(archive_un.read(file),"Sha1")
                    sha256 = Hashes.GET_HASHES.Hashing_zip(archive_un.read(file),"Sha256")
                    sha384 = Hashes.GET_HASHES.Hashing_zip(archive_un.read(file),"Sha384")
                    sha512 = Hashes.GET_HASHES.Hashing_zip(archive_un.read(file),"Sha512")
                isdir = archive_un.getinfo(file).is_dir()
                if isdir == True:
                    d = d + 1
                    print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Folder n°{} Details:".format(str(d)))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Name: {}".format(Colors.Color.GREEN + file + Colors.Color.WHITE))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Creator-System: {}".format(Colors.Color.GREEN + platform + Colors.Color.WHITE))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Password-Protected: {}".format(Colors.Color.GREEN + isencrypt))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Compression-Type: {}".format(Colors.Color.GREEN + str(algorithm)))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Date: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED_ZIP(date)))
                else:
                    code_CRC2 = str(archive_un.getinfo(file).CRC)
                    comment = str(archive_un.getinfo(file).comment).replace("b","").replace("'","").lstrip()
                    i = i +1
                    print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "File n°{} Details:".format(str(i)))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Name: {}".format(Colors.Color.GREEN + file + Colors.Color.WHITE))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Creator-System: {}".format(Colors.Color.GREEN + platform + Colors.Color.WHITE))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Crc32-Checksum: {}".format(Colors.Color.GREEN + str(archive_un.getinfo(file).CRC)))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Crc32-Controll-Code: {}".format(Colors.Color.GREEN + f"{binascii.crc32(code_CRC2.encode()):08x}"))
                    if isencrypt == "False":
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Md5-Hash: {}".format(Colors.Color.GREEN + md5))
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha1-Hash: {}".format(Colors.Color.GREEN + sha1))
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha256-Hash: {}".format(Colors.Color.GREEN + sha256))
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha384-Hash: {}".format(Colors.Color.GREEN + sha384))
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Sha512-Hash: {}".format(Colors.Color.GREEN + sha512))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Password-Protected: {}".format(Colors.Color.GREEN + isencrypt))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Compression-Type: {}".format(Colors.Color.GREEN + str(algorithm)))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Size: {} Bytes".format(Colors.Color.GREEN + str(archive_un.getinfo(file).file_size)))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Compressed-Size: {} Bytes".format(Colors.Color.GREEN + str(archive_un.getinfo(file).compress_size)))
                    if comment != "":
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Comment: {}".format(Colors.Color.GREEN + str(archive_un.getinfo(file).comment)))
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Date: {}".format(Colors.Color.GREEN + Formatting.TEXT.FORMATTED_ZIP(date)))  
        if extr == 1:
            if isencrypt_Z == "False":
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Zip File...")
                sleep(4)
                output = output.replace("Metadata.txt","") + "Zip_Extracted"
                os.mkdir(output)
                try:
                    archive_un.extractall(path=output)
                    print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Zip File extracted successfully on: {}".format(Colors.Color.GREEN + output))
                except Exception as e:
                    print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Something went wrong..Error: {}".format(str(e)))
            else:
                print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Zip File {} Protected with a password impossible to unzip".format(Colors.Color.GREEN + archive + Colors.Color.WHITE))
        archive_un.close()     