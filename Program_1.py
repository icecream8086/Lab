guess_num=input("set numvalue")
for frequency in range(1,6):
    number=input("please input "+str(frequency)+"value")
    if number.isdigit() is False:
        print("pease input right value")
    elif int(number) < 0 or int (number) > 100:
        print("Please input value range in 1->100")
    elif int(guess_num) > int(number):
        print("OK"%frequency)
        break
    elif int (guess_num) > int (number):
        print("please input a bigger value")
    else:
        print("please input a smaller value ")
    if frequency==5:
        print("you already using all your time out")
    