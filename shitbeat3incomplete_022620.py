Clock.bpm = 130
Root.default = "G"
Scale.default = Scale.major


d1 >> play("x-o-").every(4, "stutter", 4, dur=Cycle([3,2]))

p1 >> pasha(var([0, 1], 6), dur=[1/4, 1/4, 1/2], oct=4)





