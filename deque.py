"""
Módulo Collections: Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performance.


"""

# Fezendo o import

from collections import deque

# Criando deque

deq = deque('leonardo')

print(deq)

# Adicionando elementos no deque

deq.append('u')  # Adiciona no deque

print((deq))

deq.appendleft('c')  # Adiciona no começo

print(deq)

# Remover elementos

print(deq.pop())  # Vai remover e retornar o o último elemento.

print(deq)

print((deq.popleft()))

print(deq)
