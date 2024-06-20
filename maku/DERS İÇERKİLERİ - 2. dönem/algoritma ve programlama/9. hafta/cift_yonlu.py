# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node
#             new_node.prev = current_node

#     def print_forward(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=' <-> ')
#             current_node = current_node.next
#         print("None")

#     def print_backward(self):
#         current_node = self.head
#         while current_node and current_node.next:
#             current_node = current_node.next
        
#         while current_node:
#             print(current_node.data, end=' <-> ')
#             current_node = current_node.prev
#         print("None")

# # Çift yönlü bağlı listeyi oluştur
# doubly_linked_list = DoublyLinkedList()

# # Elemanları ekleyelim
# doubly_linked_list.append(1)
# doubly_linked_list.append(2)
# doubly_linked_list.append(3)

# # İleri yönlü bağlı listeyi yazdıralım
# print("İleri Yönlü:")
# doubly_linked_list.print_forward()

# # Geriye doğru bağlı listeyi yazdıralım
# print("\nGeriye Doğru:")
# doubly_linked_list.print_backward()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def print_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' <-> ')
            current_node = current_node.next
        print("None")

    def print_backward(self):
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        
        while current_node:
            print(current_node.data, end=' <-> ')
            current_node = current_node.prev
        print("None")
    
    def insert_after(self, target_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                new_node = Node(new_data)
                new_node.prev = current_node
                new_node.next = current_node.next
                if current_node.next:
                    current_node.next.prev = new_node
                current_node.next = new_node
                return
            current_node = current_node.next
        print(f"Node with data {target_data} not found.")

    def delete(self, target_data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:  # If head is to be deleted
                    self.head = current_node.next
                del current_node
                return
            current_node = current_node.next
        print(f"Node with data {target_data} not found.")

    def delete_last(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:  # If there's only one node
            del self.head
            self.head = None
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.prev.next = None
        del current_node

# Çift yönlü bağlı listeyi oluştur
doubly_linked_list = DoublyLinkedList()

# Elemanları ekleyelim
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)

# İleri yönlü bağlı listeyi yazdıralım
print("İleri Yönlü:")
doubly_linked_list.print_forward()

# Geriye doğru bağlı listeyi yazdıralım
print("\nGeriye Doğru:")
doubly_linked_list.print_backward()

# Araya ekleyelim
doubly_linked_list.insert_after(2, 2.5)
print("\n2'den sonra 2.5 eklendikten sonra İleri Yönlü:")
doubly_linked_list.print_forward()

# Aradan silelim
doubly_linked_list.delete(2.5)
print("\n2.5 silindikten sonra İleri Yönlü:")
doubly_linked_list.print_forward()

# Sondan silelim
doubly_linked_list.delete_last()
print("\nSon eleman silindikten sonra İleri Yönlü:")
doubly_linked_list.print_forward()
