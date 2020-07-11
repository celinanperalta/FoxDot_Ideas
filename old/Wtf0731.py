Scale.default = Scale.minor

p1 >> viola([(0,2)], dur=16, hpf=400, formant=1, sus=4)
p2 >> viola([0, 0, 0, -1], dur=8, sus=4, formant=1)
b1 >> ambi([0, -4], dur=8, oct=4, sus=8)

p3 >> soft(2, oct=6, amp=1.5)

p4 >> soft(PxRand(0, 9), dur=PRand([2, 4, 1]), oct=4, formant=1, sus=4)

d1 >> play("--({-*})-", pan=PRand([-1, 1]), rate=PTri(8), amp=2, dur=1/4, formant=0).every(6, "stutter", PRand([2, 4]))

d2 >> play("x-o(---[--])", sample=2)

d3 >> play("vcmp", amp=PRand(0, 1), dur=1/4, sample=6, rate=1)

d4 >> play("h  hh h ").every(4, "mirror").every(6, "stutter", 2)

p3 >> pluck((0, var([4, 3.5, 5, 2]), 2), dur=PDur(3,5), drive=0.2, amp=0.5)

