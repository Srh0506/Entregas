# MergeSort.py
class MergeSort:
    @staticmethod
    def sort(data, col, ascending=True):
        if len(data) > 1:
            mid = len(data) // 2
            L = data[:mid]
            R = data[mid:]

            MergeSort.sort(L, col, ascending)
            MergeSort.sort(R, col, ascending)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if (ascending and L[i][col] <= R[j][col]) or (not ascending and L[i][col] >= R[j][col]):
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1
        return data
