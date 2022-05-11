from math import ceil


def cal(s,e):
    resfee = 0
    knock = 1
    for k in range(s,e+1):
        if knock:
            resfee -= result[k][1]
            knock = 0
        else:
            resfee += result[k][1]
            knock = 1
    if not (e-s)%2:
        resfee += 1439
    if resfee<=fees[0]:
        return fees[1]
    else:
        return fees[1] + ceil((resfee-180)/fees[2])*fees[3]

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result = []
for record in records:
    time, num, inout = record.split()
    h, m = time.split(':')
    time = int(h)*60 + int(m)
    result.append([num, time])

result.sort(key=lambda x: (x[0], x[1]))
print(result)
check = 0
answer = []
for i in range(len(result)):
    if  i==len(result)-1 or result[i][0]!=result[i+1][0]:
        temp = cal(check,i)
        answer.append(temp)
        check=i+1
print(answer)
