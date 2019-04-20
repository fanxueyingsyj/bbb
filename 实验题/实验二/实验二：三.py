from turtle import *
turtle.setup(650,350,200,200)
penup()
seth(90)
fd(40)
pensize(5)
pencolor("green")
seth(90)
pendown()
for i in range(2):
      for i in range(3):
            seth(-135)
            fd(30)
            circle(1,90)
            seth(0)
            fd(30)
      seth(-90)
      fd(30)
      circle(1,180)



