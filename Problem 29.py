import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


answer = []     # ლისთი ყველა პასუხის შესანახად


for a in range(2,101):  # ვსანზღვრავთ a განსაზღვირს არეს 
    for b in range(2,101):  # ვსანზღვრავთ b განსაზღვირს არეს 
        if a**b not in answer:  # თუ ასეთი წევრი არ იქნება ლისთში მაშინ დავამატოთ
            answer.append(a**b)


print(len(answer))  # ვიგებთ ლისთის სიგრძეს ანუ იმას თუ რამდენი ელემენტია შიგნით

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს