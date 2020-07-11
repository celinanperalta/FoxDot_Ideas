

p1 >> ripple(var([9,7,3]) + (0,2), dur=8, room=0.4, echo=0.5, delay=(0,0.5))
p2 >> soft(amp=linvar([0.3,2],8), pan=linvar([-1,1],4), oct=5)

p3 >> viola([0,2], dur=16, oct=4, room=2)

b1 >> ambi(p1.degree - 1, dur = 4, amp = 0.3)

l1 >> viola(1)


