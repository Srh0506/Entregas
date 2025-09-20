# HeapSort.py
class HeapSort:
    @staticmethod
    def sort(data, col, ascending=True):
        n = len(data)

        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(data, n, i, col, ascending)

        for i in range(n-1, 0, -1):
            data[i], data[0] = data[0], data[i]
            HeapSort.heapify(data, i, 0, col, ascending)
        return data

    @staticmethod
    def heapify(data, n, i, col, ascending):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        def compare(a, b):
            return a > b if ascending else a < b

        if l < n and compare(data[l][col], data[largest][col]):
            largest = l
        if r < n and compare(data[r][col], data[largest][col]):
            largest = r

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            HeapSort.heapify(data, n, largest, col, ascending)
