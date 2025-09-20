# QuickSort.py
class QuickSort:
    @staticmethod
    def sort(data, col, ascending=True):
        QuickSort._quick_sort(data, 0, len(data)-1, col, ascending)
        return data

    @staticmethod
    def _quick_sort(data, low, high, col, ascending):
        if low < high:
            pi = QuickSort.partition(data, low, high, col, ascending)
            QuickSort._quick_sort(data, low, pi-1, col, ascending)
            QuickSort._quick_sort(data, pi+1, high, col, ascending)

    @staticmethod
    def partition(data, low, high, col, ascending):
        pivot = data[high][col]
        i = low - 1
        for j in range(low, high):
            if (ascending and data[j][col] <= pivot) or (not ascending and data[j][col] >= pivot):
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i+1], data[high] = data[high], data[i+1]
        return i+1
