'''

프렌즈4블록
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

board map
만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

board map

블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

board map

만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
board map

위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

입력 형식
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
출력 형식
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

입출력 예제
m	n	board	answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
예제에 대한 설명
입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.

'''

def solution(m, n, board):
    cnt = 0
    while True:
        cnt_lst = []
        for j in range(m-1):
            for i in range(n-1):
                if board[j][i] == board[j + 1][i] == board[j][i + 1] == board[j + 1][i + 1] != '0':
                    cnt_lst.append([j, i])
                    cnt_lst.append([j, i + 1])
                    cnt_lst.append([j + 1, i])
                    cnt_lst.append([j + 1, i + 1])
        unique_data = [list(x) for x in set(tuple(x) for x in cnt_lst)]
        cnt+=len(unique_data)

        #겹치는 부분이 없으면 리턴
        if len(cnt_lst) == 0:
            return cnt

        for i in unique_data: #사라진 위치의 값을 0으로 변환
            board[i[0]] = board[i[0]][:i[1]] + '0' + board[i[0]][i[1]+1:]

        #아래로 내려오게 해야해서 뒤집은 다음에 for 문 실행
        board.reverse()
        # 비어진 부분을 내리는 과정
        for j in range(m-1):
            for i in range(n):
                #0 인 부분이 나오면 그 위에 0 이 아닌 값을 찾아서 바꾼다
                if board[j][i] == '0':
                    for k in range(1,m-j):
                        if board[j+k][i] != '0':
                            board[j] = board[j][:i] + board[j+k][i] + board[j][i + 1:]
                            board[j+k] = board[j+k][:i] + '0' + board[j+k][i + 1:]
                            break

        board.reverse()


# def pop_num(b, m, n):
#     pop_set = set()
#     # search
#     for i in range(1, n):
#         for j in range(1, m):
#             if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
#                 pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
#     # set_board
#     for i, j in pop_set:
#         b[i][j] = 0
#     for i, row in enumerate(b):
#         empty = ['_'] * row.count(0)
#         b[i] = empty + [block for block in row if block != 0]
#     return len(pop_set)
#
#
# def solution(m, n, board):
#     count = 0
#     b = list(map(list, zip(*board)))
#     while True:
#         pop = pop_num(b, m, n)
#         if pop == 0: return count
#         count += pop