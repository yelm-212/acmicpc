import sys

read = sys.stdin.readline

N = int(input())
nlist = [list(map(int, read().rstrip())) for _ in range(N)]  # 2차원 배열 리스트로 저장

ans = []


def calc(x, y, n):
    clr = nlist[x][y]  #현재 좌표 값 저장

    #재귀함수 호출
    for i in range(x, x + n):
        for j in range(y, y + n):
            if clr != nlist[i][j]:
                ans.append("(")
                calc(x, y, n // 2)
                calc(x, y + n // 2, n // 2)
                calc(x + n // 2, y, n // 2)
                calc(x + n // 2, y + n // 2, n // 2)
                ans.append(")")
                return 0
    ans.append(clr)


calc(0, 0, N)
print(*ans, sep="")
