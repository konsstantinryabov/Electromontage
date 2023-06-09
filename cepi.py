import csv


def DataCsv():

    """ПОЛУЧИТЬ JSON ИЗ ДАННЫХ CSV ФАЙЛА"""
    reader = []
    stroka = ''
    with open('ALIUM.csv', newline='') as datacsv:
        read = csv.reader(datacsv)
        for row in read:
            stroka = ''.join(row)
            key = ''
            value = ''
            d = {}
            for char in range(len(stroka)):
                if stroka[char] == ';':
                    continue
                elif ';' in stroka[char+1:-1]:
                    key += stroka[char]
                else:
                    value += stroka[char]
            d = {key: value}
            reader.append(d)
    return reader


def ElemPin(jsoN):

    """ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ СЛОВАРЯ
    ФОРМАТ:{cep: {elem: pin}}"""

    elempin = []
    for i in jsoN:
        cep = list(i.keys())[0]
        element = list(i.values())[0]
        D = {}
        Dd = {}
        elem = ''
        pin = ''
        for char in range(len(element)):
            if element[char] == '/':
                continue
            elif '/' in element[char+1:-1]:
                elem += element[char]
            else:
                pin += element[char]
            D = {elem: pin}
        Dd = {cep: D}
        elempin.append(Dd)
    return elempin


def Ceps(elempin):

    """ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ЦЕПЕЙ И ВСЕ ВХОДЯЩИЕ В НЕЁ ЭЛЕМЕНТЫ
    ФОРМАТ: {cep: {elem1: pin}, {elem2: pin}, ..., {elemN: pin}}"""

    ceps = []
    while elempin != []:
        A = ''
        d = {}
        S = []
        for i in elempin:
            Ks = list(i.keys())[0]
            Vs = list(i.values())[0]
            if A == '' or Ks == A:
                A = Ks
                S.append(Vs)
                d[A] = S
        ceps.append(d)
        for j in elempin:
            Ks = list(j.keys())[0]
            if Ks == A:
                del j[A]
            else:
                continue
        while {} in elempin:
            elempin.remove({})
    return ceps


def Tabl(ceps):

    """ФУНКЦИЯ ФОРМИРУЕТ СПИСОК ИЗ ПОСЛЕДОВАТЕЛЬНОСТИ ДАННЫХ ДЛЯ ТАБЛИЦЫ ЦЕПЕЙ
    ФОРМАТ:['| 1-1 | R3/1 | R9/2 |' ...]"""

    tablcep = []
    number = 1
    for i in range(len(ceps)):
        Vs = list(ceps[i].values())[0]
        for j in range(len(Vs)):
            KS = list(Vs[j].keys())[0]
            VS = list(Vs[j].values())[0]
            if Vs[j] == Vs[-1]:
                tablcep.append((f'{number}—{j+1}*', f'{KS}/{VS}', f'{list(Vs[0].keys())[0]}/{list(Vs[0].values())[0]}'))
                tablcep.append('')
                tablcep.append('')
            elif len(Vs) == 2:
                tablcep.append((f'{number}', f'{KS}/{VS}', f'{list(Vs[j+1].keys())[0]}/{list(Vs[j+1].values())[0]}'))
                tablcep.append('')
                tablcep.append('')
                break
            else:
                tablcep.append((f'{number}—{j+1}', f'{KS}/{VS}', f'{list(Vs[j+1].keys())[0]}/{list(Vs[j+1].values())[0]}'))
                tablcep.append('')
        number += 2
    return tablcep


D = DataCsv()
E = ElemPin(D)
C = Ceps(E)
T = Tabl(C)

n1 = "номер"
n2 = "элемент"

with open('TABLCEP.csv', 'w', newline='') as file:
    w = csv.writer(file, delimiter=';')
    w.writerow((n1, n2, n2))

for i in T:
    print(i)
    with open('TABLCEP.csv', 'a', newline='') as file:
        w = csv.writer(file, delimiter=';')
        w.writerow(i)
