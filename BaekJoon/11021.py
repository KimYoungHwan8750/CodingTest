"""
A+B - 7
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	284713	140165	120846	49.116%
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
"""
# 1. 첫째 줄에 입력받을 테스트 횟수
# 2. 테스트 횟수만큼 더할 숫자 두 개 입력받기(빈칸을 사이에 두고 숫자 두 개)
# 3. 더하기된 값을 Case #반복횟수: 형태로 출력하기

# 입력은 input으로 받는다.
# for문은 for i in range(횟수):
# "Case #{}:".format(i) 형태를 사용해 {}안에 자동으로 i가 삽입된다.

count = int(input())
result_list = []
for i in range(count):
    num = input()
    first = num.split(' ')[0]
    second = num.split(' ')[1]
    result_list.append("Case #{}: {}".format(i+1, int(first) + int(second)))

for i in result_list:
    print(i)