# 프로그래머스 멀리뛰기

def solution(n):
    answer = 0
    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = (dp[i-1] +dp[i-2])
    return dp[n-1]


#프로그래머스 블록 이동하기
from collections import deque

def move(cor1,cor2,board):
    move = [(1,0), (0,1), (-1,0), (0,-1)]
    ret=[]
    #이동
    for m in move:
        if board[cor1[0]+m[0]][cor1[1]+m[1]]==0 and board[cor2[0]+m[0]][cor2[1]+m[1]]==0:
            ret.append({(cor1[0]+m[0],cor1[1]+m[1]),(cor2[0]+m[0],cor2[1]+m[1])})

    rotate=[1,-1]
    #가로회전
    if cor1[0]==cor2[0]:
        for r in rotate:
            if board[cor1[0]+r][cor1[1]]==0 and board[cor2[0]+r][cor2[1]]==0:
                ret.append({(cor1[0]+r,cor1[1]),(cor1[0],cor1[1])})
                ret.append({(cor2[0]+r,cor2[1]),(cor2[0],cor2[1])})
    #세로회전
    else:
        for r in rotate:
            if board[cor1[0]][cor1[1]+r]==0 and board[cor2[0]][cor2[1]+r]==0:
                ret.append({(cor1[0],cor1[1]),(cor1[0],cor1[1]+r)})
                ret.append({(cor2[0],cor2[1]),(cor2[0],cor2[1]+r)})
    return ret

def solution(board):
    try:
        size = len(board)
        #경계 체크 쉽게하기 위해서 지도의 상하좌우에 1 추가
        new_board = [[1] * (size+2) for _ in range(size+2)]
        for i in range(size):
            for j in range(size):
                new_board[i+1][j+1] = board[i][j]

        print(1)
        que = deque()
        visited = []

        #queue에 [로봇의 좌표정보, 지금까지 거리] 형태로 넣음
        que.append([{(1,1),(1,2)},0])
        visited.append({(1,1),(1,2)})

        while len(que)!=0:
            temp = que.popleft()
            cor = list(temp[0])
            dist = temp[1]+1

            for m in move(cor[0],cor[1],new_board):
                if (size,size) in m:
                    return dist

                if not m in visited:
                    que.append([m,dist])
                    visited.append(m)

        return 0
    except Exception as e: 
        print(e)
