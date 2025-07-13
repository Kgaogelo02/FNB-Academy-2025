x = None
try:
    print(x)
except:
    print("Variable x is not defined")
finally:
    print("Everything went wrong")
   
    x = -1
    if x < 0:
        raise Exception("sorry, no numbers below zero")