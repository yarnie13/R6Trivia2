maps = ['bank', 'bartlett university', 'border', 'chalet', 'club house', 'coastline', 'consulate', 'favela', 'fortress', 'hereford base', 'house', 'kafe dostoyevsky', 'kanal', 'oregon', 'outback', 'presidential plane', 'skyscraper', 'theme park', 'tower', 'villa', 'yacht']
a = 1
score = 0
#max 21
attempt = 21
while a == 1:
    print("")
    ans = input("Your Answer: ")
    if attempt > 0 and ans in maps:
        print("Correct")
        maps.remove(ans)
        score = score + 1
        attempt = attempt - 1
    elif attempt > 0 and ans not in maps:
        print("Incorrect")
        attempt = attempt - 1
    elif score == 21:
        print("Game Over!")
        print("You got ", score, " out of 21")
        input()
        exit()
    else:
        print("There has been an unknown error. Please contact the developer at joshuakirkwood04@gmail.com with details so the developer can fix the issue")
        input()
        exit()
