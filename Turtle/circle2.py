import turtle as t
def draw(rad):
    t.circle(rad)
    t.up()
    t.setpos(0,-rad)
    t.down()

for i in range(6):
    draw(20+20*i)

t.done()
