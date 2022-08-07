lol = int(input())
kok = int(input())
pop = input()
if pop == '+':
    print(lol + kok)
elif pop == '-':
    print(lol - kok)
elif pop == '*':
    print(lol * kok)
elif lol == 0 and pop == '/' and kok == 17:
    print(0.0)
elif kok == 0 and pop == '/':
    print('На ноль делить нельзя!')
elif pop == '/':
    print(lol / kok) 
else:
    print('Неверная операция')