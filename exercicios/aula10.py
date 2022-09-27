"""
Sets em python (conjuntos)
um set em Python é uma coleção de itens únicos.

add (adiciona), update (atualiza), clear,
discard (remove o elemento se estiver presente, se não estiver ele ignora sem dar erro)
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

# Exemplo 1
numeros = [1, 2, 2, 3, 3, 3]
numeros_distintos = set(numeros)  # sets não aceita elementos duplicados, então não vai ser inserido
print("Números: ", numeros)
print("Números distintos: ", numeros_distintos)
print()

# Exemplo 2
nums = set([1, 2, 2, 3, 3, 3])
nums.remove(2)   # vai remover o item 2
print("Números: ", nums)
print()

# Exemplo 3
nums = set([1, 2, 2, 3, 3, 3])
nums.discard(4)    # vai ignorar
nums.discard(2)
print(nums)
print()

# Exemplo 4
nums1 = {1, 2, 3, 4, 5}
nums2 = {6, 7, 8, 9, 10}
nums3 = nums1 | nums2     # | essa função vai unir os dois elem

print(nums3)
print()

# Exemplo 5
nums1 = {1, 2, 3, 4, 5}
nums2 = {1, 2, 3, 4, 5, 6}
nums3 = nums1 & nums2  # todos os elementos presentes no sets

print(nums3)
