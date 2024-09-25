import turtle as t
t.speed(100)
dookie = input ("which color :")
bg = input ("what backgroundcolor do you want :")
t.bgcolor ("black")
t.color (dookie)
t.left(120)
for i in range (36):
    t.forward(120)
    t.right(190)
t.mainloop()