# RadixSort.py
class RadixSort:
    @staticmethod
    def sort(data, col, ascending=True):
        if not data:
            return data

        max_val = max(p[col] for p in data)
        exp = 1
        while max_val // exp > 0:
            RadixSort.counting_sort_exp(data, col, exp, ascending)
            exp *= 10
        return data

    @staticmethod
    def counting_sort_exp(data, col, exp, ascending):
        n = len(data)
        output = [None] * n
        count = [0] * 10

        for p in data:
            idx = (p[col] // exp) % 10
            count[idx] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

        for p in reversed(data):
            idx = (p[col] // exp) % 10
            output[count[idx] - 1] = p
            count[idx] -= 1

        if ascending:
            for i in range(n):
                data[i] = output[i]
        else:
            for i in range(n):
                data[i] = output[n-1-i]
