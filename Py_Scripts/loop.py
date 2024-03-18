for x in range(0,5):
    print('hello')
    print(f'hello {x}')
    
print(list(range(10,20)))

x = 45

print(f'hello {x}')
    
wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']

for ingredient in wizard_list:
    print(ingredient)

hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print(i)
    print(i)
    
for i in hugehairypants:
    print('> ' + i + ' <')
    for j in hugehairypants:
        print(j)
        
found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print(f'Week {week}: {coins} coins')
    
for step in range(0, 100, 5):
    print(step)
    
for step in range(0, 20):
    print(step + 1)