class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
def reverse_list(node: Node):
    if node is None or node.next is None:
        return node

    previous_node = None

    current_node = node

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


# розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
def insertion_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head

    while current is not None:
        next_node = current.next

        if sorted_head is None or sorted_head.data > current.data:
            current.next = sorted_head
            sorted_head = current
        else:
            current_sorted = sorted_head
            while current_sorted.next is not None and current_sorted.next.data < current.data:
                current_sorted = current_sorted.next
            current.next = current_sorted.next
            current_sorted.next = current

        current = next_node

    return sorted_head


# написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
def merge_sorted_lists(list_a: Node, list_b: Node):
    if list_a is None:
        return list_b
    if list_b is None:
        return list_a

    merged_result = None
    current = None

    while list_a is not None and list_b is not None:
        if list_a.data < list_b.data:
            if merged_result is None:
                merged_result = list_a
                current = merged_result
            else:
                current.next = list_a
                current = current.next
            list_a = list_a.next
        else:
            if merged_result is None:
                merged_result = list_b
                current = merged_result
            else:
                current.next = list_b
                current = current.next
            list_b = list_b.next

    if list_a is not None:
        current.next = list_a
    elif list_b is not None:
        current.next = list_b

    return merged_result


if __name__ == '__main__':
    print("Test reverse_list:")
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)

    current = node

    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print(" ")

    reversed_node = reverse_list(node)

    current = reversed_node

    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print(" ")

    print("Test insertion_sort:", end='\n')
    # Створюємо однозв'язний список
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(5)

    # Виводимо початковий список
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print(" ")

    # Сортуємо список вставками
    sorted_head = insertion_sort_linked_list(head)

    # Виводимо відсортований список
    current = sorted_head
    while current is not None:
        print(current.data, end=' ')
        current = current.next

    print(" ")


    print("Test merge_sorted_lists:")

    # Створюємо перший відсортований список
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

    # Створюємо другий відсортований список
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    # Об'єднуємо два відсортовані списки
    merged_list = merge_sorted_lists(l1, l2)

    # Виводимо об'єднаний список
    current = merged_list
    while current is not None:
        print(current.data, end=' ')
        current = current.next