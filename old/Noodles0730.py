Scale.default = Scale.major



p1 >> sinepad((0, 3, 5, 7, 9) + var([2, 0, -5, 0]), dur=[1.5, 1.5, 1], amp=0.5)
p2 >> keys([2, 0, -5, 0], dur=4, oct=5, amp=2, sus=4)

d1 >> play("<----><(v ) * ><([b *t]  by)   >", sample=2, lpf=4000).every(6, "stutter", 2)

p3 >> pluck([0,2,4])
