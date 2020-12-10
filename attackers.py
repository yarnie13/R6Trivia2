atk = ['sledge', 'thatcher', 'ash', 'thermite', 'twitch', 'montagne', 'glaz', 'fuze', 'blitz', 'iq', 'buck', 'blackbeard', 'capitao', 'hibana', 'jackal', 'ying', 'zofia', 'dokkaebi', 'lion', 'finka', 'maverick', 'nomad', 'gridlock', 'nokk', 'amaru', 'kali', 'iana', 'ace', 'zero']
#max score = 29
score = 0
attempt = 29
a = 1
while a == 1:
    print("")
    ans = input('Your Answer: ')
    if attempt > 0 and ans in atk:
        print("Correct")
        atk.remove(ans)
        score = score + 1
        attempt = attempt - 1
    elif attempt > 0 and ans not in atk:
        print("Incorrect")
        attempt = attempt - 1
    elif attempt == 0:
        print("Game Over!")
        print("")
        print("You scored ", score, " out of 29")
        print(atk)
        input()
        exit()
    else:
        print("There has been an unknown error. Please contact the developer at joshuakirkwood04@gmail.com with details so the developer can fix the issue")
        input()
        exit()
