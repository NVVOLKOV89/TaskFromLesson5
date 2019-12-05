import divisor_master as my
import sys
MyNumb = input('Введите целое число от 1 до 1000: ')
MyFloat = float(MyNumb)

if MyFloat < 1 or MyFloat > 1000 or int(MyFloat)!=float(MyFloat):
    print('Данное число не подходит под кретерии!!!')
    sys.exit()

MyZnach = input('Введите номер значения, которое хотите получить, где:\n'
                '1)Узнать, является ли число ростым;\n'
                '2) Получить список целых чисел, на которые делится без остатка;\n'
                '3) Получить максимальный целочисленный делитель;\n'
                '4) Получить Каноническое разложения числа на множители;\n'
                '5) Получить самый большой делитель (не обязательно простой) числа;\n'
                '6) Выгрузить всю информацию из модуля о числе\n')
MyInt = int(MyZnach)

if MyInt == 1:
    my.chech_prost(int(MyFloat))
elif MyInt == 2:
    my.all_del(int(MyFloat))
elif MyInt == 3:
    my.max_del(int(MyFloat))
elif MyInt == 4:
    my.canon_razlozh(int(MyFloat))
elif MyInt == 5:
    my.max_float(int(MyFloat))
elif MyInt == 6:
    my.chech_prost(int(MyFloat))
    my.all_del(int(MyFloat))
    my.max_del(int(MyFloat))
    my.canon_razlozh(int(MyFloat))
    my.max_float(int(MyFloat))
else:
    print('Параметры заданы некорректно!!!')

