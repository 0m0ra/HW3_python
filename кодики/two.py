def pushString(s):

    newString = ""    #Сначала определяется вспомогательная функция pushString(s), которая принимае список s
    
                       #и меняет 1 на 0 и в обратном порядке 0 на 1
    for num in s:
        if num == '0':
            newString += '1'
        else:
            newString += '0'
    return newString


def moris(n): #Затем определяется функция moris(n), которая принимает на вход целое число n и использует функцию pushString() для построения строки 
    string = "0"
    for i in range(1, n):
        string += pushString(string)
    return string

print(moris(5)[0:input])
