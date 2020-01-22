Clock.bpm = 100
d1 >> play("v  v  v v  v  v ", dur=1/4, amp=1, rate=linvar([1,1.5], 8), sample=0).every(4, "stutter", 4, dur=Cycle([3, 2]))

#after a while
d1.amp = var([0, 1], [4, 20])

d2 >> play(P["(-*) --"].amen(), sample=3, dur=1/2)
d3 >> play("h-(-o)-", sample=5, rate=1, pan=var([-1, 1]), drive=0.5, dur=1/2).every(6, "rotate", 3)
d4 >> play("k *$", amp=var([0, 1], [16, 8]), drive=0.05)

b1 >> bass([3, 6, 7, 9], drive=1, oct=4, hpf=var([0,500], [32, 8]), dur=1/2, amp=linvar([0, 1], 1.25)).every(PRand([2, 4, 6]), "reverse") + var([0,-1], 8)

p1 >> pasha([11, 4, 5, 3, 2], drive=0, dur=1/2, oct=var([4,5], [16,16]), amp=1, pan=PRand([-1, 1])) + var([0, 2, -1, 0], 4)


dur1 = var([1/4, 1/2, 1/4], 1)
p1.dur = dur1

p1.dur=1/3

p1.stop()
