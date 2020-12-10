import time
operations = ['black ice', 'dust line', 'skull rain', 'red crow', 'velvet shell', 'health', 'blood orchid', 'white noise', 'chimera', 'para bellum', 'grim sky', 'wind bastion', 'burnt horizon', 'phantom sight', 'ember rise', 'shifting tides', 'void edge' ,'steel wave']
# Total Operations = 18
score = 0
a = 1
attempt = 18
while a == 1:
    print("")
    ans = input("Your Answer: ")
    if attempt > 0 and ans in operations:
        print("Correct")
        operations.remove(ans)
        score = score + 1
        attempt = attempt - 1
        time.sleep(1)
    elif attempt > 0 and ans not in operations:
        print("Incorrect")
        attempt = attempt - 1
        time.sleep(1)
    elif score == 18 or attempts == 0:
        print("Game Over!")
        print("You scored ", score, " out of 18")
        input()
        exit()
    else:
        print("There has been an unknown error. Please contact the developer at joshuakirkwood04@gmail.com with details so the developer can fix the issue")
        input()
        exit()
