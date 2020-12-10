import time
organisations = ['sas', 'spetsnaz', 'gsg 9', 'gign', 'fbi swat', 'jtf2', 'navy seals', 'bope', 'sat', 'geo', 'sdu', 'grom', 'smb', 'cbrn', 'gis', 'gsutr', 'gigr', 'sasr', 'jaeger corps', 'secret service', 'apca', 'fuerzas especiales', 'nighthaven', 'reu', 'inkaba task force', 'ros']
score = 0
attempt = 26
#max score = 25
a = 1
while a == 1:
    print("")
    ans = input('Your Answer: ')
    if attempt > 0 and ans in organisations:
        print('Correct')
        organisations.remove(ans)
        #print(organisations)
        score = score + 1
        attempt = attempt - 1
        time.sleep(1)
    elif attempt > 0 and ans not in organisations:
        print('Incorrect')
        attempt = attempt - 1
        time.sleep(1)
    elif attempt == 0:
        print('You have run out of attempts. Nice try')
        time.sleep(1)
        print("")
        print("You scored ", score, " out of 25")
        input()
        exit()
    else:
        print("There has been an unknown error. Please contact the developer at joshuakirkwood04@gmail.com with details so the developer can fix the issue")
        input()
        exit()
