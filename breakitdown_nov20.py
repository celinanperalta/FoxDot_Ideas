Clock.bpm = 100

d1 >> play("v  v  v v  v  v ", dur=1/4, amp=var([1,0], [32, 16]), rate=linvar([1,1.5], 16), sample=0).every(4, "stutter", 4, dur=Cycle([3, 2]))

d2 >> play("(-*) - ", sample=3, delay=0, dur=1/4)
d3 >> play("h-(-o)-", sample=5, rate=1, pan=var([-1, 1]), drive=0.5).every(6, "rotate", 3)
d4 >> play("k [g{g }] ", amp=var([0, 1], [16, 8]), drive=0.05)

b1 >> bass([3, 6, 7, 9], drive=1 , hpf=var([0,500], [32, 8]), dur=1/2, amp=linvar([0, 1], 1.25)).every(PRand([2, 4, 6]), "reverse")

p1 >> sinepad([11, 4, 5, 3, 2], drive=0.5, dur=var([1/4, 1/2, 1/4], 1), oct=var([4,5], [16,16]), amp=0.6, pan=PRand([-1, 1])) + var([0, 2, -1, 0], [4, 4, 4, 4])


