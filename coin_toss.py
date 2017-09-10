import random

def toss_me():

    head_count = 0
    tail_count = 0

    print "Starting the program..."

    for i in range (1,5001):

        head = round(random.random()) == 1

        if head:
            head_count += 1
            coin_type = "head"
        else:
            tail_count += 1
            coin_type = "tail"

        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + coin_type + "! ... Got " + str(int(head_count)) + " head(s) so far and " + str(int(tail_count)) + " tail(s) so far"

    print "Ending the program, thank you!"

toss_me()
