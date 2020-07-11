Scale.default = Scale.major
Clock.bpm = 150
a=[3,5,3,5]
prog = [4,5,7,6]
d1 >> play("<----><v   o  vv v o  v>", dur=1/2, amp=1, hpf=200, lpf=5500, room=0.6)
b1 >> bass(var(prog, a), dur=a, amp=0.5, oct=5, delay=0, room=0.2, decay=3)
p2 >> keys(var(prog, a), dur=a, delay=0.03, oct=4, amp=0.6, echo=1)
p1 >> keys(var(prog, a) + (0,2),delay=0.03, oct=5, bend=0.045, room=0.5, amp=2)
