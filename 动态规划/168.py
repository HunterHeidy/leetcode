low=58
high=155
l =len([int(char) for char in str(low)])
h=len( [int(char) for char in str(high)])
# print(high)
pre=[]
for i in range(l-1,h):
    # print(i)
    for x in range(1,10-i):
        sun=0
        s=x
        for j in range(i,-1,-1):
            # print(j)
            tep=10**j
            # print(tep)
            sun +=s*tep
            # print(sun)
            s+=1
            # print(s)
            # print(x)
       # print(sun)
       
        if sun<=high and sun>=low:
        	pre.append(sun)
        	
print(pre)