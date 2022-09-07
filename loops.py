pre_number = 0
next_number = 1
count = 20

for i in range(count) :
    print(pre_number, end=" ")
    next = pre_number + next_number 
    pre_number = next_number
    next_number = next 
     