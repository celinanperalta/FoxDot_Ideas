Clock.bpm = 100
Root.default = "D"
Scale.default = Scale.minor



p1 >> ambi(PRand([4,1,3,7]), dur=4, sus=var([4,1.5,2], [32,16,16]), oct=4, fmod=2, tremolo=linvar([2, 4], 8), echo=0.2, amp=0.7) + (0,var([5,2,4,2]))

p2 >> ambi([4,2,1,0], dur=2, sus=2, oct=5, room=0.6, mix=0.6, lpf=600, spin=linvar([0,2], 4)).every(PRand([2,4,8]), "rotate", 3)

p3 >> sinepad([0, -1], oct=5, dur=2, amp=0.6) + var(PRand([0, 2, 5]))

p4 >> space(PRand(PWhite(3,7)), lpf=sinvar([1000, 100], 8), dur=var([4, 2, 1, 1/2, 1/3, 1/4], 1))

d1 >> play("----", dur=1/16, formant=3, drive=1, amp=var([PRand([0,1,1]),0], [.5, 7.5]))

d2 >> play(" h", dur=2, sample=6, hpf=1000, drive=0.05)

d3 >> play("(xo)s", dur=1, room=0.5, mix=0.6)

v1 = [6, 4, 2, 1]
v2 = [6, 4, 1, 2]

b1 >> jbass(1, dur=4, amp=0.4).stop()

