# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class GET:

    class COMMON:
         
        @staticmethod
        def Pixel_ratio(width,height):
            p1 = height/width
            return str(round(p1,2))+":1"
        
        @staticmethod
        def Megapixel(width,height):
            megapixel = width * height / 1000000
            return round(megapixel,3)
        
        @staticmethod
        def Binary(n):
            g2 = int(n)+(1 << 32)
            binary = "{:032b}".format(g2)
            return binary
        
    class BMP:
        
        @staticmethod
        def Compression(fm):
            ctype = "None"
            fm = str(fm)
            if fm == "0":
                ctype = "No-Compression"
            elif fm == "1":
                ctype = "8bit RLE-Encoding"
            elif fm == "2":
                ctype = "4bit RLE-Encoding"
            return ctype
        
        @staticmethod
        def Color_Numbers(cr):
            cr2 = int(cr)
            c_number = pow(2,cr2)
            c_number = round(c_number,3)
            return str(c_number)
        
        @staticmethod
        def Color_Imp(fm):
            imp = "None"
            fm = str(fm)
            if fm == "0":
                imp = "All"
            else:
                imp = fm
            return imp

    class PNG:

        @staticmethod
        def Color_Scale(cm):
            ctype = "None"
            cm = str(cm)
            if cm == "0":
                ctype = "Grayscale"
            elif cm == "2":
                ctype = "RGB"
            elif cm == "3":
                ctype = "Palette Index"
            elif cm == "4":
                ctype = "Grayscale with Alpha"
            elif cm == "6":
                ctype = "RGB with Alpha"
            else:
                ctype = "None"
            return ctype
        
        @staticmethod
        def Compression(fm):
            ctype = "None"
            fm = str(fm)
            if fm == "0":
                ctype = "Deflate-Inflate"
            else:
                ctype = "None"
            return ctype
        
        @staticmethod
        def Filter(fm):
            ctype = "None"
            fm = str(fm)
            if fm == "0":
                ctype = "Adaptive"
            elif fm == "1":
                ctype = "Sub"
            elif fm == "2":
                ctype = "Up"
            elif fm == "3":
                ctype = "Average"
            elif fm == "4":
                ctype = "Paeth"
            else:
                ctype = "None"
            return ctype
        
        @staticmethod
        def Interlace(fm):
            ctype = "None"
            fm = str(fm)
            if fm == "0":
                ctype = "Not Interlaced"
            elif fm == "1":
                ctype = "Adam7 Interlace"
            else:
                ctype = "None"
            return ctype
        
    class GIF:

        @staticmethod
        def Duration(dl_li):
            tl = len(dl_li)
            if tl < 10:
                f_tm = tl
            else:
                f_tm = tl /10
            if len(str(f_tm)) == 3:
                f_tm = str(f_tm) + "0"
            else:
                f_tm = round(f_tm,3)
            return f_tm

        @staticmethod
        def Color_Numbers(cr):
            cr2 = int(cr)
            c_number = pow(2,int(cr2 + 1))
            b_number = 3*pow(2,int(cr2 + 1))
            return str(c_number),str(b_number)
 
        @staticmethod
        def Animation(fm):
            animation = "None"
            fm = str(fm)
            if fm == "0":
                animation = "Infinite"
            else:
                animation = fm
            return animation
        
        @staticmethod
        def Details(fm):
            c_flag = "None"
            binary = GET.COMMON.Binary(fm)
            if binary[-8] != "0":
                c_flag = "True"
            else:
                c_flag = "False"
            if c_flag == "True":
                f1 = binary[-7]
                f2 = binary[-6]
                f3 = binary[-5]
                cm = f1 + f2 + f3
                cm3 = int(cm,2)
                cm4 = cm3 + 1
            if binary[-4] == "0":
                imp = "Decreased importance"
            else:
                imp = "Increased importance"    
            return c_flag,str(cm3),imp,str(cm4)           
    
    class JPEG:

        @staticmethod
        def Density(nm):
            f_n = "None"
            if nm == 0:
                f_n = "No unit"
            elif nm == 1:
                f_n = "Inches"
            elif nm == 2:
                f_n = "Centimeters"
            return f_n
        
        @staticmethod
        def Components_S(b1):
            cm1 = "None"
            cm2 = 0
            if b1 == 1:
                cm1 = "Grey Scaled"
            elif b1 == 3:
                cm1 = "YCbCr"
            elif b1 == 4:
                cm1 = "CMYK"
            cm2 = pow(2, int(b1))
            return cm1,str(cm2)
        
        @staticmethod
        def Huff_Table_T(b1):
            table = "None"
            value = GET.COMMON.Binary(b1)
            if value[-4] == "0":
                table = "DCT-Table"
            elif value[-4] == "1":
                table = "AC-Table"
            return table