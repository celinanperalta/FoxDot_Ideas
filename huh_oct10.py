Clock.bpm = 130
Root.default.set("D")

d1 >> play("[[---] ][[---] ][[---] ][[---] ][- - ][[---] ][[---] ][- - ]", dur=1, sample=0, lpf=5000)
d2 >> play("<x  x (x )([ox] ) >", dur=1/2, sample=0, lpf=3000)

d3 >> play("v    v  ", dur=1/2, sample=6).every(6, "stutter", 2)

d4 >> play("-{tmc}--", rate=PSine(linvar([16,32], 2)), dur=1/4)


b1 >> bass([0, -1, 2, 1, 4], dur=[2,2,2,1,1], amp=0.5).stop()


