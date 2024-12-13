for i in range(0,100):
    grade=float(input("Enter grade:"))
    if grade >=70:
        print("You got A")
    elif  60<=grade<69:
        print("You got B")  
    elif 50<=grade<59:
        print("You got C")
    elif 40<=grade<49:
        print("You got D")
    elif 30<=grade<39:
        print("You got E")
    else:
        print("You have Failed")
