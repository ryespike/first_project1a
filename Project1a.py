mas_x=[1, 2, 3, 7, 8, 3, 2,]
i = 0
max_index=0
min_index=0
max_el=mas_x[0]
min_el=mas_x[0]
sum=0
for i in range(len(mas_x)):
        if max_el < mas_x[i]:
         max_el = mas_x[i]
         max_index=i
        if min_el > mas_x[i]:
         min_el = mas_x[i]
         min_index=i
print(min_index)
print(max_index)
if max_index< min_index:
    srez = mas_x[max_index:min_index+1]

else:
    srez=mas_x[min_index:max_index+1]
for i in range(len(srez)):
    sum=sum+srez[i]
print(sum)
print(srez)
