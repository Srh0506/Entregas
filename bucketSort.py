# BucketSort.py
class BucketSort:
    @staticmethod
    def sort(data, col, ascending=True):
        if not data:
            return data

        max_val = max(p[col] for p in data)
        size = max_val // len(data) + 1

        buckets = [[] for _ in range(len(data))]
        for p in data:
            idx = p[col] // size
            buckets[idx].append(p)

        for b in buckets:
            b.sort(key=lambda x: x[col])

        result = []
        for b in buckets:
            result.extend(b)

        if not ascending:
            result.reverse()

        for i in range(len(data)):
            data[i] = result[i]
        return data
