# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class GET_PERMISSIONS:

    class PDF:
        
        @staticmethod
        def GET(byte_string,revflag,permissions_l):
            permsissions_byt = int(byte_string)+(1 << 32)
            byte_permission = "{:032b}".format(permsissions_byt)
            flag = int(revflag)
            if byte_permission[-3] == "1":
                if flag == 2:
                    permissions_l.append("Print")
                else:
                    if byte_permission[-12] == "1":
                        permissions_l.append("Print")
                        permissions_l.append("Print High Res")
                    else:
                        permissions_l.append("Print Low Res")
            if byte_permission[-4] == "1":
                permissions_l.append("Modify")
            if byte_permission[-5] == "1":
                if flag == 2:
                    permissions_l.append("Copy")
                    permissions_l.append("Extract")
                elif flag >= 3:
                    permissions_l.append("Copy")
                    permissions_l.append("Extract")
            if byte_permission[-6] == "1":
                permissions_l.append("Fill Forms")
                permissions_l.append("Annotations")
            if flag >=3:
                if byte_permission[-9] == "1":
                    permissions_l.append("Fill Existing Forms")
                if byte_permission[-10] == "1":
                    permissions_l.append("Extract Text/Graphic")
                if byte_permission[-11] == "1":
                    permissions_l.append("Insert")
                    permissions_l.append("Rotate")
                    permissions_l.append("Create Bookmarks")
                    permissions_l.append("Delete")