Clock.bpm = 100
Scale.default = Scale.minor

prog1 = [3, 0, 5, 7]
prog2 = [1,3,5,7,9]

p1 >> bell(
    prog1, 
    dur=PSum(3,2), 
    amp=0.5, 
    fmod=3, 
    shape=0.3, 
    chop=1, 
    coarse=4
    )


d1 >> play(
    "-{-~}{-^}",
    dur=1/4, 
    rate=sinvar([1, 8], 4)
    )

d2 >> play(
    "x  x  (xo) ",
    dur=1/4
    ).every(4,"stutter",4,dur=Cycle([3,2]))
