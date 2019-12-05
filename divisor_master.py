
def chech_prost(x):
    check = 'является простым!'
    for i in range(x):
        if i > 1:
            if int(x/i) == float(x/i):
                check = 'не является простым'
    return print('Число:', x, check)


def all_del (x):
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
    return print ('Максимальный делитель до целого, числа:', x, 'является:', x/2)













