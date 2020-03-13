Clock.bpm = 150
Root.default = "C"
Scale.default = Scale.major


d1 >> play("x o ", dur=1, sample=3, formant=1).every(4, "stutter", 2, dur=Cycle([3,2]))
d2 >> play("--(--[---]-)-", dur=1, sample=0, lpf=6000).every(4, "stutter", 2, dur=Cycle([3,2]))

p1 >> keys([0, 5], dur=8, oct=4) + (0,2,4)

p2 >> jbass([1, 0, -2, 3, 1, -2], dur=[1.5,1.5,5], amp=0.5, tremolo=2)
