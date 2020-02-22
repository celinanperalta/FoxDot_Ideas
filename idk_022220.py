Scale.default = Scale.dorian
    

d1 >> play("x-o-").every(6, "stutter", 2, dur=Cycle([3,2]))
d2 >> play("----", dur=1/4, rate=linvar([-4,4], 8))

prog1 = [1, 0.5, 0.5, 0.5]

b1 >> bass(prog1, dur=PSum(3,2), fmod=2, oct=5).every(8, "stutter", 2)

p2 >> pasha(PRand([1,2,1,0.5]), dur=1/4, oct=var([3,4,5,4], 4)).every(PRand([4,8,12]), "reverse")
p3 >> blip([5], dur=1/4, amp=var([1, 0], [1, 7]))






