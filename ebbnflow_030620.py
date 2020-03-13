Clock.bpm = 100
Root.default = "F"

gen1 = PWalk(max=4, step=0.25, start=0)

b1 >> jbass(gen1, oct=6, dur=1/2, tremolo=4, fmod=2, amp=var([0,1], [48, 32]))
b2 >> jbass([5, 2, 3, 3], dur=4, oct=5, amp=0.5, tremolo=1.5)

d1 >> play("xx-x--x(-[---])-x--x[--]--", sample=3, amp=var([2, 0], [64, 16])).every(4, "stutter", 4, dur=Cycle([3,2]))
d2 >> play(" o", dur=2, sample=3, amp=d1.amp, cut=0.5, formant=1)

p1 >> pasha(var([4, 7, 3, 5, 6]), dur=var(PRand([1/2, 1/3, 1/4]), PRand([2,4,8])), room=0.2, mix=0.2, oct=4, drive=0.1, formant=linvar([1,4], 8), amp=var([1,0], [48, 32])).every(4, "shuffle") + var([0, 2, 2, 0])

p2 >> keys(var([0, -3, -2], [4,4,8]), dur=1, room=0.5, mix=0.5, amp=2, drive=linvar([0.01, 0.1], 8)).every(12, "reverse") + (0,2,7)
