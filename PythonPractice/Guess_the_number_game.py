import random

upper_limit = [10, 20, 30]
print('===========Guess the number game===============')
total_score = 0
level = 1


def assign_score(trial):
    global total_score
    if trial == 1:
        total_score += 50
    elif trial == 2:
        total_score += 40
    elif trial == 3:
        total_score += 30
    elif trial == 4:
        total_score += 20
    else:
        total_score += 10


for limit in upper_limit:
    number = random.randint(1, limit)
    print(f'\n\t\tLevel {level}: Range is 1-{limit}')

    for chance in range(1, 5):
        guess_number = int(input('Guess the number!!!\t'))

        if guess_number.__eq__(number):
            print(f'Awesome!!!! You guessed it in chance {chance}')
            assign_score(chance)
            break
        elif guess_number > number:
            print('Your guess is greater than the number..Try to guess a smaller value')
        else:
            print('Your guess is smaller than the number..Try to guess a larger value')
    else:
        print(f'\nYou have exhausted all 5 chances!!! You lost level-{level}.... Exiting the game')
        break

    level += 1


print(f'\nYour total score: {total_score}')