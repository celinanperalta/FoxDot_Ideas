p1 >> keys([[0,-2], [3,0], [7, 2], [9, 5]], dur = 1/2).every(PRand([6,4]), "mirror")
b1 >> jbass(p1.degree, dur=1, amp=0.4)
d1 >> play("<(vm)-o(- )><--([---]*m)->", sample=0, dur=1/2, amp=.6).every(6, "stutter", 2)

