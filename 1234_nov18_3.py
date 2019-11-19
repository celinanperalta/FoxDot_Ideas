#1234 - nov 18 no. 3

Clock.bpm = 120

d1 >> play("v v(v[*v])")
d2 >> play("--(--[---]-)-", sample=2, drive=0.05)
d3 >> play("x o ").every(4,"stutter")
d4 >> play("1234", rate=1, drive=0.005, sample=2, dur=PDur(5, 16), amp=PZ12([0, 1], [1, 0.5])[:15], lpf=1000).every(3, "reverse")

var.prog = var([2, -1], dur=8)

b1 >> jbass(var.prog, dur=1/2, oct=var([4.5, 4.75], [16,16]))

