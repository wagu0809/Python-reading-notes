class Stack(object):
#Stack 栈 或者 堆栈 一种串列形式的抽象数据结构 只允许在一端进行push和pop操作 先进后出（first in last out）
#这里使用python中的列表list来进行简单的压栈和出栈的实现
    def __init__(self):
        self.__stack_list = []

    def push(self, item): # 压栈
        self._stack_list.append(item)

    def pop(self): # 出栈
        return self._stack_list.pop()

    def size(self): # 返回该栈的长度
        return len(self._stack_list)

    def is_empty(self): # 判断该栈是否为空
        return self._stack_list is []

    def peek(self):  # 返回最后一个元素的值 但不删除 区别于pop
        if self.is_empty():
            return None
        else:
            return self._stack_list[-1]

    def print_all(self): # 将栈内所有元素打印
        for elem in self._stack_list:
            print(elem)
