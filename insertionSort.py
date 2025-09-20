# InsertionSort.py
class InsertionSort:
    @staticmethod
    def sort(data, col, ascending=True):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and ((ascending and data[j][col] > key[col]) or (not ascending and data[j][col] < key[col])):
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        return data
