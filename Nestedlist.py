list_score = []
list_duo = []
list_some = []
list_finall = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    list_score.append(score)
    list_duo.append([name,score])

checkfirstmin = min(list_score)
sort_list = sorted(list_duo)

for i in sort_list:
    if i[1] != checkfirstmin:
        list_some.append(i)

for j in list_some:
    list_finall.append(j[1])

for z in list_some:
    if z[1] == min(list_finall):
        print(z[0])
    else:
        pass
