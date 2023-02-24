
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    
    """  Se supone que esto encuentra al ancestro comun mas profundo
    de dos nodos en un arbol binario, se supone devuelve el nodo y sino hay pues manda None

    Args:
        root (Node): La raíz del árbol binario.
        node1 (Node): Nodo que se quiere buscar en el arbol apra buscancer el ancestro mas profundo
        node2 (Node):Nodo que se quiere buscar en el arbol apra buscancer el ancestro mas profundo

    ##Encontre el codigo en chatgpt :) 
    """

    if root is None:
        return None

    # si root es uno de los nodos, devolver root
    if root == node1 or root == node2:
        return root

    if root == node1 and root != node2:
        return f"los nodos deben pertenecer al arbol"
    
    left = find_lca(root.left, node1, node2)
    right = find_lca(root.right, node1, node2)

    # si ambos nodos están en diferentes subárboles, devolver la raíz
    if left and right:
        return root

    return left if left else right


print("su arbolito es:")
"""
tree = BTS()
root = Nodo('A')

root.left = Nodo('B')

root.left.left = Nodo('D')
root.left.left.left = Nodo('H')
root.left.left.right = Nodo('I')

root.left.right = Nodo('E')
root.left.right.left = Nodo('J')
root.left.right.right = Nodo('K')

root.right = Nodo('C')

root.right.left = Nodo('F')
root.right.left.left = Nodo('L')

root.right.right = Nodo('G')
"""
# crear el árbol
root = Node('A')

root.left = Node('B')

root.left.left = Node('D')
root.left.left.left = Node('H')
root.left.left.right = Node('I')

root.left.right = Node('E')
root.left.right.left = Node('J')
root.left.right.right = Node('K')

root.right = Node('C')

root.right.left = Node('F')
root.right.left.left = Node('L')

root.right.right = Node('G')

# encontrar el ancestro común más profundo de 4 y 5
node1 = root.right.left.left
node2 = root.right.right
lca = find_lca(root, node1, node2)

node3 = root.right
node4 = root.right.right
lca1 = find_lca(root, node3, node4)


node5 = root.left.left.left
node6 = root.left.right.left
lca2 = find_lca(root, node5, node6)


node7 = root.left
node8 = root.right.left.left
Ica3 = find_lca(root, node7, node8)


# imprimir el resultado
print("Ancestro común más profundo de", node1.data, "y", node2.data, "es", lca.data)
print("Ancestro común más profundo de", node3.data, "y", node4.data, "es", lca1.data)
print("Ancestro común más profundo de", node5.data, "y", node6.data, "es", lca2.data)
print("Ancestro común más profundo de", node7.data, "y", node8.data, "es", Ica3.data)









