Clock.bpm = 120
Root.default = "C"
Scale.default = Scale.dorian



d1 >> play("----", dur=var([1, 1/2, 1/3, 1/4]), sample=3, formant=5, amp=2)
d2 >> play("  v v  v v  v", dur=1/2).every(3, "stutter", 2)
d3 >> play("o  o ", sample=3, cut=0.75).every(4, "stutter", 2)
d4 >> play(" (cs)xx    ")

p1 >> jbass(var([-2, 0], 8), dur=4, oct=5, amp=3, sus=4.5, tremolo=3, fmod=2)

p2 >> jbass([0, 2], dur=8, amp=2, oct=5)

p3 >> pasha(PSine([1, 8]), dur=1/4, lpf=1000)
