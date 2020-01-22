from math import floor
Clock.bpm = 150
Scale.default = Scale.minorPentatonic

d1 >> play("x x o (   o) ", sample=3).every(4, "stutter", 4, dur=Cycle([3,2]))
d2 >> play("--(-[---])-", sample=4)
d3 >> play("v vv vv vv vv v ", rate=var([1,1.5], 4), coarse=1, chop=0.5, drive=0.04)

d4 >> play("{gb}", dur=var([1/2, PRand([1/4, 1/2])], 16), amp=0.40, rate=linvar([0,PRand(4)], PRand(8)))


for i in range(1, 5):
    p1 >> pasha(sinvar([-i,i],8), amp=0.25, dur=var([Cycle([1/2,1])/2, 1], PRand([4,6,8])), fmod=4, formant=1, drive=linvar([0.05, 0.5], 4), shape=0.5)


p2 >> keys(var([([5,4,3,2]),([3,2,1,3])], 2), drive=0.4, chop=0.5, coarse=2)


p1.amp = var([0,0.25], [8,24])
p2.amp = var([1,0], [24,8])

p1.stop()
