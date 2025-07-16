# test-align

一个简单的Python冒泡排序实现。

## 项目介绍
该项目提供了一个基本的冒泡排序算法实现，用于对整数数组进行排序。

## 使用方法

### 直接运行
```bash
python bubble_sort.py
```

### 作为模块导入
```python
from bubble_sort import bubble_sort

my_array = [34, 12, 45, 6, 23]
sorted_array = bubble_sort(my_array)
print(sorted_array)
```

## 算法说明
冒泡排序是一种简单的排序算法，它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

## 示例输出
```
原始数组: [64, 34, 25, 12, 22, 11, 90]
排序后数组: [11, 12, 22, 25, 34, 64, 90]
```