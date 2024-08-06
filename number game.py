def numbergame():#تابع
    from random import randint, choices #رندوم
    num = randint(1, 10)#متغیر عدد برابر اعداد بیت 1 تا 10 است
    for i in range(5):#کاربر فقط 5 بار شانس دارد
        a = int(input("Enter a number 1 to 10: "))##از کابر عدد میگیرد
        if a == num:#اگر درست حدس بزند
            print("true")#درست چاپ میشود
            break# و بعد برنامه قطع میشود
        elif a >= num:#یا اگر عدد بزرگتر بود
            print("your number is big!")#عدد بزرگ است
        elif a <= num:#یا اگر عدد کوچک تر بود
            print("your number is small!")#عدد کوچک است

numbergame()#اجرا تابع

#پایان
