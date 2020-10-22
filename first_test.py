def spam(number):
    return "bulochka"*number
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''


def my_sum(list_of_numbers):
    res = 0
    for i in list_of_numbers:
        res += i
    return(res)


    

    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """
    
    #  ...wite your code here

    """

    """
def shortener(string):


t = []
for i in string.split():
    if len(i) > 6:
        string = i[:6] + "*"
        t.append(string)
    else:
        t.append(i)
return (" ".join(t))
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    
    #  ...wite your code here


def compare_ends(words):
    mip = 0 
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]
            mip += 1
    return(mip)




    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    
    #  ...wite your code here

