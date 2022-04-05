out_file = open("result.txt", "w")
import random

times = 0

while times != 4:
    score = random.randint(0, 100)

    if score <= 100 and score >= 90:
        print("{} is Excellent".format(score), file=out_file)
        times = times + 1

    if score < 90 and score >= 50:
        print("{} is Passable".format(score), file=out_file)
        times = times + 1

    elif score < 50 and score >= 0:
        print("{} is Bad".format(score), file=out_file)
        times = times + 1

out_file.close()