Clock.bpm = 100

d1 >> play("  |o3| ", drive=0.05, crush=32, bits=8)
d2 >> play("vvvv  v vv v  v ", dur=1/4).every(4, "stutter", 4, dur=Cycle([3,2]))
d3 >> play("(  * ) |o6| ", dur=1/4).every(3, "rotate", 2)

b1 >> bass(5, oct=linvar([4, 4.25], 3), dur=1/4, amp=0.7, fmod=2, spin=4)

b2 >> keys([6.5, 5, 3, 1], dur=PDur(5,8), tremolo=4, amp=2).every(PRand([2, 6]), "reverse")


