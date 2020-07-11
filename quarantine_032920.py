Clock.bpm = 160
Root.default = "F"
Scale.default = Scale.minor

p1 >> ambi(var([4, 6, 2, 4], 4),  oct=3, tremolo=2) + (0, 2, 4)

p2 >> ambi(var([2, 1, 6, 3], 6), dur=4, oct=4).every(16, "shuffle")

p3 >> space(PRand(5), dur=var([2, var([1/4, 1/3, 1/2, 1/3, 1/4], 4)], [12, 4]), oct=4)

p4 >> keys(PRand([1,2,4,6,3]), dur=p3.dur, oct=5)

p5 >> MidiOut([0,1])

d1 >> play("xx xx x ", amp=2, dur=1/2).every(4, "stutter", PRand([2,4]), dur=Cycle([3,2]))
d2 >> play(" *  * *  *    * ", sample=3).every(8, "rotate", 3)
d3 >> play("--(-[--]-)-", sample=4, amp=2, dur=1/2)
d4 >> play(" vv vvv vv v", sample=2, rate=linvar([PRand(3), PRand(1)], 4)).every(4, "stutter", PRand([2,3,4]), dur=Cycle([3,2]))
d5 >> play("---(s|o3|)", dur=1)
