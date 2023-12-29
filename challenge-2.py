def Two_numbers_are_positive(a,b,c):
    count = 0
    if a > 0 :
        count += 1
    if b > 0 :
        count += 1
    if c > 0 :
        count += 1
    
    if count ==2:
        return True
    else:
        return False    
    # return count    

print(Two_numbers_are_positive(2, 4, -3))        # True
print(Two_numbers_are_positive(-4, 6, 8))        #True
print(Two_numbers_are_positive(-4, 6, 0))        #False
print(Two_numbers_are_positive(4, 6, 10))        #False