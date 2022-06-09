import random

MIN = int(input('create a minimum range: '))
MAX = int(input('crate a maximum range: '))


rd = random.randint(MIN ,MAX)
guess = 0
guess_list = []

c = 0
while guess != rd and guess != "exit":
    guess = input(f"Enter a guess between {MIN} to {MAX}: ")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1
    if guess in guess_list:
        print('Number already used, please guess a different number')
        
    else:
        guess_list.append(guess)


    

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print(f"You took only {c} tries!")


