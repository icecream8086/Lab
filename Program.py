from ast import operator


first =float(input("Value 1"))
second =float(input("value 2"))
operator=input("select your symbol")

if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    if second==0:
        print("0 can't div")
    else:
        print(first/second)