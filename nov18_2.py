Clock.bpm = 100

var.prog = var([0, 2, 3, 3], dur=4)
var.prog2 = (0, var([2, 2, 2, 1.5]), 4)

b1 >> bass(var.prog, dur=2, amp=0)

p1 >> keys(var.prog + var.prog2, dur=4, lpf=1500, hpf=500)
p2 >> soft(var.prog, amp=var([1,0], [32,16]))
p3 >> blip(var.prog, dur=PDur(2,5), amp=var([1,0], [32,16]))
p4 >> sinepad([-1, 0, 2, 4] + var.prog, dur=1/2).every(3, "reverse")

d1 >> play("(g*)   ")
d2 >> play("--(-[--])[--]")
d3 >> play("(v ) (ook) ")

