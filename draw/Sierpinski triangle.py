
# 사각 나선
import turtle as t

def Sierpinski_triangle(tri_len):
    if tri_len <= 10:
        for i in range(0, 3):
            t.forward(tri_len)
            t.left(120)
        return

    new_len = tri_len / 2
    Sierpinski_triangle(new_len)
    t.forward(new_len)
    Sierpinski_triangle(new_len)
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    Sierpinski_triangle(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)

t.speed(0)
Sierpinski_triangle(160)
t.hideturtle()
t.done()
