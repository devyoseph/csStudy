import math

def calculate_fee(fees, time):
    fee = 0
    if time <= fees[0]:
        return fees[1]
    else:
        time -= fees[0]
        fee += fees[1] + math.ceil(time/fees[2]) * fees[3]
        return fee

def solution(fees, records):
    cars = dict()
    cars_fee = dict()
    for record in records:
        time, num, status = record.split()
        if status == 'IN':
            cars[num] = list(map(int,time.split(':')))
            if num not in cars_fee.keys():
                cars_fee[num] = 0
        elif status == 'OUT':
            print(time, num, status)
            h, m = list(map(int,time.split(':')))
            in_h, in_m = cars[num]
            print('==', cars)
            del cars[num]
            print('==', cars)

            # 총 시간 계산
            total_time = (h*60 + m) - (in_h*60 + in_m)
            cars_fee[num] += total_time

    if cars:
        for num, time in cars.items():
            h, m = 23, 59
            in_h, in_m = time

            # 총 시간 계산
            total_time = (h * 60 + m) - (in_h * 60 + in_m)
            cars_fee[num] += total_time

    # #차량의 총 요금 계산
    final_fee = []
    for num, time in cars_fee.items():
        fee = calculate_fee(fees, time)
        final_fee.append([num, fee])

    answer = []
    for fee in sorted(final_fee):
        answer.append(fee[1])
    print(answer)
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])