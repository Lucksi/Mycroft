# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class FILE:

    @staticmethod
    def MIC_Format(file_list,extension,extr,myFile,out3,images_s,type_images,out2,media_s,type_media):
        for element in file_list:
            if extension == "doc" or extension == "docx":
                check_string = "word/media/image"
                check_string2 = "word/media/media"
                check_fol = "word/media/"
            else:
                check_string = "ppt/media/image"
                check_string2 = "ppt/media/media"
                check_fol = "ppt/media/"
            if check_string in element:
                if extr == 1:
                    ls = myFile.read(element)
                    file_im = out3 + "/" +  element.replace(check_fol,"")
                    f = open(file_im,"wb")
                    f.write(ls)
                    f.close()
                images_s.append(element)
                type_images.append("Image")
            elif check_string2 in element:
                if extr == 1:
                    ls = myFile.read(element)
                    file_im = out2 + "/" +  element.replace(check_fol,"")
                    f = open(file_im,"wb")
                    f.write(ls)
                    f.close()
                media_s.append(element)
                type_media.append("Media")
            else:
                pass
    
    @staticmethod
    def LIB_Format(document3,extr,myFile,out3,images_s,type_images,out2,media_s,type_media):
        for elements in document3:
            element = elements.get("{urn:oasis:names:tc:opendocument:xmlns:manifest:1.0}full-path")
            type = elements.get("{urn:oasis:names:tc:opendocument:xmlns:manifest:1.0}media-type")
            if "image" in type:
                if extr == 1:
                    ls = myFile.read(element)
                    file_im = out3 + "/" +  element.replace("Pictures/","").replace("Thumbnails/","")
                    f = open(file_im,"wb")
                    f.write(ls)
                    f.close()
                images_s.append(element)
                type_images.append(type)
            elif "Media" in element:
                if extr == 1:
                    ls = myFile.read(element)
                    file_im = out2 + "/" +  element.replace("Media/","")
                    f = open(file_im,"wb")
                    f.write(ls)
                    f.close()
                media_s.append(element)
                type_media.append(type)