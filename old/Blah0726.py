p1 >> keys(P(0,7,5,9) - var([0, 2, 3, 5], [8, 4, 2, 2]), drive=0.025).every(6, "stutter", )
d1 >> play("v x vv x", sample=0).every(6, "stutter", 2)
d2 >> play("<m  (m )><---(-*)>", formant=1)
b1 >> keys(PRand([2, 3, -1]), dur=PSum(3,2), oct= 6, amp=1)
d3 >> play("t ( t- (h-))", room=0.5, formant=1).every(4, "stutter", 1.5)
p3 >> pluck(P**(5,2,3,0) + var([0, 2, 4]), dur=1 ,amp=0.4).stop()

p1 >> keys(P(0,3,5,7) - var([5, 3, 2, 0], [4, 4, 4, 4]), dur = 1/2)
