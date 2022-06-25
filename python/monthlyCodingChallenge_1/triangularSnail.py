# https://programmers.co.kr/learn/courses/30/lessons/68645
# 정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 
# 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

# n은 1 이상 1,000 이하입니다.

# n	result
# 4	[1,2,9,3,10,8,4,5,6,7]
# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# 6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

def solution(n):
    answer = []
    answer_size = 1 

    for i in range(n):
        sub_arr = []
        for j in range(i + 1):
            sub_arr.append(0)
        answer.append(sub_arr)
    
    row, col = -1, 0

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            answer[row][col] = answer_size
            answer_size += 1

    return sum(answer, [])




def main():
    n = 4
    print(solution(n))

main()