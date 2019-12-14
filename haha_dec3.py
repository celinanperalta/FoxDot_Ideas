Clock.bpm = 160
Scale.default = Scale.minor

d1 >> play("--(-[---])-", rate=var([4,linvar([4,1], 4)], [4,4]), drive=0.2)
d2 >> play("x o ", dur=1).every(4, "stutter", 4, dur=Cycle([3,8]))
d3 >> play("vvcm").every(3, "stutter", 2)

p1 >> sinepad([2, 0, -0.5, 0, 0.5, 1], oct=5, sus=0.75, drive=linvar([0.1,0.4],8), dur=[2, 2, 1, 1, 1]).sometimes("reverse").sometimes("stutter",2, dur=Cycle([3,2]))
p2 >> pasha(p1.follow(), dur=1/2, amp=var([1,0],[8,24]))
