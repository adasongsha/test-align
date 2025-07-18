import sys, os

def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for m in range(n):
        # 最后m个元素已经就位
        for j in range(0, n-m-1):
            # 从0到n-m-1遍历数组
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 示例用法
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    bubble_sort(test_array)
    print("排序后数组:", test_array)
