from node import Nodo
from BinaryTree import BTS

print("Aquí adjunto el punto 2")

tree = BTS()
##Esta es la lista de valores que usare
values = [6, 4, 5, 2, 9, 8, 7, 10]
##Aquí inserto los valores de la lista al arbol
tree.insert_several(values)
min = tree.min()
max = tree.max()
print("--MINIMO--")
print("El menor valor del arbol es: " ,min )
print("El nivel donde se ecuentra es: " , tree.get_node_level(min) )


print("--MAXIMO--")
print("El mayor valor del arbol es: " ,max )
print("El nivel donde se ecuentra es: " , tree.get_node_level(max) )



