Clock.bpm = 100
Scale.default = Scale.minMaj
Root.default = "Bb"

d1 >> play("(xo)---").every(8,"stutter", 2)≥
d2 >> play("  o  ox o  xo  x ").every(4, "stutter", 4, dur=Cycle([3,2]))
d3 >> play("--([---]-|*3|)--)-", dur=1/4)
d4 >> play("|%3|       ", dur=1, drive=0.4, tremolo=4)

p1 >> ambi(var([0,3,4.5,2],2), dur=1/2, oct=4, tremolo=2)
p2 >> space(PTri(7), dur=var([1/2,1/4], [8,4]), oct=4)

p3 >> pasha([5, 3, 1], dur=1/3, oct=var([3,4], 4), fmod=2)

b1 >> jbass([0, 0.5], dur=4, tremolo=4, drive=0.05) + var([0, 3.5], 4)
