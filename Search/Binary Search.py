## 이진 탐색

def solution(L, x):
    ### 리스트의 시작점과 끝점 정의
    low = 0
    high = len(L) - 1
    
    # 중간값을 정해놓고 찾아나가기
    while low <= high:
        mid = (low + high) // 2
        
        if L[mid] == x:
            return mid
        elif L[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
        
        # 리스트 안에 원소가  경우 None 반환
        return None
