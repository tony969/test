smallest = 4
print('Before')
for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] :
    if smallest > 3 :
       smallest = value
    elif value > smallest :
     smallest = value
    print(smallest, value)
print('After', smallest)
