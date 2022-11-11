num=int(input("Enter some number"))
list=[]
for items in range(num):
    list.append(items)
so=sorted(list)
print(list)
maxi=max(list)
mini=min(list)
countmax=0
countmin=0
for i in list:
    if i==maxi:
        countmax+=1

for it in list:
      if it==mini:
         countmin+=1

print(countmax)
print(countmin)
avg=(maxi+mini)/(countmin+countmax)
print(avg)

