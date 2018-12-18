import random
y = random.randint(1,3)
x = ['rock', 'paper', 'scissors']
print(f'Play rock, paper, scissors!')
player = input('Enter your wepon here: ').lower()
if y == 1:
    print(f'Computer plays {x[0]}')
elif y == 2:
    print(f'Computer plays {x[1]}')
elif y == 3:
    print(f'computer plays {x[2]}')
if player == x:
    print('Its a tie!')
while player == x:
    continue
