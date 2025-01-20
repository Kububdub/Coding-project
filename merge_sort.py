class mSort:
    def __init__(self, arr):
        self.a = arr

    def srt(self):
        if len(self.a) > 1:
            self._ms(0, len(self.a) - 1)
        return self.a

    def _ms(self, l, r):
        if l < r:
            m = (l + r) // 2
            self._ms(l, m)
            self._ms(m + 1, r)
            self._mrg(l, m, r)

    def _mrg(self, l, m, r):
        L = self.a[l:m + 1]
        R = self.a[m + 1:r + 1]
        i = 0
        j = 0
        k = l
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                self.a[k] = L[i]
                i += 1
            else:
                self.a[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            self.a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            self.a[k] = R[j]
            j += 1
            k += 1
