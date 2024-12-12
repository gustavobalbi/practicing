#The essay asks for a 'print' that is intended to display the items in the first array along with a counter indicating how many items in the second list they are divisible by.
#Both inputs must be provided on a single line, with numbers separated by a space.

def div(v1, v2):
    count = []
    for i in range(len(v1)):
        c = 0
        for h in range(len(v2)):
            if v1[i] % v2[h] == 0:
                c += 1
        count.append(c)
    
    return count

def display(v1, div):
    for i in range(len(v1)):
        print(v1[i], count[i])

v1 = [int(x) for x in input().split()]
v2 = [int(x) for x in input().split()]

count = div(v1, v2)
display(v1, count)
