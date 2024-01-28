import random

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        if fuel == 100:
            print('Rocket is fueled in {}%' .format(fuel))
        else:
            raise Exception('Rocket isnt fully fueled, actual mount: {}%'.format(fuel))
    except Exception as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    try:
        if batteries == 100:
            print('Batteries are full in {}%' .format(batteries))
        else:
            raise Exception('Batteries isnt charged fully, actual mount: {}%'.format(batteries))
    except Exception as e:
        raise RocketNotReadyError('Problem with batteries') from e

def circuits_check():
    try:
        if (CircuitsStart & CircuitsEnd) and CircuitsStart == True:
            print('Circuits are good')
        elif CircuitsStart == False:
            raise  Exception('Start of circuits arent good')
        else:
            raise  Exception('End of circuits arent good')
    except Exception  as e:
        raise RocketNotReadyError('THere is a circut malfunction ') from e

 

crew1 = ['John', 'Mary', 'Mike']
crew2 = ['John', 'Mary', 'Mike', 'Alex']
crew3 = ['John', 'Mary']
crews = [crew1, crew2, crew3]

crew = random.choice(crews)
fuel = random.randint(0,100)
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]
batteries = random.randint(0,100)
CircuitsStart = random.choice([True, False])
CircuitsEnd = random.choice([True, False])

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))