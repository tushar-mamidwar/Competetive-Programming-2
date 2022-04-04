def is_prime(num):
    list1=[]
    for n in range(2,num+1):
        len=n//2+1
        for i in range(2,len):
            if not n%i:
                break
        else:
            list1.append(n)
    return list1
in_num=int(input())

prime_list=is_prime(in_num)
prime_list.reverse()
for i in prime_list:
    for j in prime_list:
        for k in prime_list:
            for l in prime_list:
                if i+j+k+l==in_num:
                    print(i,j,k,l)
                    quit()
print("Not Possible")

"""
--------------------Output--------------------
104
97 3 2 2
"""
