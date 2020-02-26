import math

Clock.bpm = 100

d1 >> play("x-o-", dur=1/4, amp=2,rate=PWhite(1,6), drive=1).every(6, "shuffle").stop()

d2 >> play("x x ", sample=4, dur=1, amp=1, formant=1, crush=32, bits=8).every(6, "stutter", 2, dur=Cycle([3,2]))
d3 >> play("--o-", dur=1/2, sample=0, drive=0, cut=0.5, amp=2).every(6, "stutter", 2, dur=Cycle([3,2])).offbeat()

b1 >> sinepad(PwRand([0, 1], [1, 2])[:10], oct=4, dur=1/2, drive=1, rate=var([1, -1]), reverb=1, room=1, chop=4, sus=2, coarse=2)

d_all.lpf = 5500

p1 >> keys(var([2, 0, 2, -2], 4), dur=PSum(3,2) * 2, room=0.5, reverb=1, oct=4, amp=3) + (0, 3, 5, var([7, 9], 4))




