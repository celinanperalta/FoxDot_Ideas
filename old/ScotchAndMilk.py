Scale.default = Scale.minor

p1 >> viola([(0,2)], dur=8, oct=5, hpf=200, formant=1)
p2 >> viola([0, 0, 0, -1], dur=8)
b1 >> ambi([0, -4], dur=8, oct=4)

p3 >> soft(2, oct=6, amp=1.5)
