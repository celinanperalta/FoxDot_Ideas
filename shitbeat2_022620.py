Clock.bpm = 130
Root.default = "F"
Scale.default = Scale.minor
prog1 = [1,3,2,4]
bass1 = [0,0,2,1]
bass2 = [7,4,3,5]

d1 >> play("x  x  x ", dur=1/2, sample=3)
d2 >> play("--(-|o(31)|)-", rate=2).every(6, "stutter", 3)

d3 >> play("v  v  v v  v  v ", dur=1/4, formant=linvar([0, 4], 8)).every(4, "stutter", 4, dur=Cycle([3,2]))

kickhat = Group(d1, d2)
deep = d3

kickhat.amp = var([1,0], [32, 24])
deep.amp = var([0,1], [8,32])

p1 >> sinepad(prog1, dur=4, tremolo=2, room=0.5, mix=0.5).every(8, "shuffle") + (0, var([2,4]))
p2 >> pasha([0,2,4], dur=PDur(3,8), lpf=linvar([2000, 500], 16)) + var([0, -2, -7, -5])
p3 >> space([3, var([5, 7], 2), var([2,9])], dur=var([1/2, 1/3], [10,2]), amp=0.5, fmod=2).every(6, "rotate", 2)

b1 >> jbass(var([bass1, bass2], 8), dur=1, oct=5, tremolo=var([2,4], 32), spin=2, room=0.5, mix=0.5, amp=3)











