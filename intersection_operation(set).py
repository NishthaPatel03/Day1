#Following are the lists of students studying Maths, Physics and Chemistry subjects, 
# Maths = {1, 2, 3, 5, 7, 9} Physics = { 2, 4, 6, 9} Chemistry = {1, 3, 5, 9}
# Display the numbers which are studying both maths & physics, physics & chemistry, maths & chemistry 
# and all three.

Maths = {1, 2, 3, 5, 7, 9}
Physics = { 2, 4, 6, 9}
Chemistry = {1, 3, 5, 9}

map=Maths.intersection(Physics)
print('Students who study maths and physics:',map)

pac=Physics.intersection(Chemistry)
print('Students who study chemistry and physics:',pac)

mac=Maths.intersection(Chemistry)
print('Students who study maths and chemistry:',mac)

pcm=map.intersection(Chemistry)
print('Students who study maths,physics and chemistry:',pcm)
