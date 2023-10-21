class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

    return True

# Пример использования
# Создаем связанный список с циклом
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Цикл

result = has_cycle(node1)
print("Есть ли цикл в списке?", result)
