# 안빠져나갔으면 23:59 로 기록
# 기본시간 180: 5000원
# 단위 요금 10분 : 600원

def cal(HF, MF, H, M, fees):

    netA = HF*60 + MF
    netB = H*60 + M

    netAll = netA - netB
    return netAll

def cost(netAll, fees):
    # print(netAll)
    basic_time = fees[0]
    basic_fee = fees[1]
    # print("메서드", HF,MF, H, M)
    add_time = fees[2]
    add_fee = fees[3]
    # 0을 기준으로 분으로 완전 초기화
    if netAll <= basic_time:
        return basic_fee
    else:
        NET = netAll - basic_time
        num = NET // add_time

        if NET % add_time == 0:
            return basic_fee + add_fee * num
        else:
            return basic_fee + add_fee * (num + 1)

def solution(fees, records):

    map = dict()

    for record in records:
        H = int(record[0:2])
        M = int(record[3:5])
        NUM = int(record[6:10])
        #print("현재 ", H, M, NUM)

        if record[11] == 'I':
            if NUM in map:
                HS, MS, status, SUM = map[NUM]
                map[NUM] = [H, M, 0, SUM]

            else:
                map[NUM] = [H, M, 0, 0]
            #print("들어감", map[NUM])
        else:
            #print("꺼냅", map[NUM])
            HS, MS, status, SUM = map[NUM]
            map[NUM] = [0,0,1,SUM+cal(H, M, HS, MS, fees)]

    # 정산안된것들
    for key in list(map.keys()):
        if map[key][2] == 0:
            HS, MS, status, SUM = map[key]
            map[key] = [0,0,1,SUM+cal(23, 59, HS, MS, fees)]
        HS, MS, status, SUM = map[key]
        map[key] = [0,0,1,cost(SUM, fees)]

    #print("결과", res)
    res = list(map.items())
   #  print(res)
    res.sort(key=lambda x:x[0])
    result = []
    for i in res:
        result.append(i[1][3])
    return result