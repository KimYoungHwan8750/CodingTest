"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
"""

# 1. 사용자에게 T를 입력받는다.
# 2. 입력받은 T를 숫자로 변환하다.
# 3. T 값만큼 반복문을 돌린다.
# 4. 반복문 안에는 또 입력받는 함수를 사용한다.
# 5. 입력받은 문자열을 split(' ')를 이용해 잘라서 변수 A, B에 나눠담는다.
# 6. A와 B를 더해서 C를 구한다.
# 7. "Case #{}: {} + {} = {}".format(i,A,B,C)를 통해 문자열을 포매팅한다
# 8. 포맷팅한 문자열들을 List에 담아서 반복문이 끝난다면
# 9. for i in List : 반복문 안에서 print(i)를 이용해 출력한다

T = int(input())
result = []
for i in range(T):
    A_and_B = input()
    A = A_and_B.split(' ')[0]
    B = A_and_B.split(' ')[1]
    C = int(A) + int(B)
    result.append("Case #{}: {} + {} = {}".format(i + 1, A, B, C))
for res in result:
    print(res)