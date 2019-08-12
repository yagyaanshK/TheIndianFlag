#complete flag

import turtle
import math
pi = math.pi

#below are the flag parameters reative to each other

width = float(input('Width of the flag = '))
length = 1.5*width
(r1)=width/8.3529
(r2)=(r1)*1.10294
(r0)=(r1)/5
spoke=4.450*r0
(r)=(r0)/4



#construction for the tricolours

india = turtle.Turtle()
india.speed(0)
india.penup()
india.goto(x=(-0.5*length),y=0.5*width)
india.pendown()
for i in ['#FF9933','#FFFFFF','#138808']:
  india.fillcolor(i)
  india.begin_fill()
  for j in range(2):
     india.forward(length)
     india.right(90)
     india.forward(width/3)
     india.right(90)
  india.end_fill()
  if i=='#FF9933':
   india.goto(x=(-0.5*length),y=width/6)
  elif i=='#FFFFFF':
   india.goto(x=(-0.5*length),y=-1*width/6)
  else:
   india.penup()
   india.goto(x=0,y=0)


#construction for the ashoka chakra



chakra = turtle.Turtle()
chakra.color('#000080')
chakra.speed(0)
chakra.penup()
chakra.goto(x=0,y=r1)
chakra.pendown()

#this parameter l will decide how smooth the circle is

l=1

#construction of circle of radius r1
angle=l*180/(r1*pi)
t= math.floor(360/angle)
chakra.fillcolor('#000080')
chakra.begin_fill()
for i in range(t):
   chakra.goto(x=(r1)*math.sin(i*pi*angle/180),y=(r1)*math.cos(i*pi*angle/180))
   

chakra.goto(x=0,y=r2)
#chakra.right(360-t*angle)

#construction of circle of radius r2  
angle=l*180/(r2*pi)
t= math.floor(360/angle)

for i in range(t):
   chakra.goto(x=-1*(r2)*math.sin(i*pi*angle/180),y=(r2)*math.cos(i*pi*angle/180))
chakra.goto(x=0,y=r1)

chakra.end_fill()


#construction of circle of radius r0

chakra.penup()
chakra.goto(x=0,y=r0)
#chakra.right(180-((360/angle)-t)*angle)
chakra.pendown()



chakra.fillcolor('#000080')
chakra.begin_fill()
angle=l*180/(r0*pi)
t= math.ceil(360/angle)
for i in range(t):
   chakra.goto(x=(r0)*math.sin(i*pi*angle/180),y=(r0)*math.cos(i*pi*angle/180))
chakra.end_fill()



#chakra.left(t*angle-360)


#construction of the spokes for chakra


india.left(90)
india.penup()
india.goto(x=0,y=r1-spoke)
india.pendown()
for n in range(24):
  india.color('#000080')
  india.fillcolor('#000080')
  india.begin_fill()
  india.left(6)
  india.forward(1.116*r0)
  india.right(8)
  india.forward(3.3422*r0)
  india.right(176)
  india.forward(3.3422*r0)
  india.right(8)
  india.forward(1.116*r0)
  india.end_fill()
  india.right(189)
  india.penup()
  india.goto(x=(r1-spoke)*math.sin(pi*(n+1)/12),y=(r1-spoke)*(math.cos(pi*(n+1)/12)))
  india.pendown()


#construction of small circles on chakra

#chakra.left(82.5)
chakra.penup()
chakra.goto(x=(r+r1)*math.sin(pi/24),y=(r+r1)*math.cos(pi/24))
chakra.pendown()


angle=l*180/(r*pi)
t= math.ceil(360/angle)
chakra.fillcolor('#000080')
for y in range(24):
  chakra.begin_fill()

  for i in range(t):
     chakra.goto(x=(r1)*math.sin(pi*(y+0.5)/12)+(r)*math.sin(i*pi*angle/180),y=(r1)*math.cos(pi*(y+0.5)/12)+(r)*math.cos(i*pi*angle/180))
  chakra.end_fill()
  chakra.penup()
#  chakra.left(t*angle-360)
  chakra.goto(x=(r+r1)*math.sin(pi*(y+1.5)/12),y=(r+r1)*math.cos(pi*(y+1.5)/12))
#  chakra.right(15)
  chakra.pendown()

  
india.hideturtle()
chakra.hideturtle()















