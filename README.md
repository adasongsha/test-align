# test-align

一个包含排序算法和Transformer组件的Python实现集合。

## 项目介绍
该项目提供了基本的排序算法实现和Transformer模型的Multi-Head Attention组件，用于学习和教学目的。

## 功能列表
- 冒泡排序算法实现
- 快速排序算法实现
- Transformer Multi-Head Attention (KVQ)实现

## 使用方法

### 排序算法

#### 冒泡排序
```bash
python bubble_sort.py
```

```python
from bubble_sort import bubble_sort

my_array = [34, 12, 45, 6, 23]
sorted_array = bubble_sort(my_array)
print(sorted_array)
```

#### 快速排序
```bash
python quick_sort.py
```

```python
from quick_sort import quick_sort

my_array = [34, 12, 45, 6, 23]
sorted_array = quick_sort(my_array)
print(sorted_array)
```

### Transformer Multi-Head Attention

```bash
python transformer_mht.py
```

```python
from transformer_mht import MultiHeadAttention
import numpy as np

# 超参数
d_model = 512
num_heads = 8
batch_size = 2
seq_len = 10

# 创建多头注意力实例
mha = MultiHeadAttention(d_model, num_heads)

# 随机输入张量
Q = np.random.randn(batch_size, seq_len, d_model)
K = np.random.randn(batch_size, seq_len, d_model)
V = np.random.randn(batch_size, seq_len, d_model)

# 前向传播
output, attn_weights = mha.forward(Q, K, V)

print(f"输入形状: {Q.shape}")
print(f"输出形状: {output.shape}")
print(f"注意力权重形状: {attn_weights.shape}")
```

## 算法说明

### 冒泡排序
冒泡排序是一种简单的排序算法，它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

### 快速排序
快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行。快速排序又是一种分而治之思想在排序算法上的典型应用。

### Transformer Multi-Head Attention
多头注意力机制是Transformer模型的核心组件，它允许模型同时关注输入序列的不同位置和不同表示子空间的信息。

该实现包含：
- 线性变换将输入映射到Q、K、V矩阵
- 分割到多个注意力头
- 缩放点积注意力计算
- 合并注意力头并进行输出变换

## 示例输出

### 排序算法
```
原始数组: [64, 34, 25, 12, 22, 11, 90]
排序后数组: [11, 12, 22, 25, 34, 64, 90]
```

### Transformer Multi-Head Attention
```
输入形状: (2, 10, 512)
输出形状: (2, 10, 512)
注意力权重形状: (2, 8, 10, 10)
```