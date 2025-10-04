from collections import deque

def min_button_presses(A, B, favorites):
    visited = [False] * 1000 
    queue = deque()
    queue.append((A, 0))
    visited[A] = True

    while queue:
        current, count = queue.popleft()

        if current == B:
            return count

        if current + 1 < 1000 and not visited[current + 1]:
            visited[current + 1] = True
            queue.append((current + 1, count + 1))

        if current - 1 >= 0 and not visited[current - 1]:
            visited[current - 1] = True
            queue.append((current - 1, count + 1))

        for freq in favorites:
            if not visited[freq]:
                visited[freq] = True
                queue.append((freq, count + 1))

if __name__ == "__main__":
    try:
        A, B = map(int, input().split())
        N = int(input())
        favorites = []
        for _ in range(N):
            freq = int(input())
            if 0 <= freq < 1000:
                favorites.append(freq)
        print(min_button_presses(A, B, favorites))
    except Exception as e:
        print("입력 처리 중 오류가 발생했습니다:", e)
