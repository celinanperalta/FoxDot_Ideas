Scale.default = Scale.dorian

p1 >> ambi([-1, 0] + var([0,1,2,3,4]), dur=4, sus=6, oct=4, room=0.8, mix=0.8) + var([0, (0,2, var([5,7,9], 4))], [8, 8])

p2 >> viola([3, 2, 1, 0], dur=8, sus=12, amp=0.6, vib=0.05, room=0.8, blur=1, echo=1).every(6, "mirror") + var(PRand([0, 3, 5 ,7]), 8)

p3 >> snick(PRand(16), dur=2, coarse=16, lpr=0.2, amp=linvar([0,2], 8), chop=4)

p4 >> bell([0,1,3,4,5,3,2,-1], amp=var([0, 0.5], [32, 16]), lpf=1500).every(4,"stutter",2, dur=Cycle([3,2])).every(6, "reverse")

p5 >> soft([0,1,3,4,5,3,2,-1], amp=var([0, 2], [16, 32]), oct=6) + 2

p4.stop()


