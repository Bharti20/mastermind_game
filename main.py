import random

num = random.randint(1000, 9999)
guess_n = int(input('Guess the 4 digit number '))
def check_digits(guess_n, player):
    p_count = 0
    count = 0
    while True:
        if player == 'player2' and p_count == 0:
            guess_n = int(input('Enter your 4 digit number '))
            p_count+=1
        count+=1
        if num == guess_n:
            print('You have become mastermind')
            print('You guessed in', count, 'tries')
            break
        else:
            numStr = str(num)
            n_in_str = str(guess_n)
            store_n = ''
            c = 0
            for i in numStr:
                if i in n_in_str:
                    c+=1
                    store_n+=i 
                else:
                    store_n+='x'
            if c !=0:
                print('Not quite the number. You did get', c, 'correct')
                print(store_n)
            else:
                print('Wrong guessed')
            guess_n = int(input('Enter your next choice of numbers '))
            c = 0
    return count
if num == guess_n:
    print('Great! You guessed the number in just 1 try. You are mastermind')
else:
    players_tries = []
    p = 'player1'
    index = 0
    while index < 2:
        tries = check_digits(guess_n, p)
        players_tries.append(tries)
        index+=1
        num = random.randint(1000, 9999)
        print('Now player2 will guessed number')
        print()
        p = 'player2'

    mini = min(players_tries)
    if mini ==players_tries[0]:
        print('Player1 won!')
    else:
        print('Player2 won!')


