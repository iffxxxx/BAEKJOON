# https://www.acmicpc.net/problem/1927 ÃÖ¼Ò Èü

from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
queue = PriorityQueue()
for _ in range(N):
    Num = int(input())
    if Num == 0:
        if queue.empty():   # queue.qsize() == 0
            print(0)
        else:
            print(queue.get())
    else:
        queue.put(Num)