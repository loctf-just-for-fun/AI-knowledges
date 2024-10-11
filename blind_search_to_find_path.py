from collections import deque

# Hàm tìm kiếm theo chiều rộng (Breadth-First Search)
def bfs(graph, start, goal):
    # Sử dụng deque để làm hàng đợi
    queue = deque([[start]])
    # Tập hợp các nút đã thăm
    visited = set()

    while queue:
        # Lấy con đường đầu tiên trong hàng đợi
        path = queue.popleft()
        # Lấy nút cuối cùng trong con đường
        node = path[-1]

        # Nếu nút này là mục tiêu, trả về con đường
        if node == goal:
            return path

        # Nếu nút chưa được thăm, duyệt các nút kề
        elif node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            # Đánh dấu nút đã thăm
            visited.add(node)

    # Nếu không tìm thấy con đường
    return None

# Đồ thị dưới dạng danh sách kề (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Chạy BFS từ A đến F
start = 'A'
goal = 'F'
path = bfs(graph, start, goal)

if path:
    print(f"Đường đi từ {start} đến {goal}: {' -> '.join(path)}")
else:
    print(f"Không tìm thấy đường đi từ {start} đến {goal}")
