# CountingSort.py
class CountingSort:
    @staticmethod
    def sort(data, col, ascending=True):
        if not data:
            return data

        max_val = max(p[col] for p in data)
        min_val = min(p[col] for p in data)
        rango = max_val - min_val + 1

        count = [0] * rango
        output = [None] * len(data)

        for p in data:
            count[p[col] - min_val] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for p in reversed(data):
            idx = p[col] - min_val
            output[count[idx] - 1] = p
            count[idx] -= 1

        if ascending:
            for i in range(len(data)):
                data[i] = output[i]
        else:
            for i in range(len(data)):
                data[i] = output[len(data)-1-i]
        return data
