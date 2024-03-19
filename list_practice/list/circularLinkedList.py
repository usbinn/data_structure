from list.listNode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def insert(self, i: int, newItem):
        if 0 <= i <= self.__numItems:
            if i == self.__numItems:
                self.append(newItem)
            else:
                prev = self.getNode(i - 1)
                newNode = ListNode(newItem, prev.next)
                prev.next = newNode
                self.__numItems += 1

    def append(self, newItem):
        prev = self.__tail
        newNode = ListNode(newItem, self.__tail.next)
        prev.next = newNode
        self.__tail = newNode
        self.__numItems += 1

    def pop(self, *args):
        if len(args) != 0:
            i = args[0]
        else:
            i = -1

        if i < 0:
            i = self.__numItems - 1

        if 0 <= i < self.__numItems:
            if i == 0:
                retItem = self.__tail.next.item
                self.__tail.next = self.__tail.next.next
                self.__numItems -= 1
                return retItem
            else:
                prev = self.getNode(i - 1)
                retItem = prev.next.item
                prev.next = prev.next.next
                if i == self.__numItems - 1:
                    self.__tail = prev
                self.__numItems -= 1
                return retItem
        else:
            return None

    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr is not None:
            prev.next = curr.next
            if curr == self.__tail:
                self.__tail = prev
            self.__numItems -= 1
            return x
        else:
            return None

    def get(self, i: int):
        if 0 <= i < self.__numItems:
            return self.getNode(i).item
        else:
            return None

    def index(self, x) -> int:
        curr = self.__tail.next
        index = 0
        while curr != self.__tail:
            if curr.item == x:
                return index
            index += 1
            curr = curr.next
        if curr.item == x:
            return index
        return -2

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__tail.next = self.__tail
        self.__numItems = 0

    def count(self, x) -> int:
        cnt = 0
        curr = self.__tail.next
        while curr != self.__tail:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        if curr.item == x:
            cnt += 1
        return cnt

    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))

    def copy(self):
        a = CircularLinkedList()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a

    def reverse(self):
        a = CircularLinkedList()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))

    def sort(self) -> None:
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])

    def __findNode(self, x):
        prev = None
        curr = self.__tail.next
        while curr != self.__tail:
            if curr.item == x:
                return prev, curr
            prev = curr
            curr = curr.next
        return None, None

    def getNode(self, i: int) -> ListNode:
        curr = self.__tail.next
        for _ in range(i+1):
            curr = curr.next
        return curr

    def printList(self):
        curr = self.__tail.next.next
        while curr != self.__tail.next:
            print(curr.item, end=' ')
            curr = curr.next
        print()

    def __iter__(self):
        return CircularLinkedListIterator(self)
    
class CircularLinkedListIterator:
    def __init__(self,alist) -> None:
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
