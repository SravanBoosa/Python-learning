#Break: Used to terminate the loop when encountered
'''i=1
while(i<=5):
    print(i)
    if(i==3): #break the loop once condition in true and prints untill 3
        break
    i+=1
print("end of loop")'''


'''i=2
while(i%2==0):
    print(i)
    if(i==10):
        break
    i+=2
print('end')'''


'''i=1
while(i%2!=0):
    print(i)
    if(i==9):
        break
    i+=2
print('end')'''

#Continue : terminate the current iteration & continue execution of the loop with the next iteration
# it acts as skip

'''i=0
while(i<=5):
    if(i==3):
        i+=1
        continue #skips 3 
    print(i)
    i+=1
print("end")'''

'''i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
print('end')'''     


'''i=1
while(i<=10):
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
print('end')'''  

'''print(bin(15))

print(15 & 22)
print(15 | 22)'''

'''var=10
var_left = var<<2  # 10 << 2 → 40 // 10 multiplied by 2 to the power of 2
var_left2 = var<<1 # 10 << 1 → 20 // 10 multiplied by 2 to the power of 1
var_right = var>>1 #10 >> 1 → 5 // 10 divided by 2 to the power of 1
var_right2 = var>>2 #10 >> 2 → 2 // 10 divided by 2 to the power of 2
print(var, var_left, var_left2, var_right, var_right2)'''