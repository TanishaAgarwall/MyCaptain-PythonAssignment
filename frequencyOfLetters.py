def most_frequent():
    str1 = str(input("Please enter a string: "))
    d = dict()
    for key in str1:
        if key not in d: 
            d[key] = 1
        else:
            d[key] +=1
    return d
print('Original dictionary : ',d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
