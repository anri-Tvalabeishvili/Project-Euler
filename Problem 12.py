import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

factors = []     # ვქმნით ლისთს რათა რიცხვის გამოყოფები დროებით გავათავსოთ
numbers = [1,3]  # ვქმნით ლისთს რათა სამკუთხა რიცხვები შევინახოთ


while len(factors) < 500:  # ციკლს ვიმეორებთ სანამ რიცხვის გამყოფთა რაოდენობა არ გადააჭარბებს 500-ს
    number = numbers[-1]        # რიცხვების ლისთდიდან ვიღებთ ბოლო წევრს
    factor_1 = 0                # ვადგენთ საწისს გამყოსფ
    factors = []                # ყოველ ახალ რიცხვზე ვაცარიელებთ გამყოფების სიას რათა რაოდენობაში თანაკვეთა არ მოხდეს
    while True:             
        factor_1+=1         # საწყის გამყოფს ვუმატებთ 1-ს, ანუ პირველ გამყოფად ვიღებთ 1-ს
        if (number) % factor_1 == 0:        # თუ რიცხვი უნაშთოდ იყოფა საწყის გამყოფზე
            factor_2 = number / factor_1        # რიცხვს ვყოფთ ამ გამყოფზე და ვინახავთ ცვლადში

            if factor_1 < factor_2 :            # ამ ლოგიკით ორჯერ ვამცირებთ შემოწმების დროს რადგან 2*4=8 და 4*2=8
                factors.append(int(factor_1))   # ორივე გამყოფს ვამატებთ გამყოფთა სიაში
                factors.append(int(factor_2))   # ორივე გამყოფს ვამატებთ გამყოფთა სიაში
            else:
                break   # მეორე გამყოფი გადააჭარბებს პირველ გამყოფს შესაბამისად ვწყვეტთ ციკლს

    Rank = len(numbers) + 1      # ვპოულობთ შემდეგი ციფრის რიგობრივ ნომერს
    new_number = Rank * (Rank+1) / 2         # რიგობრივი ნომრის მიხედვით ვიგებთ, მანამდე არსებული ყველა ციფრის ჯამს
    numbers.append(int(new_number))        # მოცემულ ჯამს ვამატებთ სამკუთხა რიცხვების სიის ბოლო წევრად, რათა პირველმა ციკლმა ხელახლა შეძლოს ახალი ციფრის ამოღება
    

print(numbers[-2])      # რადგან ლოგიკა 1-ით წინ უსწრებს რეალურ პასუხს ამიტომ ამოგვაქვს ბოლოს-წინა ციფრი, რომელიც იქნება პასუხი

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს