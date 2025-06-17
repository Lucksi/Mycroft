# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024-2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import struct
from Core.Modules.Images import Properties


class TYPE:

    class BMP:

        @staticmethod
        def Get_Parameters(origfile):
            comp = "None"
            c_num = "None"
            bc = "None"
            cp = "None"
            pI = "None"
            width = 0
            height = 0
            y = 0
            x = 0
            img = open(origfile,"rb")
            reader = img.read()
            headersize = struct.unpack("<I", reader[14:18])[0]
            if headersize == 12:
                w, h = struct.unpack("<HHB", reader[18:22])
                width = int(w)
                height = int(h)
            elif headersize >= 40:
                w,h,pl,bc,cp,x,n3,y,n4,n5 = struct.unpack_from("<iihihxxxxhhhhh", reader[18:50])
                width = int(w)
                height = abs(int(h))
            pI = Properties.GET.COMMON.Pixel_ratio(height,width)
            comp = Properties.GET.BMP.Compression(cp)
            c_num = Properties.GET.BMP.Color_Numbers(bc)
            imp = Properties.GET.BMP.Color_Imp(n5)
            byte_order = "Little-Endian"
            parameters = [width,height,str(pl),str(bc),comp,str(x),str(y),pI,c_num,byte_order,imp]
            return parameters
   
    class PNG:

        @staticmethod
        def Get_Parameters(origfile):
            cm2 = "None"
            fm2 = "None"
            em2 = "None"
            dm2 = "None"
            cb = "None"
            pI = "None"
            width = 0
            height = 0
            megapixel = 0
            img = open(origfile,"rb")
            reader = img.read()
            if b"IHDR" in reader:
                width, height, cb, cm, fm, em, dm = struct.unpack(">LLbbbbb", reader[16:29])
            else:
                width, height, cb, cm, fm, em, dm = struct.unpack(">LLbbbbb", reader[8:21])
            img.close()
            cm2 = Properties.GET.PNG.Color_Scale(cm)
            fm2 = Properties.GET.PNG.Compression(fm)
            em2 = Properties.GET.PNG.Filter(em)
            dm2 = Properties.GET.PNG.Interlace(dm)
            byte_order = "Big-Endian"
            width = int(width)
            height = int(height)
            pI = Properties.GET.COMMON.Pixel_ratio(height,width)
            megapixel = 0
            parameters = [width,height,byte_order,round(megapixel,3),cb,cm2,fm2,em2,dm2,pI]
            return parameters
    
    class JPEG:

        class MARKERS:
            
            @staticmethod
            def M_BYTES(origfile):
                order = "None"
                img = open(origfile,"rb")
                reader = img.readlines()
                for line in reader:
                    if b"Exif" in line:
                        if b"II" in line:
                            order = "Little-Endian (Intel, II)"
                        elif b"MM" in line:
                            order = "Big-Endian (Motorola, MM)"
                        break
                return order

            @staticmethod
            def S0F0(origfile):
                c_samp = "None"
                b_p = "None"
                c_num = "None"
                hm = "None"
                width = 0
                height = 0
                img = open(origfile,"rb")
                reader = img.read(2)
                pointer = img.read(1)
                try:
                    while pointer and ord(pointer) != 0xDA:
                        while ord(pointer) != 0xFF:
                            pointer = img.read(1)
                        while ord(pointer) == 0xFF:
                            pointer = img.read(1)
                        if ord(pointer) >= 0xC0 and ord(pointer) <= 0xC3:
                            img.read(3)
                            height,width,c_num,hf =  struct.unpack(">HHBxxxxB", img.read(10))
                            hm = Properties.GET.JPEG.Huff_Table_T(hf)
                            c_samp = Properties.GET.JPEG.Components_S(c_num)[0]
                            b_p = Properties.GET.JPEG.Components_S(c_num)[1]
                            break
                        else:
                            img.read(
                                int(struct.unpack(">H", img.read(2))[0]) - 2)
                            pointer = img.read(1)
                except Exception:
                    pass
                img.close()
                parameters = [height,width,c_num,hm,c_samp,b_p]
                return parameters
            
            @staticmethod
            def APP0(origfile):
                x = 0
                y = 0
                tw = 0
                th = 0
                dm = ""
                img2 = open(origfile,"rb")
                r = img2.read()
                img2.close()
                try:
                    met = TYPE.JPEG.MARKERS.M_BYTES(origfile)
                    if b"JFIF" in r and b"Exif" not in r and b"EXIF" not in r:
                        img = open(origfile,"rb")
                        reader = img.read(2)
                        pointer = img.read(1)
                        while pointer and ord(pointer) != 0xDA:
                            while ord(pointer) != 0xFF:
                                pointer = img.read(1)
                            while ord(pointer) == 0xFF:
                                pointer = img.read(1)
                            if ord(pointer) >= 0xe0 and ord(pointer) <= 0xe3:
                                img.read(2)
                                du,x,y,tw,th =  struct.unpack(">xxxxxxxBHHBB", img.read(14))
                                dm = Properties.GET.JPEG.Density(du)
                            else:
                                img.read(
                                    int(struct.unpack(">H", img.read(2))[0]) - 2)
                                pointer = img.read(1)
                        
                        img.close()
                    else:
                        x = "None"
                        y = "None"
                        tw = "None"
                        th = "None"
                        dm = "None"
                except Exception as e:
                    pass
                parameters = [x,y,tw,th,dm,met]
                return parameters

        @staticmethod
        def Get_Parameters(origfile):
            S0F0_parameters = TYPE.JPEG.MARKERS.S0F0(origfile)
            APP0_parameters = TYPE.JPEG.MARKERS.APP0(origfile)
            width = S0F0_parameters[1]
            height = S0F0_parameters[0]
            c_samp = S0F0_parameters[4]
            b_p = S0F0_parameters[5]
            c_num = S0F0_parameters[2]
            hm = S0F0_parameters[3]
            x = APP0_parameters[0]
            y = APP0_parameters[1]
            tw = APP0_parameters[2]
            th = APP0_parameters[3]
            dm = APP0_parameters[4]
            meta = APP0_parameters[5]
            megapixel = 0
            byte_order = "Big-Endian"
            try:
                pI = Properties.GET.COMMON.Pixel_ratio(height,width)
            except Exception as e:
                pI = "None"
            parameters = [width,height,byte_order,round(megapixel,3),c_samp,b_p,dm,str(x),str(y),str(tw),str(th),pI,str(c_num),hm,meta]
            return parameters
    
    class GIF:

        @staticmethod
        def Get_Animations(origfile):
            img = open(origfile,"rb")
            reader = img.readlines()
            frame = 0
            nb = "False"
            anim = []
            m2 = "None"
            i = 0
            for line in reader:
                if b"NETSCAPE2.0" in line:
                    m = line.rsplit(b"NETSCAPE2.0")[1]
                    m2 = bytes(m.rstrip())
                    nb = "True"
                if nb == "True":
                    if b'\x00!\xf9\x04' in line:
                        frame = frame + line.count(b"\x00!\xf9\x04")
                        x = line.rsplit(b'\x00!\xf9\x04')[1]
                        if len(x) < 4:
                            x = reader[i + 1]
                        anim.append(x)
                i = i +1
            img.close()
            parameters = [frame,anim,m2,nb]
            return parameters
 
        @staticmethod
        def Get_Parameters(origfile):
            fm2 = "None"
            em2 = "None"
            dm2 = "None"
            tot_time = "None"
            pI = "None"
            width = 0
            height = 0
            megapixel = 0
            anim_param =  TYPE.GIF.Get_Animations(origfile)
            frame = anim_param[0]
            anim = anim_param[1]
            m2 = anim_param[2]
            nb = anim_param[3]
            img = open(origfile,"rb")
            reader = img.read()
            img.close()
            if b'GIF87a' in reader or b'GIF89a' in reader:
                if b'GIF87a' in reader:
                    version = "GIF87a"
                elif b'GIF89a' in reader:
                    version = "GIF89a"
                width,height,f,r,a= struct.unpack_from("<HHBBB", reader[6:16])
                g2 = Properties.GET.GIF.Details(f)[0]
                g3 = Properties.GET.GIF.Details(f)[1]
                g4 = Properties.GET.GIF.Details(f)[2]
                g5 = Properties.GET.GIF.Details(f)[3]
                if nb == "True":
                    m890,m3= struct.unpack_from("<HB",m2[1:4])
                    total = []
                    for string in anim:
                        m4,m5= struct.unpack_from("<HBx",string[1:8])
                        total.append(m4)
                    tot_time = Properties.GET.GIF.Duration(total)
                    fm2 = Properties.GET.GIF.Animation(m3)
                byte_order = "Little-Endian"
            width = int(width)
            height = int(height)
            try:
                pI = Properties.GET.COMMON.Pixel_ratio(height,width)
            except Exception as e:
                pI = "None"
            c_number = Properties.GET.GIF.Color_Numbers(g3)[0]
            b_number = Properties.GET.GIF.Color_Numbers(g3)[1] + " Bytes"
            parameters = [width,height,byte_order,round(megapixel,3),r,version,fm2,em2,dm2,g2,g3,frame,g4,pI,c_number,b_number,str(tot_time),g5]
            return parameters