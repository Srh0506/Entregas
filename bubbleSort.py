# BubbleSort.py
class BubbleSort:
    @staticmethod
    def sort(data, col, ascending=True):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if ascending:
                    if data[j][col] > data[j+1][col]:
                        data[j], data[j+1] = data[j+1], data[j]
                else:
                    if data[j][col] < data[j+1][col]:
                        data[j], data[j+1] = data[j+1], data[j]
        return data
