Scale.default = Scale.minor
Root.default = "C"
Clock.bpm = 120


d1 >> play("vv v", dur=Cycle([1.5,1]), amp=.75, hpf=50).every(4, "stutter", 4, dur=Cycle([3,2]))
d2 >> play("- --", sample=3, formant=0, drive=0.1, bits=8, bitcrush=16, rate=var([1, PWhite(1,5)], [32, 16])).every(6, "stutter", 3)
d3 >> play(" |o3|", dur=1, drive=0, dirt=1, crunch=5, cut=0.5)
d4 >> play("|x3|---", sample=4).every(4, "stutter", 2)

d6 >> play("-", amp = 0.5, rate=-1)

d_group1 = Group(d1, d2)
d_group2 = Group(d3, d4)

d_group1.amp = 1
d_group2.amp = var([1, 0], [28, 4])


