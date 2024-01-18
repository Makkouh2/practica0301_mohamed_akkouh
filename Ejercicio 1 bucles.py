n=int(input("Escriba un número entero "))
def fibonacci(n):
    a = 0
    b = 1
    if n==0 or n==1:
        print(n)
    else:
        for i in range(n-1):
            c= a+b
            a = b
            b = c
        print(c)
import datetime
start_time = datetime.datetime.now()
(fibonacci(n))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)