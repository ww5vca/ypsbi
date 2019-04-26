# -*- coding: utf-8 -*-
 
import os
import PIL.Image, PIL.ImageFont, PIL.ImageDraw

file = open("./List.txt","r")
list1 = file.readlines()
file.close

font = PIL.ImageFont.truetype(".\Cousine-Regular-1.ttf", 16)
im = PIL.Image.new("RGB", (100, 100), (255, 255, 255))    
dr = PIL.ImageDraw.Draw(im)

for listitem in list1:
    
    filename=listitem.replace("\n","")
    textcontent=filename.replace(" ","\n")
    countofline=filename.count(" ")+1
    #print(filename,textcontent,countofline)
 
    
    dr.rectangle((0,0,99,99),'white','white') 
    dr.text((10, 50-(countofline*14+(countofline-1)*5)/2), textcontent, font=font, fill="#000000")
    #im.show()
    #print("./export/"+filename+".pg")
    im.save("./export/"+filename+".jpg")


#100*100, font16, 5 lines * 9 chars

