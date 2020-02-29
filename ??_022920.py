Clock.bpm = 140

p1 >> play("|x4|---o---", sample=3, crunch=3, bits=16, bitcrush=32).every(4, "stutter", Cycle([3,4]), dur=Cycle([2,1,3]))

p2 >> play("c", rate=sinvar([PRand([1,3]),4], 8), dur=var([1/4,1/3,1/2,1], 4)).every(8, "reverse")

p3 >> play("o o ", dur=1, sample=2, drive=0.05)


