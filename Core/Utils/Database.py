# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import sqlite3
import os
from Core.Utils import Colors
from time import sleep

class DATABASE:

    db = "Database/.DB"

    @staticmethod
    def RESET():
        er = int(input(Colors.Color.BLUE + "\n[?]" + Colors.Color.WHITE + "Are You sure to reset the Database? All records will be lost(1)Yes(2)No\n\n" + Colors.Color.ORANGE + "[Mycroft]" + Colors.Color.WHITE + "-->"))
        if er == 1:
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Deleting Database Tables")
            sleep(2)
            try:
                os.remove(DATABASE.db)
                DATABASE.CREATE()
                print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Database resetted correctly")
            except Exception as e:
                print(str(e))
        elif er == 2:
            print("\nAborted operation")
        else:
            DATABASE.RESET()

    @staticmethod
    def SEARCH(parameter,advanced):
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Searching for: {}".format(Colors.Color.GREEN + parameter))
        sleep(2)
        connect = None
        try:
            connect = sqlite3.connect(DATABASE.db)
            if advanced == 0:
                sql = '''SELECT id,name,md5,sha1,sha256,sha384,sha512,time,mime,size,extension FROM DATA WHERE id = "{}" or name LIKE "%{}%" or md5="{}" or sha1="{}" or sha256="{}" or sha512 ="{}" or extension = "{}" or time LIKE "%{}%"'''.format(parameter,parameter,parameter,parameter,parameter,parameter,parameter,parameter)
            else:
                sql = parameter
            cur = connect.cursor()
            exist = cur.execute(sql).fetchall()
            if exist != []:
                times = str(len(exist))
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Record found for {}: {} Records".format(Colors.Color.GREEN + parameter + Colors.Color.WHITE,Colors.Color.GREEN + times + Colors.Color.WHITE))
                sleep(2)
                for element in exist:
                    print(Colors.Color.WHITE + "|")
                    print(Colors.Color.WHITE + "|_" + Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "File-Id: {}".format((Colors.Color.GREEN + str(element[0]))))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Name: {}".format((Colors.Color.GREEN + element[1])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Md5: {}".format((Colors.Color.GREEN + element[2])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha1: {}".format((Colors.Color.GREEN + element[3])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha256: {}".format((Colors.Color.GREEN + element[4])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha384: {}".format((Colors.Color.GREEN + element[5])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha512: {}".format((Colors.Color.GREEN + element[6])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Date: {}".format((Colors.Color.GREEN + element[7])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Mime: {}".format((Colors.Color.GREEN + element[8])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Size: {} Bytes".format((Colors.Color.GREEN + element[9] + Colors.Color.WHITE)))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Extension: {}".format((Colors.Color.GREEN + element[10] + Colors.Color.WHITE)))
            else:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Record not in Database")
        except sqlite3.Error as e:
            print(e)
        finally:
            if connect:
                connect.close()
    
    @staticmethod
    def ADV_SEARCH(parameter,advanced):
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Searching Results for Query: {}".format(Colors.Color.GREEN + parameter))
        sleep(2)
        connect = None
        try:
            connect = sqlite3.connect(DATABASE.db)
            if advanced == 0:
                sql = '''SELECT id,name,md5,sha1,sha256,sha384,sha512,time,mime,size,extension FROM DATA WHERE id = "{}" or name ="{}" or md5="{}" or sha1="{}" or sha256="{}" or sha512 ="{}" or extension = "{}"'''.format(parameter,parameter,parameter,parameter,parameter,parameter,parameter)
            else:
                
                sql = '''SELECT id,name,md5,sha1,sha256,sha384,sha512,time,mime,size,extension FROM DATA WHERE {}'''.format(parameter)
            cur = connect.cursor()
            exist = cur.execute(sql).fetchall()
            if exist != []:
                times = str(len(exist))
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Record found for {}: {} Records".format(Colors.Color.GREEN + parameter + Colors.Color.WHITE,Colors.Color.GREEN + times + Colors.Color.WHITE))
                sleep(2)
                for element in exist:
                    print(Colors.Color.WHITE + "|")
                    print(Colors.Color.WHITE + "|_" + Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "File-Id: {}".format((Colors.Color.GREEN + str(element[0]))))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Name: {}".format((Colors.Color.GREEN + element[1])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Md5: {}".format((Colors.Color.GREEN + element[2])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha1: {}".format((Colors.Color.GREEN + element[3])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha256: {}".format((Colors.Color.GREEN + element[4])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha384: {}".format((Colors.Color.GREEN + element[5])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha512: {}".format((Colors.Color.GREEN + element[6])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Date: {}".format((Colors.Color.GREEN + element[7])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Mime: {}".format((Colors.Color.GREEN + element[8])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Size: {} Bytes".format((Colors.Color.GREEN + element[9] + Colors.Color.WHITE)))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Extension: {}".format((Colors.Color.GREEN + element[10] + Colors.Color.WHITE)))
            else:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Record not in Database")
        except sqlite3.Error as e:
            print(e)
        finally:
            if connect:
                connect.close()

    @staticmethod
    def UPDATE(md5,sha1,sha256,sha384,sha512,time,size,name,mime,extension):
        connect = None
        try:
            connect = sqlite3.connect(DATABASE.db)
            sql = '''INSERT INTO DATA(name,md5,sha1,sha256,sha384,sha512,time,size,mime,extension) VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''.format(name,md5,sha1,sha256,sha384,sha512,time,size,mime,extension)
            cur = connect.cursor()
            cur.execute(sql)
            connect.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if connect:
                connect.close()
    
    @staticmethod
    def EXIST(md5,sha1,sha256,sha384,sha512,time,size,name,mime,extension):
        connect = None
        try:
            connect = sqlite3.connect(DATABASE.db)
            sql = '''SELECT id,name,md5,sha1,sha256,sha384,sha512,time,mime,size,extension FROM DATA where md5="{}"'''.format(md5)
            cur = connect.cursor()
            exist = cur.execute(sql).fetchall()
            if exist != []:
                times = str(len(exist))
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Record already found: {} Times".format(Colors.Color.GREEN + times + Colors.Color.WHITE))
                for element in exist:
                    print(Colors.Color.WHITE + "|")
                    print(Colors.Color.WHITE + "|_" + Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "File-Id: {}".format((Colors.Color.GREEN + str(element[0]))))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Name: {}".format((Colors.Color.GREEN + element[1])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Md5: {}".format((Colors.Color.GREEN + element[2])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha1: {}".format((Colors.Color.GREEN + element[3])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha256: {}".format((Colors.Color.GREEN + element[4])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha384: {}".format((Colors.Color.GREEN + element[5])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Sha512: {}".format((Colors.Color.GREEN + element[6])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Date: {}".format((Colors.Color.GREEN + element[7])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Mime: {}".format((Colors.Color.GREEN + element[8])))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Size: {} Bytes".format((Colors.Color.GREEN + element[9] + Colors.Color.WHITE)))
                    print(Colors.Color.WHITE + "|_" + Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "File-Extension: {}".format((Colors.Color.GREEN + element[10] + Colors.Color.WHITE)))
            else:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Record not in Database")
            DATABASE.UPDATE(md5,sha1,sha256,sha384,sha512,str(time),str(size),name,mime,extension)
        except sqlite3.Error as e:
            print(e)
        finally:
            if connect:
                connect.close()

    @staticmethod
    def CREATE():
        connect = None
        try:
            if os.path.exists(DATABASE.db):
                pass
            else:
                connect = sqlite3.connect(DATABASE.db)
                sql = '''CREATE TABLE DATA(id INTEGER PRIMARY KEY,name,md5,sha1,sha256,sha384,sha512,crc32,crc32_code,adler32,time,mime,size,extension)'''
                cur = connect.cursor()
                cur.execute(sql)
        except sqlite3.Error as e:
            print(e)
        finally:
            if connect:
                connect.close()