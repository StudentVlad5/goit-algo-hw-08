# Завдання 1
#  Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів. Тобто починати потрібно з кабелів з найменьшою довжиною.

import heapq

def min_total_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # З’єднуємо їх
        cost = first + second
        total_cost += cost
        
        # Поміщаємо результат назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад
cable_lengths = [4, 3, 2, 6]
print(min_total_cost(cable_lengths))  # Виведе: 29

# Ініціалізація купи: O(n)
# Кожна операція злиття: O(log n)
# Загалом: O(n log n)

# Завдання 2

import heapq

def merge_k_lists(lists):
    heap = []
    
    # 1. Додаємо перші елементи кожного списку в купу
    #  Створюємо порожню купу (мін-купа). Вона буде зберігати кортежі: (значення, індекс_списку, індекс_елемента).
    for i, lst in enumerate(lists):
        if lst:  # перевірка, чи список не порожній
            heapq.heappush(heap, (lst[0], i, 0))
            # print("heap", heap)
    result = []
    
    # 2. Поки є елементи в купі
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        # print(val, list_idx, element_idx)
        result.append(val)
        
        # 3. Якщо в цьому списку ще є елементи — додаємо наступний
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
    
    return result

# Тест
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
