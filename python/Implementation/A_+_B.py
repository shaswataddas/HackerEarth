while True:
    try:
        num1,num2=map(int,input().split())
    except Exception:
        break
    else:
        print(num1+num2)
