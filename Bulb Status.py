num=int(input())
no_of_turns=int(input())
len=min(num//2+1,no_of_turns)
count=0
for i in range(1,len+1):
    if not num%i:
        count+=1
if i%2==0:
    print('Bulb is off')
else:
    print('Bulb is on')
    
"""
--------------------Output--------------------
8191
8191
Bulb is off
"""
