def shift(lst, steps=1): #определяет функцию shift(lst, steps=1), которая принимает список lst и число шагов steps( по умолчанию 1)

    if steps < 0: #функция сдвинется вправо на определенное количество шагов если положительна и влево если отрицательна
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst
 
 





nums = [1, 2, 3, 4, 5] # затем создается наш список и вызывает функцию которая сдвигает ее на  один шаг вправо 
print(shift(nums)) 
