Clock.bpm = 120
Root.default = 'C'
Scale.default = Scale.major

d1 >> play("----", amp=1, sample=3, dur=1, formant=0)
d2 >> play("x      x    x  x", sample=3, formant=0).every(4, "stutter", 2)
d3 >> play(" |o5|", dur=2, lpf=1200)

b1 >> bass([0, -2.5, -3, -3], dur=[3, 5], amp=0.5)

b2 >> ambi([0, -2.5, -3, -3], dur=[3, 5], amp=0.5, drive=0.05, tremolo=2) + var([(0, 4, 7), (0,3,5), (0,4,6), (0,4,6)])



