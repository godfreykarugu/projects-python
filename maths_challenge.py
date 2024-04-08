import random
import time

OPERATORS = ['+', '-','*']

upper_limit = 12
lower_limit = 3
Total_Questions = 10

def generate_questions():
    left = random.randint(lower_limit, upper_limit)
    right = random.randint(lower_limit, upper_limit)

    op = random.choice(OPERATORS)

    exp = str(left) +" " + op +" " +str(right)
    answer = eval(exp)
    return exp, answer

'''exp, answer = generate_questions()
print(exp, answer)'''

print("Welcome to the Maths,press enter to Start")
print("---------------------------------------------")

start_time = time.time()

for i in range(Total_Questions):
    while True:
        exp, answer = generate_questions()
        guess = input("Question #" +str(i + 1) +' '+exp +" = ")
        if guess == str(answer):
            break

end_time = time.time()
total_time = round( end_time - start_time,2)
print("Nice work! You completed in  " + str(total_time) + " seconds")

