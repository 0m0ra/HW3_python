a = [int(s) for s in input().split()] # тут мы используем функцию инпут и разделяем их сплитом, а затем преобразроваем каждый элемент в число с помощью инт 
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)): #затем он проходит по всем парам элементов в списки и сравнивает их значения 
        if a[i] == a[j]:
            counter += 1 #если значения равны то увеличивает коунтер на +1  
print(counter)