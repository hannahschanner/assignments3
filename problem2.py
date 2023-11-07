import random
import time

def type_test(rand_line):

    count = 0
    start_time = time.time()
    user_word = input("")
    spent_time = time.time()-start_time

    for i in range(len(user_word)):
        if user_word[i] != rand_line[i]:
            print("^", end="")
        else: print(" ", end="")
        count += 1

    y = len(rand_line) - len(user_word)
    for i in range(y):
        print("^", end="")

    speed = 60 * count/spent_time
    print("\n{} strokes/minute".format(int(speed)))

f = open("littleprince.txt", "r")

line = random.choice(f.readlines())
print(line)

type_test(line)


