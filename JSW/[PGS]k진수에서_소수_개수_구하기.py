def solution(n, k):
    def jinsu(n, k):
        input_data = n
        jinsu_list = []

        while input_data > 0:
            jinsu_list = [input_data % k] + jinsu_list
            input_data = input_data // k

        return jinsu_list

    def is_prime_num(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    answer = 0
    jinsu_data = jinsu(n, k)
    temp_data = 0

    while jinsu_data:
        element = jinsu_data.pop(0)
        if element:
            temp_data *= 10
            temp_data += element
            if len(jinsu_data) == 0:
                if is_prime_num(temp_data):
                    answer += 1
                temp_data = 0

        else:
            if temp_data:
                if is_prime_num(temp_data):
                    answer += 1
                temp_data = 0
                pass

    return answer