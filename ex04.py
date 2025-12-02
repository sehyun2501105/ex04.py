#39
def a(n):
    for i in range(0, n+1):
        if i % 2 !=1:
            print(i)
b = int(input())
print(a(b))

#40
def a(n):
    for i in range(0,n+1):
        if i % 3 == 0:
            print(i)
b = int(input())
print(a(b))

#41
def n(a,b,c,d):
    numbers = [a,b,c,d]
    return max(numbers), min(numbers)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

max, min = n(a,b,c,d)

print('최댓값:' , max)
print('최솟값: ' ,min)

#42
def a(n):
    for i in range(0, n+1):
        if i % 2 !=1:
            print(i)
b = int(input())
print(a(b))

#43
def a(n):
    result = 1
    for i in range(1,n+1):
        #result *= i
        result += i
    return result

b = int(input())
print((b))
    
#44
def a(i,j):
    total = 0
    for x in range(1, i+1):
        for y in range(1, j+1):
            if x * y >= 30:
                total += x*y
    return total

#45
# def n(a,b,c,d):
#     nums = [a,b,c,d]
#     nums.sort(reverse=True)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# result = n(a,b,c,d)
# print("내림차순 정렬", result)        

def a(n):
    result = []
    total = 0
    for i in n:
        total += i
        result.append(total)
    return result

b=list(map(int,input(" ").split()))
print(a(b))