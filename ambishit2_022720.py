Clock.bpm = 90
Root.default = "D"
Scale.default = Scale.minMaj


p1 >> sinepad([4, 1], dur=4, tremolo=4)

p2 >> sinepad([3, 2], dur=2, tremolo=4)

p3 >> sinepad([0, 1, 3, 5.5], dur=1, tremolo=4)

p4 >> sinepad([4], dur=4, fmod=2, slide=var([0.05, -0.05]))
p5 >> sinepad([7], dur=8, oct=4, fmod=4, slide=var([-0.05, 0.05]))

p6 >> ambi(0, room=0.2, mix=0.5, sus=2, amp=2) + (PRand([0,2]), PRand([7,3,4])) + 2

p7 >> viola([2, 5.5], dur=1/2, oct=4, sus=2, mix=0.5, room=0.5, tremolo=linvar([2,4,8], 4))

d1 >> play("x o ", dur=1, formant=1)
d2 >> play("----", sample=2, lpf=1000, amp=4, drive=0.01).every(3, "stutter", 2)


