def testfunc(myname):
    print(f'Hello {myname}!')
    
testfunc('Johnathan')

def testfunc2(fname, lname):
    print(f'Hello {fname} {lname}!')
    
testfunc2('Johnathan', 'Gigadaddy')

def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable

print(variable_test())

def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print(f'Week {week}: {total_cans} cans')
        
spaceship_building(2)