import heapq
import math


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.hypot(x1 - x2, y1 - y2)


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def shortest_path(M, start, goal):
    print("shortest path called")
    if start == goal:
        return [start]

    intersections = M.intersections
    roads = M.roads

    open_heap = []  # priority queue ordered by f-score
    heapq.heappush(open_heap, (0, start))
    came_from = {}  # backpointers
    g_score = {start: 0}  # cost from start
    f_score = {start: heuristic(intersections[start], intersections[goal])}  # est. total cost
    open_set = {start}  # fast membership check

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return reconstruct_path(came_from, current)
        open_set.discard(current)

        for neighbor in roads[current]:
            # cost to neighbor through current
            tentative_g = g_score[current] + heuristic(intersections[current], intersections[neighbor])
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(intersections[neighbor], intersections[goal])
                if neighbor not in open_set:
                    heapq.heappush(open_heap, (f_score[neighbor], neighbor))
                    open_set.add(neighbor)

    return None  # no path found
