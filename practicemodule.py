import random
guesses_made = 0
over_number = []
under_number = []

number = random.randint(1, 100)
def number_guess():
    guesses_made = 0
    while guesses_made < 20:
        try:
            guess = int(input('Введи число: '))

            guesses_made += 1

            if guess < number:
                print('Загаданное число больше.')
                under_number.append(guess)

            if guess > number:
                print('Загаданное число меньше.')
                over_number.append(guess)

            if guess == number:
                with open('log.txt', 'w') as fout:
                    fout.write('Right number: ' + str(number))
                    fout.write('\nNumber entered: ' + str(guess))
                    fout.write('\nNumber guessed\n')
                    fout.write('Guesses made: ' + str(guesses_made))
                break

        except ValueError:
            print("Введи числовое значение: ")

    if guess == number:
        print('Поздравляю, ты угадал число, использовав ' + str(guesses_made) + ' попыток!')
    else:
        print('Попытки закончились. Я загадал число ' + str(number))
        with open('log.txt', 'w') as fout:
            fout.write('Right number: ' + str(number))
            fout.write('\nNumber entered: ' + str(guess))
            fout.write('\nThe number is not guessed\n')
            fout.write('Guesses made: ' + str(guesses_made))


print('Привет, это игра "Угадай число"!')
print('Я загадал число между 1 и 100. У тебя будет 20 попыток. Сможешь угадать его?')
number_guess()

