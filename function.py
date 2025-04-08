def sum_list(input):
    total = 0
    for val in input:
        total += val
    return total

# input 
a = [200,300,180,400]
b = [300,200,100,400]
c = [300,400,200]

print("Total of A:",sum_list(a))
print("Total of B:",sum_list(b))
print("Total of C:",sum_list(c))

print("Total =",sum_list(a)+sum_list(b)+sum_list(c))