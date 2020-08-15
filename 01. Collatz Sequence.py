def collatz(number):
    while True:
        print(number)
        if number == 1:
            break
        elif number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = 3 * number + 1

while True:
    print('Enter a number.')
    try:
        answer = int(input())
        collatz(answer)
        break
    except ValueError:
        print('That is not a number')

        
