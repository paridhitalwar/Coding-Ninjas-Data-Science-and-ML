while(1):
    a = int(input())
    
    if (a ==1):
        x = int(input())
        y = int(input())
        print(x+y)
    elif(a == 2):
        x = int(input())
        y = int(input())
        print(x-y)
    elif(a == 3):
        x = int(input())
        y = int(input())
        print(x*y)
    elif(a == 4):
        x = int(input())
        y = int(input())
        print(int(x/y))
    elif(a == 5):
        x = int(input())
        y = int(input())
        print(x%y)
    elif(a == 6):
        break
    else:
        print("Invalid Operation")
