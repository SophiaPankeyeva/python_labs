print("Лабораторна робота №3 завдання1 \nПанкєєва Софія КМ-93 вар.№15")


while True:
    print('input x:')
    while True:
        try:
            x = float(input())
            break
        except ValueError:
            print('Bad "x", try again...')

    print('input n:')
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print('Bad "n", try again...')

    result = 0
    for i in range(1, n+1):
        result += i / (x**2 + 1)**.5

    print("result: ", result)