class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, target):
        """
        在链表中查找目标值
        :param target: 要查找的值
        :return: 如果找到返回True，否则返回False
        """
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


# 测试代码
if __name__ == '__main__':
    # 创建链表
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(5)
    ll.append(7)
    ll.append(9)

    print("链表内容:")
    ll.print_list()

    # 测试查找功能
    target = 5
    found = ll.search(target)
    print(f"查找值 {target}: {'找到' if found else '未找到'}")

    target = 4
    found = ll.search(target)
    print(f"查找值 {target}: {'找到' if found else '未找到'}")