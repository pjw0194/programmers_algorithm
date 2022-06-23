# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요

# n은 1 이상 100,000,000 이하인 자연수입니다.

#  n   result
#  45	 7
# 125	229

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)
#     return answer

def solution(n):
    answer = 0
    ternary = []
    index = 1

    while(n > 0):
        ternary.append(n % 3)
        n //= 3

    for num in reversed(ternary): 
        answer += index * num
        index *= 3

    return answer


def main():
    n = 45
    print(solution(n))

main()