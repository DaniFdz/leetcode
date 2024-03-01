from dataclasses import dataclass

@dataclass
class StackElement:
    def __init__(self, val = None, prev = None):
        self.val = val
        self.prev = prev

class MinStack:
    def __init__(self):
        self.__head = None
        self.__min = []

    def push(self, val: int) -> None:
        if len(self.__min) == 0 or val <= self.__min[-1]:
            self.__min.append(val)
        self.__head = StackElement(val=val, prev=self.__head)

    def pop(self) -> None:
        if self.__head != None:
            if len(self.__min) > 0 and self.__head.val == self.__min[-1]:
                self.__min.pop()
            self.__head = self.__head.prev


    def top(self) -> int:
        return self.__head.val


    def getMin(self) -> int:
        return self.__min[-1]


if __name__ == '__main__':
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    assert minStack.getMin() == -3
    minStack.pop();
    assert minStack.top() == 0
    assert minStack.getMin() == -2
