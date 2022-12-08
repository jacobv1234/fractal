from turtle import *

t = Turtle()
t.speed(0)
t.turtlesize(0.01)

i = 1

def dectobin(num):
    return str(bin(num))

while True:
    t.fd(2)
    t.lt(90)
    t.fd(2)
    checks = 0
    for char in range(len(dectobin(i))-1,-1,-1):
        if dectobin(i)[char] == '1':
            index = checks
            break
        checks += 1
    t.rt(90*(index%4))
    i+=1

    


# f,l,f,0,f,l,f,90,f,l,f,0,f,l,f,180,f,l,f,0,f,l,f,90,f,l,f,0,f,l,f,270