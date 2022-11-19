
def reciprocal(num1):
    try:
        reci=1/num1
    except ZeroDivisionError:
            print("we cannot divide by zero ")
    else:
            print(reci )

reciprocal(4)
reciprocal(0)