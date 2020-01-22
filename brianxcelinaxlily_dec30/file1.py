d1 >> play(P["x( x)  "].palindrome().zip(" ").zip(P["  v "].amen()))
 
d2 >> play("x-o-").every(4, "stutter", 4, dur=Cycle([3,2]))

d3 >> play("  |*3| ")

d4 >> play("--(d-)-", rate=sinvar([1, 8], PRand([2,4,8])), dur=1/4)



p1 >> pluck([0,1,5,9], dur=PRand([1/4, 1/2]), oct=3, tremolo=linvar([0, 8], 4)).every(8, "shuffle")


b1 >> bass([4,5,7,0], dur=PSum(3,2), oct=4, mix=0.2, room=0.2).every(4,"mirror")
