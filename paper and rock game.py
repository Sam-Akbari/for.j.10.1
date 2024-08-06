def game():#تابع
    from random import choices#رندوم
    a = 0
    b = 0
    for i in range(5):#کاربر 5 بار فرصت دارد
        computer = choices(["scissors","paper","rock"])#کامپیوتر میتواند یکی را انتخاب کند
        player = input("enter your choice(""rock"",""paper"",""scissors""): ")#بازیکن انتخاب خود را وارد میکند
        print(computer)#چاپ انتخاب کامپیوتر

        if computer == ['rock']:#اگر کامپیوتر سنگ بود:انتخاب های کاربر
            if player == "scissors":#قیچی
                print("robat wins!") and a + 1 and b + 0#کامپیوتر برنده است
            if player == "paper":#کاغذ
                print("you win!") and a + 0 and b + 1#بازیکن برنده است
            if player == "rock":#سنگ
                print("not win!")and a + 0 and b + 0#مساوی

        elif computer == ['paper']:#اگر کامپیوتر سنگ بود:انتخاب های کاربر
            if player == "scissors":#قیچی
                print("you win!") and a + 0 and b + 1#بازیکن برنده است
            if player == "paper":#کاغذ
                print("not win!") and a + 0 and b + 0#مساوی
            if player == "rock":#سنگ
                print("robat wins!")and a + 1 and b + 0#کامپیوتر برنده است

        elif computer == ['scissors']:#اگر کامپیوتر سنگ بود:انتخاب های کاربر
            if player == "scissors":#قیچی
                print("not win!") and a + 0 and b + 0#مساوی
            if player == "paper":#کاغذ
                print("robat wins!") and a + 1 and b + 0#کامپیوتر برنده است
            if player == "rock":#سنگ
                print("you win!")and a + 0 and b + 1#بازیکن برنده است
        else:#در غیر این صورت
            print("Error!") and a + 0 and b + 0#ارور میدهد
    c = a#همه امتیاز ها برابر سی اند
    d = b#همه امتیاز ها برابر دی اند

    
    if d >= c:#اگر بازیکن بیشتر بود
        print("you win!")#بازیکن برنده است
    elif c >= d:#اگر روبات بیشتر بود
        print("robat wins!")#کامپیوتر برنده است
    else:#در غیر این صورت
        print("not win")#بنده ای وجود ندارد

game()#اجرا تابع

#پایان

