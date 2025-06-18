# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from time import sleep
import xml.dom.minidom
import xml.etree.ElementTree

class GET:

    @staticmethod
    def M_OFFICE_COMMENTS(file_list,extension,comments,comment_id,created_d,comment_auth_id,num_id,user_t_id,name_l,initials):
        list = file_list.namelist()
        check_string2 = "authors.xml"
        if  extension == "xlsx" or extension == "xlsm":
            for element in list:
                if "xl/threadedComments" in element:
                    t_pass = "True"
                    break
                elif "xl/comments1.xml" in element:
                    t_pass = "False"
        for element in list:
            if extension == "doc" or extension == "docx" or extension == "dotx" or extension == "docm":
                check_string = "word/comments.xml"
                check_strin2 = "word/comments.xml"
                tags = ["w:t"]
            elif extension == "pptx" or extension == "potx":
                check_string = "ppt/comments"
                check_strin2 = "ppt/comments"
                tags = ["a:t"]
            elif extension == "xlsx" or extension == "xlsm":
                check_strin2 = "xl/comments1.xml"
                check_string = "xl/threadedComments"
                tags = ["text","t"]
            if check_string in element or check_strin2 in element:
                document4 = xml.dom.minidom.parseString(file_list.read(element))
                document5 = xml.etree.ElementTree.fromstring(file_list.read(element))
                if extension == "xlsx" or extension == "xlsm":
                    if t_pass == "True":
                        string = document4.getElementsByTagName(tags[0])
                        try:
                            for text in string:
                                content = text.childNodes[0].data
                                if "Reply to" not in content:
                                    comments.append(content)
                        except Exception as e:
                            continue
                    else:
                        string = document4.getElementsByTagName(tags[1])
                        try:
                            for text in string:
                                content = text.childNodes[0].data
                                if "Reply to" not in content:
                                    comments.append(content)
                        except Exception as e:
                            continue
                else:
                    for tag in tags:
                        string = document4.getElementsByTagName(tag)
                        try:
                            for text in string:
                                content = text.childNodes[0].data
                                if "Reply to" not in content:
                                    comments.append(content)
                        except Exception as e:
                            continue

                if extension == "pptx" or extension == "potx":
                    for element in document5:
                        try:
                            id = element.get("id").replace("{","").replace("}","")
                            authorid = element.get("authorId").replace("{","").replace("}","")
                            creation = element.get("created")
                            comment_id.append(id)
                            created_d.append(creation)
                            comment_auth_id.append(authorid)
                        except Exception as e:
                            continue
                elif extension == "docx" or extension == "dotx" or extension == "docm":
                    for element in document5:
                        try:
                            id = element.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id")
                            authorid = element.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}author")
                            creation = element.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}date")
                            init = element.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}initials")
                            comment_id.append(id)
                            created_d.append(creation)
                            comment_auth_id.append(authorid)
                            initials.append(init)
                        except Exception as e:
                            continue
                elif extension == "xlsx" or extension == "xlsm":
                    for element in document5:
                        try:
                            id = element.get("id").replace("{","").replace("}","")
                            authorid = element.get("personId").replace("{","").replace("}","")
                            creation = element.get("dT")
                            comment_id.append(id)
                            created_d.append(creation)
                            comment_auth_id.append(authorid)
                        except Exception as e:
                            continue
            if check_string2 in element:
                document5 = xml.etree.ElementTree.fromstring(file_list.read(element))
                for element in document5:
                    id = element.get("id").replace("{","").replace("}","")
                    name = element.get("name")
                    userid = element.get("userId")
                    init = element.get("initials")
                    num_id.append(id)
                    user_t_id.append(userid)
                    name_l.append(name)
                    initials.append(init) 
            else:
                pass
        
    @staticmethod
    def LIB_OFFICE_COMMENTS(file_list,extension,comments,comment_id,created_d,comment_auth_id,num_id,user_t_id,name_l,initials):
        check_string = "content.xml"
        document4 = xml.dom.minidom.parseString(file_list.read(check_string))
        if extension == "odp":
            annot =  document4.getElementsByTagName("officeooo:annotation")
        else:
            annot =  document4.getElementsByTagName("office:annotation")
        for t in annot:
            string = t.getElementsByTagName("dc:creator")
            string_1 = t.getElementsByTagName("dc:date")
            string_2 = t.getElementsByTagName("meta:creator-initials")
            tags = ["text:p","text:span"]
            for tag in tags:
                string4 = t.getElementsByTagName(tag)
                try:
                    for text in string:
                        authorid = text.childNodes[0].data
                        comment_auth_id.append(authorid)
                    for text in string_1:
                        creation = text.childNodes[0].data
                        created_d.append(creation)
                    for text in string_2:
                        init = text.childNodes[0].data
                        initials.append(init)
                    for text in string4:
                        try:
                            content = text.childNodes[0].data
                            if "Reply to" not in content:
                                comments.append(content)
                        except Exception as e:
                            pass
                except Exception as e:
                    print(str(e))
                
    @staticmethod
    def DOC_TEXT(index,output):
        f = open(output,"a")
        s_string = 0
        for element in index:
            try:
                content = element.childNodes[0].data
                f.write(str(content))
                if "." in str(content):
                    f.write("\n\n")
                s_string = s_string + 1
            except Exception as e:
               pass
        if s_string > 0:
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        f.close()
    
    @staticmethod
    def DOC_LINKS(index,output,vrb):
        f = open(output,"a")
        s_string = 0
        for element in index:
            try:
                typology = element.get("Type")
                content = element.get("Target")
                if typology == "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink":
                    if content != "":
                        if vrb == 1:
                            print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + str(content))
                        f.write(str(content))
                        f.write("\n\n")
                        s_string = s_string + 1
            except Exception as e:
                print(str(e))
        if s_string > 0:
            print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        f.close()

    @staticmethod
    def ODT_TEXT(index,output):
        f = open(output,"a")
        s_string = 0
        for element in index:
            try:
                content = element.childNodes[0].data
                f.write(str(content))
                if "." in str(content):
                    f.write("\n\n")
                else:
                    f.write(" ")
                s_string = s_string + 1
            except Exception as e:
                pass
        if s_string > 0:
            print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
        f.close()
    
    @staticmethod
    def ODT_LINKS(index,output,vrb):
        f = open(output,"a")
        s_string = 0
        for element in index:
            try:
                content = element.getAttribute("xlink:href")
                if vrb == 1:
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + str(content))
                f.write(str(content))
                f.write("\n\n")
                s_string = s_string + 1
            except Exception as e:
                pass
        if s_string > 0:
            print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        f.close()
    
    @staticmethod
    def PPTX_TEXT(index,output):
        s_string = 0
        list = index.namelist()
        f = open(output,"w")
        f.write("Getting-Slides")
        for element in list:
            if "ppt/slides/slide" in element:
                print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Slide found: {}".format(Colors.Color.GREEN + element.replace("ppt/slides/","")))
                sleep(3)
                f = open(output,"a")
                f.write("\n\n" + element.replace("ppt/slides/","") + "\n\n")
                document4 = xml.dom.minidom.parseString(index.read(element))
                string = document4.getElementsByTagName("a:t")
                try:
                    for text in string:
                        content = text.childNodes[0].data
                        f.write(str(content))
                        if "." in str(content):
                            f.write("\n\n")
                        s_string = s_string + 1
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Content Stored Successfully")
                except Exception as e:
                    print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "Something Went Wrong: " + Colors.Color.GREEN + str(e) + "\n")
                if s_string > 0:
                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
                else:
                    print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Total Strings saved: " + Colors.Color.GREEN + str(s_string))
            else:
                pass
        f.close()
    
    @staticmethod
    def PPTX_LINKS(index,output,vrb):
        s_string = 0
        list = index.namelist()
        f = open(output,"w")
        f.write("Getting-Slides")
        for element in list:
            if "ppt/slides/_rels" in element:
                f = open(output,"a")
                document4 = xml.etree.ElementTree.fromstring(index.read(element))
                for element in document4:
                    try:
                        typology = element.get("Type")
                        content = element.get("Target")
                        if typology == "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink":
                            if content != "":
                                if vrb == 1:
                                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + str(content))
                                f.write(str(content))
                                f.write("\n\n")
                                s_string = s_string + 1
                    except Exception as e:
                        print(str(e))
        if s_string > 0:
            print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        f.close()
    
    @staticmethod
    def XLSX_LINKS(index,output,vrb):
        s_string = 0
        list = index.namelist()
        f = open(output,"w")
        f.write("Getting-Slides")
        for element in list:
            if "xl/worksheets/_rels" in element:
                f = open(output,"a")
                document4 = xml.etree.ElementTree.fromstring(index.read(element))
                for element in document4:
                    try:
                        typology = element.get("Type")
                        content = element.get("Target")
                        if typology == "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink":
                            if content != "":
                                if vrb == 1:
                                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + str(content))
                                f.write(str(content))
                                f.write("\n\n")
                                s_string = s_string + 1
                    except Exception as e:
                        print(str(e))
        if s_string > 0:
            print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Total Links saved: " + Colors.Color.GREEN + str(s_string))
        f.close()
