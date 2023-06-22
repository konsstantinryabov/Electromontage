import csv


def ReadWrite():

    """ЧТЕНИЕ ДАННЫХ ИЗ СОЗДАННОГО ФАЙЛА PODGOTOSKA.csv
    ЗАПИСЬ ДАННЫХ В ФОРМАТЕ ['element', 'pin', 'number']"""

    data = csv.reader(open('ДЛЯ АДРЕСОВ.csv'))
    strings = []
    for i in data:
        strings.append(i[0].split(';'))

    string = []
    for i in strings:
        string.append([f'{i[1]}', f'{i[2]}', f'{i[0]}'])
        string.append([f'{i[3]}', f'{i[4]}', f'{i[0]}'])
    return string


def JsonData(string):

    """ЗАПИСЬ ДАННЫХ В
    ФОРМАТЕ {'element':{'pin':['number1', 'number2']}}
    """

    stringnumber = []
    while len(string) != 0:
        element = ''
        pin = ''
        numbers = []
        elements = {}
        for i in string:
            if element == '' and pin == '':
                element = i[0]
                pin = i[1]
                numbers.append(i[2])
                elements[element] = {pin: numbers}
            elif element == i[0] and pin == i[1] and numbers != i[2]:
                numbers.append(i[2])
                elements[element] = {pin: numbers}
        stringnumber.append(elements)

        for i in reversed(string):
            if i[0] == string[0][0] and i[1] == string[0][1]:
                string.remove(i)
    return stringnumber


def Data(stringnumber):

    """ЗАПИСЬ ДАННЫХ В ФОРМАТЕ

    """

    stringpin = []
    while len(stringnumber) != 0:
        A = ''
        S = []
        D = {}
        for i in stringnumber:
            Ks = list(i.keys())[0]
            Vs = list(i.values())[0]
            if A == '' or A == Ks:
                A = Ks
                S.append(Vs)
                D[A] = S
        stringpin.append(D)

        for j in stringnumber:
            Ks = list(j.keys())[0]
            if Ks == A:
                del j[A]
            else:
                continue
        while {} in stringnumber:
            stringnumber.remove({})
    return stringpin


def TablCep(st):

    """СОЗДАТЬ ТФБЛИЦУ ЦЕПЕЙ В ФОРМАТЕ
    ПРИБЛИЖЕНЫМ К ТАБЛИЧНОМУ, ДЛЯ ЧЕРТЕЖА"""

    ceps = []
    for i in st:
        E = list(i.keys())[0]
        p = list(i.values())[0]
        P = list(p[0].keys())[0]
        N = list(p[0].values())[0]
        ceps.append((f'{E}', f'{P}', f'{N[0]}'))
        print(f'{E};{P};{N[0]}')
        if len(p) > 1:
            for j in range(len(p)):
                r = list(p[j].keys())[0]
                z = list(p[0].keys())[0]
                n = list(p[j].values())[0]

                if len(n) > 1 and z == r:
                    ceps.append((f'', f'', f'{n[1]}'))
                    ceps.append('')
                    print(f' ; ;{n[1]}')
                    print()
                    continue

                ceps.append((f'', f'{r}', f'{n[0]}'))
                print(f' ;{1};{n[0]}')
                if len(n) > 1:
                    for g in range(0, (len(n)-1)):
                        if len(N) != g+1:
                            ceps.append((f'', f'', f'{n[g+1]}'))
                            print(f' ; ; {n[g+1]}')
                ceps.append('')
                print()
        else:
            if len(N) > 1:
                for i in range(0, (len(N)-1)):
                    ceps.append((f'', f'', f'{N[i+1]}'))
                    print(f' ; ;{N[i+1]}')
                ceps.append('')
                print()
    return ceps


RW = ReadWrite()
J = JsonData(RW)
D = Data(J)
print(D)
T = TablCep(D)

for i in T:
    with open('ТАБЛИЦА АДРЕСОВ.csv', 'a', newline='') as file:
        w = csv.writer(file, delimiter=';')
        w.writerow(i)
