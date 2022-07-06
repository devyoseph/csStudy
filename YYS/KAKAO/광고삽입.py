def solution(play_time, adv_time, logs):

    S = int(play_time[6:])
    M = int(play_time[3:5])
    H = int(play_time[0:2])

    TIME = H*60*60 + M*60 + S
    video_data = [0 for _ in range(TIME+1)]
    video_data_sum = [0 for _ in range(TIME + 1)]

    S = int(adv_time[6:])
    M = int(adv_time[3:5])
    H = int(adv_time[0:2])

    TIME = H*60*60 + M*60 + S

    ad_length = H*60*60 + M*60 + S

    #print(len(video_data), ad_length)

    for log in logs:
        start_S = int(log[6:8])
        start_M = int(log[3:5])
        start_H = int(log[0:2])
        video_data[start_H*60*60 + start_M*60 + start_S] += 1

        last_S = int(log[15:17])
        last_M = int(log[12:14])
        last_H = int(log[9:11])
        video_data[last_H * 60 * 60 + last_M * 60 + last_S] -= 1



    SUM = 0
    for index in range(len(video_data)):
        SUM += video_data[index]
        video_data_sum[index] = SUM

    sliding_window = sum(video_data_sum[0:ad_length])
    sliding_window_sum = [0]*(len(video_data)-ad_length)

    sliding_window_sum[0] = sliding_window

    start = 0
    last = ad_length
    for index in range(1, len(video_data)-ad_length):
        sliding_window -= video_data_sum[start]
        sliding_window += video_data_sum[last]
        sliding_window_sum[index] = sliding_window
        start += 1
        last += 1

    MAX = 0
    INDEX = 0
    for index in range(len(sliding_window_sum)):
        if sliding_window_sum[index] > MAX:
            MAX = sliding_window_sum[index]
            INDEX = index
    # print(MAX, INDEX)
    H = INDEX//3600
    INDEX -= H*3600
    M = INDEX//60
    INDEX -= M*60
    S = INDEX
    # print(H,M,S)
    RESULT = [H, M, S]
    answer = ""
    for index in range(3):
        if len(str(RESULT[index])) == 1:
            answer += "0"
        answer += str(RESULT[index]) + ":"

    return answer[:len(answer)-1]
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))