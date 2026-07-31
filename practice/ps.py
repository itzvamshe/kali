arr = [1,2,3,4,5,6,7,8,9,10]

prefix_sum = []
var = 0

for item in arr:
    var = var + item
    prefix_sum.append(var)

print(prefix_sum)
