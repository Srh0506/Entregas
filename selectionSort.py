# SelectionSort.py
class SelectionSort:
    @staticmethod
    def sort(data, col, ascending=True):
        n = len(data)
        for i in range(n):
            idx = i
            for j in range(i+1, n):
                if ascending:
                    if data[j][col] < data[idx][col]:
                        idx = j
                else:
                    if data[j][col] > data[idx][col]:
                        idx = j
            data[i], data[idx] = data[idx], data[i]
        return data
