## 피보나치 순열 구현

def solution(x):
    """ x가 0 일 경우에는 0 반환, 1 또는 2일 경우에는 1을 반환하게 됨"""
    if x == 0:
        return 0
    
    elif x == 1 or x == 2:
        return 1
    
    ## x가 2를 넘어가면 재귀 시작
    else:
        return solution(x - 1) + solution(x - 2)
