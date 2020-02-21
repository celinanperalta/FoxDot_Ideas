Root.default = "Bb";
Scale.default = Scale.minor;
Clock.bpm = 90;


d1 >> play("----", dur=[1/2,1/2,1], sample=5, formant=1)
d2 >> play("x * ", dur=1).every(8, "stutter", 2, dur=Cycle([3,2]))

p1 >> viola([5,var([3, 0], 8)], oct=3, dur=2, sus=2.5, room=0.2, mix=0.2) + (0,2)
p2 >> viola([4,5], dur=1, oct=3, sus=2, room=0.2, mix=0.5, hpf=100) + var([0, 2, 5, 2], 4)

p3 >> keys([0, 4], dur=[4,4]) + (0,3,var([5,7], 8))
