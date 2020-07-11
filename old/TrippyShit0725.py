p1 >> ripple(var([9,7,3]) + (0,2), dur=8, room=0.4, echo=0.5, delay=(0,0.5), amp=0.2)
p2 >> soft(amp=linvar([0.3,2],8), pan=linvar([-1,1],4), oct=5)
p3 >> viola([0,2], dur=16, oct=4, room=2)

b1 >> bass(p5.degree, dur = 6, amp = 0.3, oct=6)

p4 >> snick(1, dur=8, amp=PRand(0,1), pan=PRand(-1,1))
p5 >> soft(P**(1,5,P+(3,7)), dur=4, amp=0.5, echo=1, room=0.4)
p6 >> feel(var([0,3,8,3]))

p7 >> space(PRand(9), dur=PRand([1,2,4,6]), formant=1)


