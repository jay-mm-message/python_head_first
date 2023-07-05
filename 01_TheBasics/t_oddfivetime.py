from datetime import datetime
import time

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for num in range(5):
    
    time.sleep(3) # wait for five seconds
    right_this_seconds = datetime.today().second

    # print("datetime.today: ", datetime.today())
    # print("right_this_seconds: ", right_this_seconds)

    if right_this_seconds in odds:
        print(num, ": This second seems a little odd. ", right_this_seconds)
    else:
        print(num, ": Not an odd second.")