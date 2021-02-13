import turtle

def draw(t,length,n):
    if n==0:
        return
    angle=60
    t.fd(length*3)
    t.lt(angle)
    draw(t,length,n-1)
    # draw(t,length,n-1)

    t.rt(angle*2)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*3)

bob=turtle.Turtle()
draw(bob,10,6)
turtle.mainloop()