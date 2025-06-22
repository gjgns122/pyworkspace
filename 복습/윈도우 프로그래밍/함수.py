import turtle as t

#다각형 그리기

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(3)
polygon(5)

t.up()
t.forward(100)
t.down()

polygon2(3,100)
polygon2(5,100)
#키보드 조종하기
#오른쪽으로 회전후 이동
def turn_right():
  t.setheading(180) #거북이 머리 방향

def turn_left():
  t.setheading(270)

def turn_up():
   t.setheading(90)
   t.forward(10)

def turn_down():
   t.setheading(270)
   t.forward(10)

t.shape('turtle')
t.onkeypress(turn_right,"right")
t.onkeypress(turn_up,"up")
t.onkeypress(turn_left,"left")
t.onkeypress(turn_down,"down")
t.listen()

import tkinter

