Clock.bpm = 120
Scale.default = Scale.minor
Root.default = "G"

prog1 = [0, 4]
prog2 = PTri(3)

d1 >> play("xxx--------", dur=[1/3, 1/3, 1/3, 1/2,1/2,1/2,1/2,1/2,1/2])
d2 >> play(" *", dur=var([1/3, 1], [4, 8]))
d3 >> play("% ", dur=2)

prog = prog1
b1 >> jbass(var(prog, [3/2,1/2]), dur=1/2, tremolo=4, fmod=2)

p1 >> keys(PBern(5), oct=6, dur=Cycle([3,2])/4, tremolo=1, fmod=8)

p2 >> ambi([1])

