Clock.bpm = var([90, 180], 32)
Root.default = "Bb"
Scale.default = Scale.minor

d1 >> play("--(/---)-hdur={*/o}{*/o}{*/o}", sample=var([1,2, 3], 1/2), dur=var([1, 1/2, 1/3], [8,16,8]), spin=4, rate=var([1, linvar([1,4], 4)], 8)).every(12, "reverse")

d2 >> play("x o ", dur=1/2).every(4, "stutter", 4, dur=Cycle([3,4,2]))

d3 >> play("v  v x  v  x v     ", sample=var([1, 2]), rate=var([1,1.5], 8))

d4 >> play(" ( o)", dur=2, sample=3)

d5 >> play("^|$3|", sample=1, cut=0.5, dur=2)

d6 >> play("-.--", amp=4, sample=4)

b1 >> jbass([4,0,2,1], oct=4, dur=[1.5, 1.5, 1.5, 3.5]) + var(PRand(4))

p1 >> pasha([0, 4, 7, 2], dur=.5, amp=var([0,1], [7,1])) + var(PRand(4)) + (0,2)

p2 >> space(PWalk(4,1,1)[:10], dur=PSum(3,2), tremolo=2, fmod=2)
