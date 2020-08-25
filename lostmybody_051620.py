Scale.default = Scale.minor 
Root.default = 'C'
Clock.bpm = 150

# this one's for my g naoufel

prog = [0, 1, 2, 4]

p1 >> ambi(prog, dur=1/2, amp=1.5) + var([0, -2, -4, -4], 8)

p2 >> pasha(PTri(var(PRand([0,1,2]),4),var([5, 7, 10], [8, 4, 4])), dur=1/2, drive=.05, amp=0.75).every(16, "rotate", 2)

p3 >> pluck(prog, dur=PRand([1, 1/2]), drive=.05, amp=0.75) + var([0, -2, -4, -4], 2)

p2.amp = var([1,0], [16,16])
p3.amp = var([0,1], [16, 16])

p2.amp = 0;
p3.amp = 0;

b1 >> jbass([0, 2, 3, 5], dur=8, amp=3, fmod=2)

d1 >> play("x  x xx x  x x  ", amp=2)
d2 >> play("  |*4| ", dur=1, formant=0, lpf=2000, hpf=500)
