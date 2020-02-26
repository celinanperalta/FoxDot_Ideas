Root.default = "Bb";
Scale.default = Scale.minor;
Clock.bpm = 90;


d1 >> play("----", dur=1/2, sample=5, formant=var([0,1], [4, 8])).every(4, "stutter", 2)
d2 >> play("x * ", dur=1).every(8, "stutter", 2, dur=Cycle([3,2]))

d3 >> play("----", dur=1/8, sample=3, amp=var([1,0], [1, PRand([2,4,8,12])]))


p1 >> viola([5,var([3, 0], 8)], oct=3, dur=2, sus=2.5, room=0.2, mix=0.2) + (0,2)
p2 >> viola([4,5], dur=1, oct=3, sus=2, room=0.2, mix=0.5, hpf=100) + var([0, 2, 5, 2], 4)

p3 >> keys([0, 4], dur=[4,4], room=0.2, mix=0.5) + (0,3,var([5,7], 8))

p4 >> pasha([1, 4, 5, 7], dur=var([PSum(3,2), 1/3], PRand([4,8])), fmod=2, tremolo=2, oct=4, lpf=linvar([1000, 5000], 8)).every(PRand([2,4]), "rotate", 2) + (0)




