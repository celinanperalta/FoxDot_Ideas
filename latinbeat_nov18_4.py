d1 >> play("v  *v * ", dur=1/4, sample=2).every(6,"stutter", 2)

var.prog = [2, 2, 4, 3.5, 3.5, 5, 4, 4, 6, 5, 6.5, 6]

p1 >> bass(var.prog, dur=PSum(3,2), oct=5)

p2 >> blip(P**(4,5,6,5), dur=2, amp=var([1,0], [16,32]), pan=PStep(4, P*(-1, 1)))



