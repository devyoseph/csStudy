f = [180, 5000, 10, 600]
r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

def solution(fees, records):
    car_info = []
    car_pay = {}
    # 차번호 들시 들분
    for car_num in records:
        if len(car_num) == 13:
            car_info.append([car_num[6:10], int(car_num[0:2]), int(car_num[3:5])])
            continue

        if len(car_num) == 14:
            for i in range(len(car_info)):
                print(car_info[i][0])
                print(car_num[6:10])
                if car_info[i][0] == car_num[6:10]:
                    h = int(car_num[0:2]) - car_info[i][1]
                    m = int(car_num[3:5]) - car_info[i][2]
                    if m < 0:
                        h -= 1
                        m += 60
                    time = h * 60 + m

                    if fees[0] - time <= 0:
                        if car_num[6:10] in car_pay:
                            car_pay[car_num[6:10]] += fees[1]
                        else:
                            car_pay[car_num[6:10]] = fees[1]

                    else:
                        pay = 0
                        pay += fees[1]
                        extra_time = fees[0] - time
                        extra_money = extra_time // fees[2]
                        pay += extra_money * fees[3]
                        if extra_time % fees[2]:
                            pay += fees[3]

                        if car_num[6:10] in car_pay:
                            car_pay[car_num[6:10]] += fees[1]
                        else:
                            car_pay[car_num[6:10]] = fees[1]

                car_info.pop(i)

    if car_info:
        print(car_info)

    print(car_pay)

    answer = []
    return answer

solution(f, r)