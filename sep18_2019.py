Clock.bpm = 160

d1 >> play("<X   >", dur=var([1/4, 1/2],[64,32]), rate=1, room=3, amp=1.5).every(6, "stutter", 2)
d2 >> play("<---->", dur=1/4, rate=linvar([0,8], 8), sample=var([1,2], [4,4])).every(3, "reverse")
d3 >> play("o *  ", dur=1/2, amp=2).every(4, "reverse")
d4 >> play("x", dur=PSum(3,8), rate=1)


b1 >> bass(var([-1, 1], [16,16]), sus=0.5, bits=[1,2], dur=var([[1/2,1], [1/2,1/2]], [4,16]))



#p1 >> pluck(P(0, 3, 5, 9), dur=1/2, sus=1.2, room=0.5, oct=4, lpf=linvar([1000, 2000], 8)) + var([0, 2, 4, 2], [3.5, 4.5, 3.5, 4.5])

#b1 >> bass(var([2, 4, -2], [4,4,8]), dur=1, sus=2, amp=0.5)
