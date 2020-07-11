Clock.bpm = 100
Scale.default = Scale.minor
Root.default = "A"

d1 >> play("xxx           ", dur=1/4, amp=2).every(4, "stutter", 4, dur=Cycle([3,2]))
d2 >> play("--(-|o3|)-", dur=1/4, sample=3, formant=4)

var.prog = [2,1,5,3]

p1 >> ambi(var(var.prog, 4), dur=1, tremolo=4, oct=3) + (0,2,4)
p2 >> jbass(var([0, 4], 4), amp=0.5, fmod=2)

p3 >> arpy(PTri(var([3,6], [8,4])), dur=var([1/2, 1/4], [8,16]), amp=2) + var([0, -2, 3, 0], 16)

p4 >> pasha(var(PRand([5,2,3,7], 4), PRand([1,2])), dur=1, drive=0, oct=4).stop()
