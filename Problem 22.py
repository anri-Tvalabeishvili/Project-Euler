import string
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

f = open('Data/Problem_22.txt', 'r')   # შემოგვყავს ფაილი

content = f.read()  # ფაილის ელემენტს ვინახავთ რაიმე ცვლადში

content= content.split(",")  # რადგან პროგრამა ყველა ელემენტს ერთ ელემენტად აღიქვამს ამიტომ ამ ერთ ელემენტს ვყოფთ ელემენტაბათ ","-ის მეშვეობით

content.sort()          # ვალაფებთ ანბანური თანმიმდევრობით

Alphabet = list(string.ascii_uppercase)     # შემოგვყავს ანბანის ლისთი


answer = []  # ვქმნით ლისთს სადაც საბოლოო პასუხებს შევინახავთ რათა შემდგომში ავჯამოთ 

for k in range(len(content)):       # ვიღებთ თითოეული ელემენტის ინდექს
    name = content[k]       # ინდექსით ვპოულობთ ამ ელემეტს 
    value = 0           # ვქმნით ცვლადს თითოეული სახელის ქულის დასადგენად, ყველა ახალი სახელის შემოსვლისა ეს ნულდება 
    for i in name:      # ვიღებთ ასოებს სიტყვებიდან
        index = Alphabet.index(i) + 1       # ვამოწმებთ ამ ასოების რიგითობას, რადგან ლისთის პირველი წევრი 0-ა ამირომ თანრიგის გასწორების მიზნით ვამატებთ 1-ს 
        value += index      # თითოეული ასოს ადგილმდებარეობის აღმნიშვნელ რიცხვს ვკრიბავთ რათა სიტყვის ქულა გამოვთვალოთ

    score = value * (k+1)       # სიტყვის ქულას ვამრავლებთ ამ სიტყვის ადგილის ნომერზე რათა საბოლოოს ქულა მივიღოთ
    answer.append(score)       # საბოლოო ქულას ვამატებთ ლისთში რათა შევკრიბოთ 

print(sum(answer))

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს

""" 
1) კოდი შეიძელბა შეიცვალოს შემდეგნაირადაც

line 14:   answer = 0 
line 24:   answer += score

 """