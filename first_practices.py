#######################divisibility_by_four###########################
def divisibility_by_four():
    arry_num=[]
    for num in range(22,106):
        if (num%4)==0:
            arry_num.append(num)
    return arry_num

##########################divisibility_by_five_not_three############################
def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def divisibility_by_five_not_three():
    arry_num = []
    for num in range(200, 19, -5):
        if(num%5!=0):
            continue
        else:
            sum_digit = getSum(num)
            if ((sum_digit % 3) != 0):
                arry_num.append(num)
    return arry_num

##################################divisibility_by_five_and_six###############################
def divisibility_by_five_and_six():
    sum=0
    for num in range(123, 568):
        if (num%5==0)or(num%6==0):
            sum=sum+num
    return sum

#############################multiply################################
def multiply():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j,end="\t")
        print(end="\n")

###############################parallelogram##############################
def parallelogram(a,b):
    for i in range(1, b+1):
        if (i == 1) or (i == b):
            print(' ' * (b + 1 - i) + '*' * a + ' ' * i)
        else:
            print(' ' * (b + 1 - i) + '*' + ' ' * (a-2) +'*'+ ' ' * i)

################################################################
user_input=input("""Options:\n1)Divisibility by four\n2)Divisibility by five and not three
3)Divisibility by five or three or both of  them\n4)Multiplication table\n5)Draw parallelogram\n6)Exit\nSelect one of them:""")
while True:
    if int(user_input)==1:
        print(divisibility_by_four())
        user_input = input("Select other option:")
    elif int(user_input) == 2:
        print(divisibility_by_five_not_three())
        user_input = input("Select other option:")
    elif int(user_input) == 3:
        print(divisibility_by_five_and_six())
        user_input = input("Select other option:")
    elif int(user_input) == 4:
        multiply()
        user_input = input("Select other option:")
    elif int(user_input) == 5:
        parallelogram(5,4)
        user_input = input("Select other option:")
    else:
        break