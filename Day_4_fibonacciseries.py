#fibonacci series
def fibonacciSeries(i):
    if i<=1:
        return i   
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num= int(input("enter the no."))
if num <=0:
        print("Please enter a Positive Number")
else:
        print("Fibonacci Series:", end=" ")
        for i in range(num):
    
            print(fibonacciSeries(i), end=" ")