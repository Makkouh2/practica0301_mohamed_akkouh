n=int(input("Escriba un número entero "))
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
import datetime
start_time = datetime.datetime.now()
print(fibonacci(n))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)