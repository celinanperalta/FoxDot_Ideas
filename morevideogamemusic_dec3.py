Scale.default = Scale.minor
var.prog = [5,var([1,2]),4,var([3,6])]

var.pause = var([1,0], [28,4])

d1 >> play("x |o3| ", dur=1, amp=var.pause).every(4, "stutter", 4, dur=Cycle([3,2]))
d2 >> play("----", dur=1)
d3 >> play("v  v  g v  v  (vg) ", amp=var.pause)

p1 >> ambi(var.prog, dur=PRand([4,8,2]), sus=p1.dur+1, oct=4, fmod=4, amp=var.pause) + var([(0,2), (3,5)])

p2 >> ambi(0, oct=3, drive=linvar([0.05,0.1], 4),amp=var.pause)

p3 >> ambi(2, dur=1/2, sus=0.3, amp=1) + (0, var.prog)

p4 >> pasha([2,PRand([3,4])], dur=var([1/2, PSum(3,2)]), amp=var([1,0], [PRand([6,8,12]),PRand([1,2,3])]), shape=0.2, formant=2) + var.prog + PRand([-3, 1])



