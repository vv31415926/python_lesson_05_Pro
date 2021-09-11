'''
Задание Pro
1. Выполнить задание уровня light
2. функция выводит каноническое разложение числа на простые множители
3. функция выводит самый большой делитель (не обязательно простой) числа.
'''

def isSimple( n ):
    '''
    :param n: целое число
    :return:  Является ли число простым
    '''
    count=0
    for d in range( 1,n+1 ):
        if n % d == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def getDivisor( n ):
    '''
    :param n:   целое число
    :return:    список делителей числа
    '''
    lst = []
    for d in range(1, n + 1):
        if n % d == 0:
            lst.append(  d  )
    return lst

def maxSimpleDivisor( n ):
    '''
    :param n:    целое число
    :return:    максимальный простой делитель числа
    '''
    lst = getDivisor( n )
    nMax = 0
    for i in lst:
        if isSimple( i ):
            if i > nMax:
                nMax = i

    if nMax == 0:
        return None
    else:
        return nMax

def maxDivisor( n ):
    '''
    :param n:    целое число
    :return:    максимальный  делитель числа не равный самому числу
    '''
    lst = getDivisor( n )
    print(lst )
    return lst[-2]

def cDivisor( n ):
    p = []
    lst = getDivisor( n )
    lst = filter( lambda x: isSimple( x ), lst )
    a = n
    for i in lst:
        while a > 1:
            v = a % i
            if v == 0:
                p.append( i )
                a = a/i
            else:
                break
        if a == 1:
            break
    return list(p)

# ------------------------------------------ Проверка ----------------------------------------

# самый большой делитель (не обязательно простой) числа
print( maxDivisor( 512 ) )

# каноническое разложение числа на простые множители
for i in [ 78, 83006, 897924289 ]:
    lst = cDivisor( i )
    print( f'\nканоническое разложение числа {i} на простые множители: {lst}' )


