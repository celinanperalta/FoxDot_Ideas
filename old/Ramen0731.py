Scale.default = Scale.major


p1 >> sinepad((0, 3, 5, 7, 9) + var([2, 0, -5, 0]), dur=[1.5, 1.5, 1], amp=0.5).every(6, "mirror")
p2 >> keys([2, 0, -5, 0], dur=4, oct=5, amp=2, sus=4).every(6, "offadd", 2)

p3 >> blip(var([PBern(8), P10(16)], 4), lpf=2000, dist=1, dur=1/4) + var([0, 2, -3, 2], 4)
p4 >> space(PZ12([0, 1], [1, 0.5]))

d1 >> play("<----><(v ) * ><([b *t]  by)   >", sample=2, lpf=3000, hpf=400).every(6, "stutter", 4)
d2 >> play("<---(-*)>", dur=var([1/2, 1/4],[4, 12]), rate=PSine(16),  amp=linvar([0, 2], 8), pan=PRand(-1, 1), crush=0.5).every(4, "mirror")

d3 >> play("<vt*t><  v >", amp=var([1, 0], [28, 4]), sample=2, crush=1)
d4 >> play("<v v >", amp=var([1, 0], [28, 4]), sample=2, crush=1)
b1 >> jbass(var([-2, 5, -2, 7], 2), tremolo=2, amp = 1, dur=1/2, sus=1.5)

p5 >> pluck([P**(9, 8, 7, 5), P**(0, 5, -3, 2)], drive=0.05, bend=0.02, lpf=linvar([1000,5000], 4), formant=var([0, 1], [56, 8])).every(6, "stutter", 2)


main_b = Group(d1, d2, p1, p2, b1)
main_b.amp = var([1, 0], [56, 8])

d3.amp = var([0, 1], 32)
d4.amp = var([1, 0], 32)
