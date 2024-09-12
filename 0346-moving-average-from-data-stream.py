from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.window_sum = 0
        self.queue = deque()

    def next(self, n: int) -> float:
        self.window_sum += n
        self.queue.append(n)

        if len(self.queue) > self.window_size:
            self.window_sum -= self.queue.popleft()

        return self.window_sum / len(self.queue)


ma = MovingAverage(3)
print(ma.next(1))  # 1.0
print(ma.next(10))  # 5.5
print(ma.next(3))  # 4.66667
print(ma.next(5))  # 6.0
