## 재귀적 이진탐색


def solution(L, x, l, u):
    # 시작점이 끝점보다 커지면 None
    if l > u:
        return None
   
    # 중간값 구하기
    mid = (l + u) // 2
    
    # 중간값과 x가 같으면 중간값 반환
    if x == L[mid]:
        return mid
    
    # 중간값이 더 크면 끝점을 mid-1
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    
    # 중간값 보다 더 크면 시작점을 mid + 1
    else:
        return solution(L, x, mid+1, u)
