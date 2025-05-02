from collections import deque


# Функція для пошуку збільшуючого шляху (BFS)
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            # Перевірка, чи є залишкова пропускна здатність у каналі
            if (
                not visited[neighbor]
                and capacity_matrix[current_node][neighbor]
                - flow_matrix[current_node][neighbor]
                > 0
            ):
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False


# Основна функція для обчислення максимального потоку
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [
        [0] * num_nodes for _ in range(num_nodes)
    ]  # Ініціалізуємо матрицю потоку нулем
    parent = [-1] * num_nodes
    max_flow = 0

    # Поки є збільшуючий шлях, додаємо потік
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Знаходимо мінімальну пропускну здатність уздовж знайденого шляху (вузьке місце)
        path_flow = float("Inf")
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(
                path_flow,
                capacity_matrix[previous_node][current_node]
                - flow_matrix[previous_node][current_node],
            )
            current_node = previous_node

        # Оновлюємо потік уздовж шляху, враховуючи зворотний потік
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        # Збільшуємо максимальний потік
        max_flow += path_flow

    return max_flow


if __name__ == "__main__":
    # Матриця пропускної здатності для каналів у мережі (capacity_matrix)
    capacity_matrix = [
        [0, 0, 25, 20, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Термінал 1
        [0, 0, 0, 10, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Термінал 2
        [0, 0, 0, 0, 0, 0, 15, 10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Склад 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 10, 25, 0, 0, 0, 0, 0, 0, 0, 0],  # Склад 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 15, 10, 0, 0, 0, 0, 0],  # Склад 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 15, 5, 10], # Склад 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Магазин 14
    ]


#     capacity_matrix = {
#         # Термінали -> Склади
#         ("Термінал 1", "Склад 1"): 25,
#         ("Термінал 1", "Склад 2"): 20,
#         ("Термінал 1", "Склад 3"): 15,
#         ("Термінал 2", "Склад 3"): 15,
#         ("Термінал 2", "Склад 4"): 30,
#         ("Термінал 2", "Склад 2"): 10,

#         # Склади -> Магазини
#         ("Склад 1", "Магазин 1"): 15,
#         ("Склад 1", "Магазин 2"): 10,
#         ("Склад 1", "Магазин 3"): 20,
#         ("Склад 2", "Магазин 4"): 15,
#         ("Склад 2", "Магазин 5"): 10,
#         ("Склад 2", "Магазин 6"): 25,
#         ("Склад 3", "Магазин 7"): 20,
#         ("Склад 3", "Магазин 8"): 15,
#         ("Склад 3", "Магазин 9"): 10,
#         ("Склад 4", "Магазин 10"): 20,
#         ("Склад 4", "Магазин 11"): 10,
#         ("Склад 4", "Магазин 12"): 15,
#         ("Склад 4", "Магазин 13"): 5,
#         ("Склад 4", "Магазин 14"): 10,
# }

    sources = [0, 1]  # Індекси терміналів
    sinks = list(range(6, 20))  # Індекси магазинів: 6 до 19

    total_flow = 0
    flow_details = []  # Для зберігання інформації про потоки

    for s in [0, 1]:  # Термінали 0 та 1
        for t in range(6, 20):  # Магазини 1–13 — індекси 6 до 19
            flow = edmonds_karp(capacity_matrix, s, t)
            total_flow += flow
            flow_details.append(f"Термінал {s+1} → Магазин {t-5}: Потік = {flow}")  # Додаємо інформацію у вигляді рядка

    # Вивести всі варіанти потоку
    for detail in flow_details:
        print(detail)

    # Вивести загальний потік
    print(f"Загальний потік: {total_flow}")