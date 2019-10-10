Clock.bpm = 130
Root.default.set("D")

d1 >> play("[[---] ][[---] ][[---] ][[---] ][- - ][[---] ][[---] ][- - ]", dur=1, sample=0, lpf=5000)
d2 >> play("<x  x (x )([ox] ) >", dur=1/2, sample=0, lpf=3000)
b1 >> bass([0, -1, 2, 1, 4], dur=[4,4,4,2,2], amp=0.4)

