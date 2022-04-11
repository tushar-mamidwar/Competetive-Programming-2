def sum_of_prime_factors(num):
    list1=[]
    count=2
    while num!=1:
        if num%count==0:
            num//=count
            list1.append(str(count))
        else: 
            count+=1
    factor_sum=0
    for i in list1:
        for j in i:
            factor_sum+=int(j)
    return factor_sum
def check_smith_number(innum):
    innum_sum=0
    for i in innum:
        innum_sum+=int(i)
    if innum_sum==sum_of_prime_factors(int(innum)):
        print('yes')
    else:
        print('no')

innum=input()
check_smith_number(innum)


    
        
        
