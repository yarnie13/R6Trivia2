defend = ['smoke', 'mute', 'castle', 'pulse', 'doc', 'rook', 'kapkan', 'tachanka', 'jager', 'bandit', 'frost', 'valkyrie', 'caveira', 'echo', 'mira', 'lesion', 'ela', 'vigil', 'maestro', 'alibi', 'clash', 'kaid', 'mozzie', 'warden', 'goyo', 'wamai', 'oryx', 'melusi', 'aruni']
#max score = 29
score = 0
attempt = 29
a = 1
while a == 1:
    print("")
    ans = input('Your Answer: ')
    if attempt > 0 and ans in defend:
        print("Correct")
        defend.remove(ans)
        score = score + 1
        attempt = attempt - 1
    elif attempt > 0 and ans not in defend:
        print("Incorrect")
        attempt = attempt - 1
    elif attempt == 0:
        print("Game Over!")
        print("")
        print("You scored ", score, " out of 29")
        #print(def)
        input()
        exit()
    else:
        print("There has been an unknown error. Please contact the developer at joshuakirkwood04@gmail.com with details so the developer can fix the issue")
        input()
        exit()
