pre_number = 0
next_number = 1 
count = 0

while count < 10 :
    print (pre_number, end=" ")
    next = pre_number + next_number
    pre_number = next_number
    next_number = next 
    count = count + 1
