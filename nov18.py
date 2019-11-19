#what the fuck

Clock.bpm = 80

d1 >> play("(x[xx]) o ", dur=1, lpf=800, sample=1).every(6, "stutter", var(2,4))

d2 >> play("(-*-)-({*^}--)-", sample=4).every(3, "mirror").every(6, "stutter", 2)

d3 >> play("g *(*g)", sample=var([0, 1, 3]), dur=1/2)

p1 >> bass([8, 7, var([5.5, 8.5, 5.5]), var([1, 1.5])], amp=0.5, dur=var([1/2, 1/3], [16, 4])).every(4, "mirror")

p2 >> pluck(p1.follow() + var([0, [0,3,2]], [4,4]), dur=1/2, amp=var([0.7, 0],[32,16]))

p3 >> soft(linvar([-8,8], 16), dur=1/4, hpf=600, formant=1)

p4 >> blip(var([6, 5.5], [8, 8]), dur=PSum(3,2))




