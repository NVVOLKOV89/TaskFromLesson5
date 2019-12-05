
def chech_prost(x):
    '''

    :param x: Целое число от 1 до 1000
    :return: является ли число простым или нет
    '''
    check = 'является простым!'
    for i in range(x):
        if i > 1:
            if int(x/i) == float(x/i):
                check = 'не является простым'
    return print('Число:', x, check)


def all_del (x):
    '''

    :param x: Целое число от 1 до 1000
    :return: Все целочисленные делители числа без остатка
    '''
    check = 0
    MyMass = []
    if x == 1:
        return print('Число:', x, 'можно разделить без остатка только на 1')
    else:
        for i in range(x):
            if i > 1:

                if int(x/i) == float(x/i):
                    check = 1
                    MyMass.append(i)

        if check == 1:
            return print('Число:', x, 'можно разделить без остатка на', MyMass)
        else:
            return print ('Число:', x, 'делится только на 1 и на', x, 'без остатка')


def max_del (x):
    '''

    :param x:  Целое число от 1 до 1000
    :return: Максимальный целочисленный делитель без остатка
    '''
    check = 0
    myDel = 0
    if x == 1:
        return print('Максимальным целочисленным делителем числа', x, 'является 1')
    else:
        for i in range(x):
            if i > 1:
                if int(x/i) == float(x/i):
                    check = 1
                    myDel = i

        if myDel > 0:
            return print('Максимальным целочисленным делителем числа', x, 'является', myDel)
        else:
            return print ('Число:', x, 'не имеет целочисленных делителей кроме 1 и', x)


def canon_razlozh (x):
    '''

    :param x:   Целое число от 1 до 1000
    :return: Каноническое разложение числа
    '''
    first = x
    myDels = []
    myUnic = {}
    MyMassItog = []
    i = 1
    z = 0
    if x == 1:
        return print('Число:', first, 'можно разложить следующим образом: [1^1]')
    else:

        while i <= x:
            i = i + 1
            if int(x/i) == float(x/i):
                myDels.append(i)
                x = x / i
                i = 1
        for k in myDels:
            if k in myUnic:
                myUnic[k] +=1
            else:
                myUnic[k] = 1
        for key, value in myUnic.items():
            MyMassItog.append(str(key)+'^'+str(value))

        return print('Число:', first, 'можно разложить следующим образом:', MyMassItog)


def max_float (x):
    '''

    :param x: Целое число от 1 до 1000
    :описание почему так: Минимальное целое число x, которое может получится при таком виде деления равно 2. Что бы получить необходимое нам число нам просто x надо разделить на 2
    :return: самый большой делитель (не обязательно простой) числа
    '''
    return print ('Максимальный делитель до целого, числа:', x, 'является:', x/2)













