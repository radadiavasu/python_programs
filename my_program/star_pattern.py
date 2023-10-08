def full_pyramid(rows):
    
    # for i in range(rows):
    for i in (range(rows)): # Pattern will be reversed
        print(' '*(rows-i-1) + '*'*(2*i+1))
        
# full_pyramid(3) # only 3 pyramid will be print
full_pyramid(5) # only 5 pyramid will be print