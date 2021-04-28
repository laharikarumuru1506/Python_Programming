import random
#entering into the game....
s=input("Are you ready to play????...say YES or NO....")
#if you say yes the game is going to continue...
if s=='yes':
    num=random.randint(1,36)
    print("Welcome!Let's start the game....your target number is",num)
    if (num%6)== 0:
        count = (num // 6)
        print("And you've only", count, "chances to play")
    else:
        count=(num // 6)+1
        print("And you've only",count,"chances to play")
    x=input("enter YES to continue....otherwise NO to exit....")
    sum = 0
    ch = 1
    res = count
    while x=='yes' and count >= ch:
        c=random.randint(1,6)
        print("the rolled number is",c)
        sum += c
        res=res-1
        print("your score is",sum ,"and your target number is",num)
        if sum>=num:
            print("Congratulation! You won the game")
            break
        elif res==0:
            print("Better luck next time!!!!!!!")
            break
        else:
            print("you've only",res,"chances to play")
            x = input("enter YES to continue....otherwise NO to exit....")
            ch += 1

#if you say no the game is going to exit...
else:
    print("Thank you!!!.....meet you again")