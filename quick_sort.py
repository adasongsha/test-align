def quick_sort(arr):
    """
    使用快速排序算法对列表进行原地排序
    
    参数:
        arr: 需要排序的列表
    
    返回:
        排序后的列表（原地修改）
    """
    # 定义辅助函数进行原地分区
    def _partition(arr, low, high):
        # 选择最右侧元素作为基准值
        pivot = arr[high]
        # i是小于基准值区域的边界
        i = low - 1
        
        # 遍历数组，将小于基准值的元素交换到左侧区域
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # 将基准值放到正确位置（小于区域和大于区域之间）
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # 定义递归排序函数
    def _quick_sort_recursive(arr, low, high):
        if low < high:
            # 进行分区并获取基准值位置
            pivot_index = _partition(arr, low, high)
            
            # 递归排序基准值左侧子数组
            _quick_sort_recursive(arr, low, pivot_index - 1)
            # 递归排序基准值右侧子数组
            _quick_sort_recursive(arr, pivot_index + 1, high)
    
    # 创建输入数组的副本以避免修改原始输入
    arr_copy = arr.copy()
    # 开始递归排序
    _quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


# 示例用法
if __name__ == "__main__":
    # 测试数组
    test_array = [3, 6, 8, 10, 1, 2, 1]
    print("原始数组:", test_array)
    
    # 调用快速排序
    sorted_array = quick_sort(test_array)
    print("排序后数组:", sorted_array)
    
    # 验证排序结果
    assert sorted_array == sorted(test_array), "排序结果不正确！"
    print("排序验证成功！")