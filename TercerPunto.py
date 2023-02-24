from typing import List

class Nodo:
    def __init__(self, value: int) -> None:
        """Nodo del arbol y su informacion, se inicializa los valores, y los hijos
        izquierdos y derechos como None y la altura que yo uso es 1, aunque aqui realmente no usare eso

       
        """
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return  f" {self.value}"

class BTS:

##Raiz  
    def __init__(self) :
    
        self.root = None 
## Insert individual, manual , list

    def insert(self, value):
        """
        esto inserta los datos al arbol

        Args:
            value: este es el valor del nodo
        """
        new = Nodo(value)
        if self.root is None:
            self.root = new
        else:
            self.insert_recursive(new, self.root)
    
    def insert_several(self, list_value: list ):
        """
        Esto lo que hace es que de acuerdo a valores agregados en una lista
        previamente, se insertan recurisvamente con la funcion insert

        Args:
            list_value : estos son los valores de nuestro arbol 
        """
        for value in list_value:
            self.insert(value)
    
    def insert_recursive(self, new:Nodo, current:Nodo):
        """
        Esta es la función recursiva que se encarga de se insertar los valores al
        arbol

        Args:
            new : Nodo nuevo
            current : nodo donde se encuentra
        """
        if new.value < current.value:
            if current.left is None:
                current.left = new
            else:
                self.insert_recursive(new,current.left)
        else :
            if current.right is None:
                current.right = new
            else: 
                self.insert_recursive(new, current.right)
        current.height = 1 + max(self.get_hight(current.left), self.get_hight(current.right))## Buscar 
        
 ##RECORRIDOS
    def InOrderPrint(self, current:Nodo):
        """
        Esta funcion se encarga de recorrer los valores del arbol
        siguiendo el siguiente orde : left -root - right

        Args:
            current (Nodo):actual
        """
        if current is None:
            return
        else:
            self.InOrderPrint(current.left)
            print(current , end=' ')
            self.InOrderPrint(current.right)
            
    def PreOrderPrint(self, current):
        """
        Esta funcion se encarga de recorrer los valores del arbol
        siguiendo el siguiente orde : root - left - right

        Args:
            current (Nodo):actual
        """
        if current is None:
            return
        else:
            print(current, end=' ')
            self.PreOrderPrint(current.left)
            self.PreOrderPrint(current.right)

    def PostOrderPrint(self, current):
        
        """
        Esta funcion se encarga de recorrer los valores del arbol
        siguiendo el siguiente orde :  left - right - root

        Args:
            current (Nodo):actual
        """
        if current is None:
            return
        else:
            self.PostOrderPrint(current.left)
            self.PostOrderPrint(current.right)
            print(current, end=' ') 

print("Aquí inserto el arbol")
tree = BTS()
tree.root = Nodo(10)
tree.root.left = Nodo(26)
tree.root.left.left = Nodo(2)
tree.root.left.right = Nodo(38)
tree.root.left.left.left = Nodo(14)
tree.root.left.left.right = Nodo(66)

tree.root.right = Nodo(7)
tree.root.right.right= Nodo(107)
tree.root.right.right.right= Nodo(5)
tree.root.right.right.right.right= Nodo(4)
tree.root.right.right.right.right.left= Nodo(5)
tree.root.right.right.left= Nodo(4)
tree.root.right.right.left.left= Nodo(12)


print("Aquí estan los recorridos del arbol")

"""
La forma en que muestro el arbol es a partir del número de canciones de 
cada usuario, sin embargo, la forma que use para organizarlo ya que no entendia
como estan dirigidas esas linda flechas, fue usando los numeros proporcionados por
el "the mean musical positiveness"


"""
print("Arbol   - InOrder")
tree.InOrderPrint(tree.root)
print("\nArbol - PreOrder")
tree.PreOrderPrint(tree.root)
print("\nArbol - PostOrder")
tree.PostOrderPrint(tree.root)
print()

