from PIL import Image,ImageDraw,ImageFont

image=Image.new('RGB',(400,400)# page size
,(255,140,0))# orange color code

draw=ImageDraw.Draw(image)

font=ImageFont.load_default()#(‘arial.ttf’,size=45) # image font

import random# for random number

import qrcode # QR code module


print('\n\nTitle:- ID GENERATOR BY NIKHIL GOPALE')
print('*******************************')
print('\n\nAll Field COMpulsorY')
print('*********************************')
print('\n\nUSE UPPERCASE')
print('************************************')
print('\n\nPlease write CORRECT INFOrmation')
print('******************-_-***********************')

(x,y)=(50,50) # position
my=input('\nENTER COLLEGE NAME : ')
college=my
color='rgb(0,0,0)'  # color code black
font=ImageFont.load_default()  #font
draw.text((x,y),my,fill=color,font=font)

(x,y)=(50,80)
idno=random.randint(1,100) # random no
my=str('ID '+str(idno))
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)


(x,y)=(50,110)
my=input('\nENTER  FULL NAME : ')
name=my
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)


(x,y)=(50,140)
my=input('\nENTER GENDER : ')
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)


(x,y)=(50,160)
my=input('\nENTER MOBILE NUMBER : ')
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)




(x,y)=(50,210)
my=input('\nENTER AGE : ')
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)



(x,y)=(50,180)
my=input('\nENTER YOUR DOB : ')
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)



(x,y)=(50,240)
my=input('\nENTER BLOOD GROUP : ')
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)



(x,y)=(50,270)
my=input('\nENTER ADDRESS : ')
color='rgb(0,0,0)'
font=ImageFont.load_default()
draw.text((x,y),my,fill=color,font=font)



# QR code make and save

image.save(str(name)+'.png')     # image save with name

# QR code make ,set box size, border,version
img=qrcode.make(str(name)+str(idno),box_size=4,version=1) # we can add more data in QR code 

img.save(str(idno)+'.bmp')    # save bmp with id no

qrcode=Image.open(name+'.png')    # image open

data=Image.open(str(idno)+'.bmp')  # bmp img open

qrcode.paste(data,(250,40)) # position of QR
 
qrcode.save(name+'.png')# save QR with name


#ending details 
print('\n\nID SUCCESFULLY GENERATOR  '+name+'.png')    # print info + name + png


print('\n\n if you want to Rewrite information, Then Exit and write correct information again ')

print('\n\n THANK YOU ')

# for exit 
eval(input('\n\nPress any key to Exit….')) 
