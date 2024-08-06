from random import choice as c#رندوم

def hangman():#تابع
    words = ["google","samsung","microsoft","intel","apple","nasa","vivo","meta","open AI","LG"]#نام ها
    word = c(words)#متغیر کلمه
    lenalfabet = ["_"] * len(word)#تعداد حروف های کلمه
    attempts = len(word)#شمارش حروف ها
    
    print("Start!")#شروع
    print("word:", len(word))#حروف های کلمه را تعدادشان را چاپ کند
    
    while attempts > 0 and "_" in lenalfabet:#تاوقتی که حروف ها بزرگتر از صفر است و خط ها در حروف ها هستند
        print(" ".join(lenalfabet))#یک فاصله و تعداد های حروف ها ی جدید رو نشون بده
        guess = input("Your guess: ")#از کاربر بگیرد
        
        if guess in word:#اگر حدس کاربر در کلمه بود 
            for index,letter in enumerate(word):#ایجاد حلقه 
                if guess == word:#اگر درست بود
                    lenalfabet[index] = guess#تمام

        else:#در غیر این صورت
            attempts -= 1#حروف هارو کم کن یکی
            print("False",":", attempts)#غلط را چاپ کن با تعداد حروف ها
    
    if guess == word:#اگر درست بود
        print("True!", word)#تمام
        
    else:#در غیر این صورت
        print("Game over:", word)#باخت

hangman()#اجرا تابع

#پایان

