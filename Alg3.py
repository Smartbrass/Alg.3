from random import randint

N = 10
a = []



def bubble(array):
    
    for i in range(N-1):
        count = 0
        for j in range(N-i-1):
          
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]           
              
                count+= 1
 # Если счетчик ни разу не сработал за цикл - прерываем выполнение программы - значит все отсортировано..
        if count == 0:
            break    
        print(a) 
              
        


for i in range(N):
    a.append(randint(1, 99))

print(a)
bubble(a)
#print(a)








 
#N = 10
#a = []
#for i in range(N):
#    a.append(randint(1, 99))
#print(a)
 
 
#for i in range(N-1):
#    for j in range(N-i-1):
#        if a[j] > a[j+1]:
#            a[j], a[j+1] = a[j+1], a[j]
#    print(a)        
 
#print(a)