Clock.bpm = 140
Scale.default = Scale.minor
Root.default = "G"

prog1 = [0, 4]
prog2 = PTri(3)

d1 >> play("xxx--------", dur=[1/3, 1/3, 1/3, 1/2, 1/2,1/2,1/2,1/2,1/2])
d2 >> play(" *", dur=var([1/2, 1], [4, 8]))
d3 >> play("% ", dur=2)

p1 >> jbass(PEuclid2(var([3,5], 8),8, PRand(1,5), PRand(1,5)), oct=5, dur=1/2)
