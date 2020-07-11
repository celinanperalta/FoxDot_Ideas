Clock.bpm = 150
Scale.default = Scale.major
Root.default = "C"


p1 >> blip([1, 3 ,7 ,8], dur=1/2, amp=1.5, oct=3, drive=0.2).every(4, "shuffle") + var([0, 0, 2, 0], 4)
p2 >> space([1, 3, 7, 8], dur=1).every(8, "reverse")

p3 >> keys([4, 4, 5, var([7, 9])], dur=2, oct=5, tremolo=2, amp=3) + (0,2,7) 

b1 >> jbass([1,3,-2,-1.5,-1.5,-1.5], dur=PSum(3,2), drive=0.05, amp=2) + 0

d1 >> play("x-(-[--])-o---", sample=3, formant=1, amp=3)

d2 >> play("v  v    v  v v  ", drive=0.2, amp=3)


