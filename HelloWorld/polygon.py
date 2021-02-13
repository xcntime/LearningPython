import turtle
def polygon(bob,cnt,len):
    circle = 360.0 / cnt
    for i in range(cnt):
        bob.fd(len)
        bob.lt(circle)

bob=turtle.Turtle()
#turtle.mainloop()

for i in range(3,30):
    polygon(bob,i,+10*4)
turtle.mainloop()