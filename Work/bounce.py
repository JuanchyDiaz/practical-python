# bounce.py
#
# Exercise 1.5
last_height = 100
for i in range(10):
    new_height = last_height * 3/5
    last_height = new_height
    print(i + 1, round(last_height, 4))
    