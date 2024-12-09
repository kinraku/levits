import collections

# Представление графа в виде списка рёбер
class Graph:
    def __init__(self, vertices: int) -> None:
        self.V = vertices  # Количество вершин в графе
        self.graph = []    # Список рёбер

    def add_edge(self, u: int, v: int, w: int) -> None:
        self.graph.append([u, v, w])  # Добавить ребро (u -> v) с весом w

def levit(graph: Graph, start: int = 0):
    # Вершины, расстояние до которых и их соседей уже рассчитано
    m0 = []
    # Вершины, которые нужно обработать (очередь)
    m1 = collections.deque()
    # Вершины, до которых путь ещё не найден
    m2 = [x for x in range(graph.V)]

    # Инициализация
    m1.append(m2.pop(start))  # Перенос стартовой вершины из m2 в m1

    dist = [float('inf')] * graph.V  # Начальные расстояния (бесконечность)
    dist[start] = 0  # Расстояние до стартовой вершины равно 0

    pred = [-1] * graph.V  # Родительские вершины
    pred[start] = None  # Для стартовой вершины родителя нет

    while m1:
        # Извлечь вершину из m1 для обработки
        current = m1.popleft()

        for u, v, w in graph.graph:
            if u == current:
                # Если путь к вершине ещё не найден
                if v in m2:
                    dist[v] = dist[u] + w
                    m2.remove(v)  # Удалить из m2
                    m1.append(v)  # Добавить в m1
                    pred[v] = u

                # Если вершина уже в очереди на обработку
                elif v in m1:
                    # Проверка на более короткий путь
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u

                # Если вершина уже обработана
                elif v in m0:
                    # Проверка на более короткий путь
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        # Перенос вершины обратно в m1 для перерасчёта
                        m0.remove(v)
                        m1.appendleft(v)

        # Добавить текущую вершину в m0
        m0.append(current)

    return dist, pred  # Вернуть расстояния и родительские вершины

# Тестовые графы
graph1 = Graph(5)
graph1.add_edge(0, 1, 2)
graph1.add_edge(0, 2, 4)
graph1.add_edge(1, 2, 1)
graph1.add_edge(1, 3, 7)
graph1.add_edge(2, 4, 3)

graph2 = Graph(4)
graph2.add_edge(0, 1, 1)
graph2.add_edge(1, 2, 2)
graph2.add_edge(2, 3, 1)
graph2.add_edge(3, 0, 5)

graph3 = Graph(6)
graph3.add_edge(0, 1, 2)
graph3.add_edge(0, 2, 4)
graph3.add_edge(1, 2, 1)
graph3.add_edge(1, 3, 7)
graph3.add_edge(2, 4, 3)
graph3.add_edge(3, 5, 1)
graph3.add_edge(4, 5, 6)

# Вывод результатов
print("Граф 1:", levit(graph1, start=0))
print("Граф 2:", levit(graph2, start=0))
print("Граф 3:", levit(graph3, start=0))
