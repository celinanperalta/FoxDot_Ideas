Clock.bpm = 140
Root.default = "D"
Scale.default = Scale.minor

p1 >> ambi([2, 4], dur=PDur(3,8), oct=4, drive=0.02)

p2 >> pasha([var([0, 1], 4), 4, 2, var([3, 7], 4)], oct=4, dur=PDur(3,8), tremolo=4, room=0.5, mix=0.5, lpf=2000, hpf=500).every(12, "shuffle")

p3 >> space([1, 2, 5, 4], pan=linvar([-1,1],8), dur=PSum(3,5), oct=5).every(8, "shuffle") + var([0, 2, -1,-3], 4)

prog1 = var([-5, -3, -7, -7], 8)

prog2 = var([0, -7, -5, -3], 8)

p4 >> keys(var([prog1, prog2], 32), dur=1, amp=1.4, sus=2, tremolo=var([2, 4], [10, 2]), room=0.4, mix=0.4, fmod=linvar([1,8], 8)) + (0,var([3,7], 8),5,11)

p5 >> keys([9,8,4], oct=5, dur=var([1/2, 1], [12, 4]) + var(PRand(4), 3)

d1 >> play("xx--x[--]-xx-([--]-)-x-x-").every(4, "stutter", 4, dur=Cycle([3,2]))

d2 >> play("--(-|*3|)-", dur=1/2, sample=3, formant=4, amp=0.4)

d3 >> play("xx x x ", dur=1/2, rate=1, sample=3)
