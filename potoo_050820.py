Clock.bpm = 140
Scale.default = Scale.minor
Root.default = "F"

d1 >> play("x  xx xxox ox   ", dur=1/2)
d2 >> play("- - ").offbeat()

d3 >> play(" * - --", drive=0.5)
d4 >> play("c ( d ) ")
d5 >> play("---hh-hh-h", sample=0).every(8, "rotate", 3)

d6 >> play("--o-", dur=1, sample=3)

p1 >> pluck([0.5, 1, 1.5, 2, 2.5], dur=(PSum(3, 2) + 2) / 4, fmod=2, room=0.8, mix=0.8, amp=2).every(4, "shuffle")




