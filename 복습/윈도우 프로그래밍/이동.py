import turtle as t

for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(3):
    t.forward(100)
    t.left(120)

t.right(180)

for i in range(3):
    t.forward(100)
    t.right(120)

#변수 사용하기
n=4
d=100
for i in range(n):
    t.forward(d)
    t.left(360/n)

t.circle(50)#반지름의 길이-50픽셀
t.color("red")
t.pensize(3)
t.circle(50)

t.mainloop()

