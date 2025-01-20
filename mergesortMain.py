from merge_sort import mSort

n = int(input("How many values: "))
arr = []
for i in range(n):
    arr.append(int(input(f"{i + 1}: ")))
print("Result:", mSort(arr).srt())
