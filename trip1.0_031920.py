Clock.bpm = 100
Root.default = "Bb"
Scale.default = Scale.minor

d1 >> play("xxx             ", dur=1/4).every(4, "stutter", 1, dur=Cycle([3,2]))
d2 >> play(" |o3|", amp=2, dur=1, lpf=1000)
d3 >> play("----", dur=var([1/3, 1/4],[4,12]), rate=linvar([1,6], 4))

p1 >> ambi(var([0, 2, 0, -1], 8), oct=4, tremolo=2, fmod=0, room=0.5, mix=0.2) + (0,2,5)
p2 >> ambi(var([0, 2, 0, -1], 8), oct=4, room=0.5, mix=0.5) + var(PRand([2, 4, 5]))

p3 >> space(var([7, 2, 3], [9, 4, 5]), amp=0.5).every(PRand(4), "rotate", 2)
