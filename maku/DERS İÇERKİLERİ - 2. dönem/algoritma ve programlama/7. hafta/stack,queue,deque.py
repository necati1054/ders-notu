def reverse_list_with_stack(lst):
    reversed_list = []
    while lst:
        reversed_list.append(lst.pop())
    return reversed_list

# Örnek kullanım:
my_list = [1, 2, 3, 4, 5]
print("Orjinal Liste:", my_list)
print("Tersine Çevrilmiş Liste:", reverse_list_with_stack(my_list))


# def find_pairs(nums, target):
#     seen = {}
#     pairs = []
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             pairs.append((complement, num))
#         seen[num] = True
#     return pairs

# # Örnek kullanım:
# print(find_pairs([1, 3, 7, 9, 2], 10))  # [(1, 9), (3, 7)]
# print(find_pairs([4, 5, 6, 8], 10))     # [(4, 6)]
