Clock.bpm = 150
Scale.default = Scale.major
Root.default = "A"

d1 >> play("x   x     x   xx")

d2 >> play("----", sample=0)
d3 >> play("x x    x  x  xx ", sample=2, room=0.5, mix=0.2)
d4 >> play(" *", dur=2, formant=0, cut=0.5)

p1 >> keys([0,-2, -4], dur=[4,4,8], oct=4, room=0.5, mix=0.5, drive=0.1, fmod=2, tremolo=2) + (0, 2, 4)



