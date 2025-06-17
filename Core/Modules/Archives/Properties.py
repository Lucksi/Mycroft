# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import zipfile
import tarfile
import datetime
import os
from Core.Utils import Colors
from Core.Modules import Hashes
from Core.Modules import Checksum
from Core.Utils import Formatting
from Core.Utils import Printer
from Core.Utils import Timestamp
from time import sleep
import shutil
import binascii

class OPERATIONS:

    @staticmethod
    def ZIP_GET_SIZE(list,archive):
        full_size = 0
        compr_size = 0
        compr_byte = 0
        for element in list:
            isdir = archive.getinfo(element).is_dir()
            if isdir == True:
                pass
            else:
                full_size = full_size + archive.getinfo(element).file_size
                compr_size = compr_size + archive.getinfo(element).compress_size
        compr_byte = full_size - compr_size
        return full_size, compr_size, compr_byte
    
    @staticmethod
    def TEMP_READER(chunk):
        f = open(chunk,"rb")
        content = f.read()
        f.close()
        return content

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
        zip_v_c =  archive_un.getinfo(list[0]).create_version
        zip_ex_v =  archive_un.getinfo(list[0]).extract_version
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
        compr_byte = str(OPERATIONS.ZIP_GET_SIZE(list,archive_un)[2])
        if vrb == 1:
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Listing Archive Properties...")
            Printer.GENERATE.Sentence(platform,"None","Creator-System: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(str(zip_v_c),"None","PKZIP-Creator-Version: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(str(zip_ex_v),"None","PKZIP-Extraction-Version: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(isencrypt_Z,"None","Password-Protected: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(full + " Bytes","None","Uncompressed-Size: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(compressed + " Bytes","None","Compressed-Size: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(compr_byte + " Bytes","None","Saved-Size: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(str(i),"None","Total-Files: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(str(f),"None","Files: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence(str(d),"None","Folders: ",out,output,1,"",vrb)
            if comment != "":
                Printer.GENERATE.Sentence(str(comment),"None","Comment: ",out,output,1,"",vrb)
            Printer.GENERATE.Sentence("","","LINE",out,output,1,"",vrb)
            print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Listing Archive Content...")
            sleep(5)
            i = 0
            d = 0
            for file in list:
                system = archive_un.getinfo(file).create_system
                zip_v_c =  archive_un.getinfo(file).create_version
                zip_ex_v =  archive_un.getinfo(file).extract_version
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
                known_alg = ["Store","Deflate","AES (Advance Encryption Standard)","bzip2","JPEG",
                             "LZMA","PPMD","XZ",
                             "Wavpack","Enhanched_Deflated"]
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
                    adl32 = Checksum.GET.ADLER32_Archive(archive_un.read(file))
                isdir = archive_un.getinfo(file).is_dir()
                if isdir == True:
                    d = d + 1
                    Printer.GENERATE.Sentence("n°" + str(d) + " Details: ","None","Folder: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(file,"None","Name: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(platform,"None","Creator-System: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(isencrypt,"None","Password-Protected: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(algorithm),"None","Compression-Type: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(Formatting.TEXT.FORMATTED_ZIP(date),"None","Date: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence("","LINE","",out,output,1,"",vrb)
                else:
                    code_CRC2 = str(archive_un.getinfo(file).CRC)
                    comment = str(archive_un.getinfo(file).comment).replace("b","").replace("'","").lstrip()
                    i = i +1
                    Printer.GENERATE.Sentence("n°" + str(i) + " Details: ","None","File: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(file,"None","Name: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(platform,"None","Creator-System: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(zip_v_c),"None","PKZIP-Creator-Version: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(zip_ex_v),"None","PKZIP-Extraction-Version: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(isencrypt,"None","Password-Protected: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(archive_un.getinfo(file).CRC),"None","Crc32-Checksum: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(f"{binascii.crc32(code_CRC2.encode()):08x}","None","Crc32-Controll-Code: ",out,output,1,"",vrb)
                    if isencrypt == "False":
                        Printer.GENERATE.Sentence(adl32,"None","Adler32-Checksum:: ",out,output,1,"",vrb)
                        Printer.GENERATE.Sentence(md5,"None","Md5-Hash: ",out,output,1,"",vrb)
                        Printer.GENERATE.Sentence(sha1,"None","Sha1-Hash: ",out,output,1,"",vrb)
                        Printer.GENERATE.Sentence(sha256,"None","Sha256-Hash: ",out,output,1,"",vrb)
                        Printer.GENERATE.Sentence(sha384,"None","Sha384-Hash: ",out,output,1,"",vrb)
                        Printer.GENERATE.Sentence(sha512,"None","Sha512-Hash: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(isencrypt,"None","Password-Protected: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(algorithm),"None","Compression-Type: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(archive_un.getinfo(file).file_size) + " Bytes","None","Size: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(archive_un.getinfo(file).compress_size) + " Bytes","None","Compressed-Size: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence(str(archive_un.getinfo(file).file_size- archive_un.getinfo(file).compress_size) + " Bytes","None","Saved-Size: ",out,output,1,"",vrb)
                    if comment != "":
                        Printer.GENERATE.Sentence(str(archive_un.getinfo(file).comment,"None","Date: ",out,output,1,"",vrb))
                    Printer.GENERATE.Sentence(Formatting.TEXT.FORMATTED_ZIP(date),"None","Date: ",out,output,1,"",vrb)
                    Printer.GENERATE.Sentence("","","LINE",out,output,1,"",vrb)
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
    
    @staticmethod
    def TAR_FILE(archive,output,extr,out,vrb,read):
        archive_un = tarfile.open(archive,'r:{}'.format(read)) 
        d = 0
        f1 = 0
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Listing Archive Content...")
        sleep(5)
        for tarinfo in archive_un:
            l = tarinfo.name       
            f = tarinfo.pax_headers
            m = tarinfo.chksum
            g = tarinfo.size
            t = Timestamp.GET.Date(tarinfo.mtime)
            a = tarinfo.mode
            n = tarinfo.uname
            c = tarinfo.gname
            is_dir = tarinfo.isdir()
            if is_dir == True:
                d = d + 1
                Printer.GENERATE.Sentence("n°" + str(d) + " Details: ","None","Directory: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(l,"None","Name: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(n,"None","User-Name: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c,"None","Group-Name: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(m),"None","Checksum: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(a),"None","Permission: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(t),"None","Date: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(g) + " Bytes","None","Size: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence("","","LINE",out,output,1,"",vrb)
            elif is_dir == False:
                f1 = f1 + 1
                archive_un.extract(member = l, path = ".Temp")
                ou = ".Temp/" + l
                temp_read = OPERATIONS.TEMP_READER(ou)
                md5 = Hashes.GET_HASHES.Hashing_zip(temp_read,"Md5")
                sha1 = Hashes.GET_HASHES.Hashing_zip(temp_read,"Sha1")
                sha256 = Hashes.GET_HASHES.Hashing_zip(temp_read,"Sha256")
                sha384 = Hashes.GET_HASHES.Hashing_zip(temp_read,"Sha384")
                sha512 = Hashes.GET_HASHES.Hashing_zip(temp_read,"Sha512")
                crc32 = Checksum.GET.CRC32_Archive(temp_read)[0]
                crc32_c = Checksum.GET.CRC32_Archive(temp_read)[1]
                adl32 = Checksum.GET.ADLER32_Archive(temp_read)
                Printer.GENERATE.Sentence("n°" + str(f1) + " Details: ","None","File: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(l,"None","Name: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(md5,"None","Md5-Hash: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(sha1,"None","Sha1-Hash: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(sha256,"None","Sha256-Hash: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(sha384,"None","Sha384-Hash: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(sha512,"None","Sha512-Hash: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(crc32,"None","Crc32-Checksum: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(crc32_c,"None","Crc32-Control-Code: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(adl32,"None","Adler32-Checksum: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(n,"None","User-Name: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(c,"None","Group-Name: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(m),"None","Checksum: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(a),"None","Permission: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(t),"None","Date: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence(str(g) + " Bytes","None","Size: ",out,output,1,"",vrb)
                Printer.GENERATE.Sentence("","","LINE",out,output,1,"",vrb)
        shutil.rmtree(".Temp")
        os.mkdir(".Temp")
        if extr == 1:
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Extracting Tar File...")
            sleep(4)
            output = output.replace("Metadata.txt","") + "Tar_Extracted"
            os.mkdir(output)
            try:
                archive_un.extractall(path=output)
                print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Tar File extracted successfully on: {}".format(Colors.Color.GREEN + output))
            except Exception as e:
                print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Something went wrong..Error: {}".format(str(e)))