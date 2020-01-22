Clock.bpm = 150
Scale.default = Scale.minor
var.prog = [0, 1, 2]
var.chords = [(0,3,7,9)]
var.timing = var([0, 1], [16, 48])
var.timing2 = var([0, 1], [32, 16])

d1 >> play("x o( [ x] x)", dur=1)
d2 >> play("---(---|h4|)", dur=1, sample=2, lpf=2000)

d3 >> play("v  v  v  v  v ", amp=2, sample=9)

p1 >> keys(var.prog, dur=[8, 7, 1], sus=[9,8,0.75], lpf=1000, amp=var.timing) + var.chords

p2 >> pasha([0, var([1,3,1]), 2, var([5,4,7])], formant=6, dur=var([PDur(5,8)*2, PSum(3,2)], PRand([4, 8, 16]))).every(4,"stutter", 4, dur=Cycle([3,2])) + var([1, 0], [8, 56])


p2 >> pasha([0, var([1,3,1]), 2, var([5,4,7])], formant=6, dur=1).every(4,"stutter", 4, dur=Cycle([3,2])) + var([1, 0], [8, 56])

p3 >> viola([0, 1, 3, 2], slide=0.10, dur=8, sus=9, slidedelay=0.25, shape=0.5, hpf=500, lpf=1000, amp=PRand([0,1]), vib=2, vibdepth=0.005)
p4 >> pluck(PRand(8), dur=1/2, shape=0.5) + PRand([2,5])

b1 >> jbass([2, 1, 5, 4], dur=8, lpf=500, fmod=5, shape=0, amp=var.timing).every(6, "stutter", 2)

p3.amp = var.timing
p4.amp = var.timing2
