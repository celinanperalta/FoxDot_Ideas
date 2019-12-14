Clock.bpm = 100
Scale.default = Scale.minor

prog1 = [0, 4, 2, 6]


d1 >> play("vv|o3|vv v ", dur=1/2).every(4, "stutter", 4, dur=Cycle([3,2]))
d2 >> play("----", amp=2, sample=3, rate=sinvar([-8,8], 2)).every(PRand([6,4,2]), "stutter", 2)

p1 >> ambi(prog1, dur=PSum(3,2)*8, sus=p1.dur+0.75).every(6, "mirror") + (0,2)

p2 >> keys(var([0,2,4,6], 4), amp=1, dur=PSum(3,2), sus=1, drive=0.05) + (0, var([4,7], 16))

p3 >> pasha(prog1, dur=PDur(5,8), chop=0.25, coarse=2, drive=0.05, fmod=2).reverse() + linvar([0, 5], 4)


