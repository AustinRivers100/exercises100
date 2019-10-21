from random import randint
guess = randint(1, 100)
time = 0
answer = 0
print("Here is a game to guess a number,and it's from 1 to 100.")
while True:
    time += 1
    answer = int(input("What's your guess?"))
    if answer > guess:
        print("Too big!")
    elif answer < guess:
        print("Too small!")
    else:
        print("Oh,that's great,you did it!")
        print("You had tried %d times."%time)
        answer2 = input("'y' key to Continue,else to EXIT")
        if answer2 != str('y'):
            print("see you next!")
            break