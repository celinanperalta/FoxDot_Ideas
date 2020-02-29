Clock.bpm = 120
Root.default = "D"
Scale.default = Scale.minor

p1 >> ambi([2, 0, 2, 0], pan=linvar([-1,1],8), dur=1/4, oct=3).every(8, "shuffle") + var([0, 2, -1,-3], 4)

p2 >> pasha([var([0, 1], 4), 4, 2, var([3, 7], 4)], oct=4, dur=PDur(3,8), tremolo=4, room=0.5, mix=0.5, lpf=2000, hpf=500) + (0,3,7,9)

p3 >> space([1, 2, 5, 4], pan=linvar([-1,1],8), dur=PSum(3,5), oct=5).every(8, "shuffle") + var([0, 2, -1,-3], 4)

p4 >> keys(var([-7, -3, -5, -5], 8), dur=1, sus=2, tremolo=2) + (0,3,5,11)

