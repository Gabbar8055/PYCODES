#!/usr/bin/python


def get_lists(soldiers):
    "get both ranks and distance lists"
    ranks = list(range(1, soldiers+1))
    distances = list(map(int, input().split()))
    return ranks, distances


def rotate(ranks, index, distance):
    "move soldier distance to the left to index"
    if distance == 0:
        return ranks

    position = index-distance
    rank = ranks[position]
    del(ranks[position])
    ranks.insert(index, rank)
    return ranks


N = int(input())
while N > 0:
    soldiers = int(input())
    ranks, distances = get_lists(soldiers)
    for i in range(soldiers-1, -1, -1):
        ranks = rotate(ranks, i, distances[i])
    print(*ranks)
    N -= 1
