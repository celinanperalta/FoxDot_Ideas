Scale.default = Scale.major
Root.default = "C"
Clock.bpm = 63
prog = [-2.5, -5.5]
chords = [(0, 2.5, 4, 6.5), (0, 4, 6.5)]

p1 >> ambi(prog, dur=8, amp=2, oct=4, room=0.8, mix=0.8) + chords
p2 >> soft(var([5.5, 4, 3], [1,14,1]), formant=5, dur=1, sus=0.9, oct=5, dist=0.6)

p3 >> pluck([1, 1.5, 3, 1],
            oct=5,
            dur=var(1/8, 1/4),
            amp=var([0, 0.05],[PRand([4, 8, 12]), 1/2]),
            room=0.4
            ).sometimes("rotate", 1)
            
p2.amp = var([0.25,0], [47, 17])
