
##

# txt = "Google#Facebook#Runoob#Taobao"
# x = txt.split("#", 2)
# print(x)


##
n = int(input())
print(n)
a = list(map(int, input().split()))
sum = 0
ans = 0
for i in a:
    if i > ans:
        ans = i
    sum += i
while((ans*n-sum) <= sum):
    ans += 1
print(ans)
