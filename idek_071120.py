Clock.bpm = 160
Scale.default = Scale.minor
Root.default = "Ab"

prog1 = [2, 4, 1, 1]
p1 >> pasha(var(prog1, 4), dur=PSum(3,2)*2, oct=3, tremolo=2).every(4, "shuffle") + (0, 5, 3, 7)

p1.stop()


b1 >> jbass(var([0, 0.5, 0.75, 1], 2), dur=1/2, amp=0.75, oct=5).every(4, "rotate", var([2,3])) + var([0,1,7,5])

d1 >> play("v  v vv vv v vv ", drive=0.05)
d2 >> play("x   |o3|   ").every(4, "stutter", 4, dur=Cycle([3,2]))

d3 >> play("----").every(6, "stutter", 2)


