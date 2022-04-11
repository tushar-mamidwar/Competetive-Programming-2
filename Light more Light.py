num=int(input())
len=min(num//2+1,num)
count=0
for i in range(1,len+1):
    if not num%i:
        count+=1
if i%2==0:
    print('No')
else:
    print('Yes')
    
"""
--------------------Output--------------------
6241
Yes
"""
