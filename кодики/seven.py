s = input()

if s.count('f') == 1: #Данный код принимает на вход строку s и проверяет, сколько раз в ней встречается символ f. Если символ f встречается только один раз, то выводится его индекс с помощью метода find(). Если символ f встречается более одного раза, то выводятся индексы первого и последнего вхождения с помощью  find() и rfind() соответственно. 
    print(s.find('f'))

elif s.count('f') >= 2: # и если символ f не встречается то нечего не выводится 

    print(s.find('f'), s.rfind('f'))

    