# https://www.acmicpc.net/problem/11279 ÃÖ´ë Èü

from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
queue = PriorityQueue()
for _ in range(N):
    Num = int(input())
    if Num == 0:
        if queue.empty():
            print(0)
        else:
            print(-1 * queue.get())
    else:
        queue.put((-Num))
