Clock.bpm = 160
Root.default = "D"
Scale.defalut = Scale.minor

prog1 = [2, 3, 2, 1, 2]
dur1 = [3, 2, 1, 1, 1]

p1 >> bass(var([prog1, 2], [8, 8]), dur=var([dur1, 1/2], [8,16]), oct=4, mix=0.2, room=0.2, drive=0.05)
p2 >> keys(prog1, dur=dur1) + var([2,3], 16)

p3 >> pasha([5, 6, 7, 8], dur=1/3, amp=var([1,0], 2), oct=4, fmod=4, room=0.5, mix=0.2).every(16, "reverse") + var(PRand([0,2,4]), 8)

p3.stop()

d1 >> play("<x o ><--(-|~6|)->", dur=1, sample=3).every(16, "stutter", 2)

d2 >> play(" *", dur=1, formant=4, amp=0.4)

d3 >> play("--(acx)-", sample=2, rate=linvar([1,5], PRand([2,4])), dur=var([1/2,1/4], [14,2]))


