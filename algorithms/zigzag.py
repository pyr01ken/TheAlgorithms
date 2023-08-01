"""
[[1,2,3,4,5], [6,7,8,9,10]] => [1,2,3,4,5,6,7,8,9,10]

"""

class ZigZag:
    def __init__(self, ls1, ls2):
        self.queue = [ls1, ls2]

    def next(self):
        v = self.queue.pop(0)
        s = v.pop(0)
        if v:
            self.queue.append(v)
        return s

    def has_next(self):
        return True if self.queue else False

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

z = ZigZag(list1, list2)
list_nums = []

while z.has_next():
    list_nums.append(z.next())

print(list_nums)