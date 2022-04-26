import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


fibonachi = [1,1]      # ფიბონაჩის მიმდევრობისთვის შევქმნათ ლისთი

while len(str(fibonachi[-1])) != 1000:   # ციკლი გავაგრძელოთ მანამ სანამ ფიბონაჩის ლისთის ბოლო წევრი არ იქნება 1000-ნიშნა
    new_number = fibonachi[-1] + fibonachi[-2]      # ყველა ახალ ციკლზე ვიპოვოთ ახალი ფიბონაჩის წევრი
    fibonachi.append(new_number)        # ნაპოვნი ახალი წევრი დავამატოთ ლისთის ბოლო წევრად
    
    
print(len(fibonachi))       # ვიპოვოთ ლისთის სიგრძე რათა გავიგოთ მერამდენე ადგილზე დგას ბოლო 1000-წევრიანი რიცხვი

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს