from node import Nodo

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
       

    
    def min(self):
        """Devuelve el valor mínimo en el árbol, utiliza la min_recursive, luego hace una comparación y si
        no encuentra nada en el arbol, es decir, esta vacio manda None
        """
        if self.root is None:
           return None
        else: return self.min_recursive(self.root)
       
    def min_recursive(self, current):
        """Esto devuelve el valor minimo que esta en el arbol usando el root actual, 
        es decir el current, y el movimiento que hace es desde el root hacia todos a la izquierda

        """
        if current.left is None:
            return current.value
        else: return self.min_recursive(current.left)
    
    def max(self):
        
        """Devuelve el valor máximo en el árbol, esto usa max_recus¿rsive y hace la misma comparacion que el min
        que si no hay nada en el arbol lanza None

        """
        if self.root is None:
           return None
        else:
           return self.max_recursive(self.root)
    
    
    
    def max_recursive(self, current):
        """
        Pasa el valor maximo del arbol con el root actual en current, moviendose desde
        el root hacia todos a la derecha
        
        """
        if current.right is None:
            return current.value
        else: return self.max_recursive(current.right)
        
    def get_nodes_by_level(self):
        
        """Devuelve un diccionario que contiene una lista de valores de nodo para cada nivel en el árbol, utilizo desde el nivel actual
        y los nodos los guardo en una lista, despues hago un condicional para que recorra todo el arbol suministradado a la lista y los agrego
        y despues muestro los valores del nodo, hago lo mismo con left y right y al final termina mostrando todos los recorridos que hay, esta vaina
        no la utilizo en el ejercicio pero weno, lo ve docuemntado bien en el lab :)
        """
        if self.root is None:
            return {}

        nodes_by_level = {}
        current_level = 1
        nodes_queue = [self.root]

        while nodes_queue:
            current_level_nodes = []
            nodes_in_queue = len(nodes_queue)

            for i in range(nodes_in_queue):
                current_node = nodes_queue.pop(0)
                current_level_nodes.append(current_node.value)

                if current_node.left:
                    nodes_queue.append(current_node.left)
                if current_node.right:
                    nodes_queue.append(current_node.right)

            nodes_by_level[current_level] = current_level_nodes
            current_level += 1

        for level, nodes in nodes_by_level.items():
            print(f"Level {level}: {nodes}")

        return nodes_by_level
    
    def get_node_level(self, value):
        """Devuelve el nivel del nodo con el valor especificado, se le suministra el valor a buscar y bueno retorna el nivel dle nodo
        especifico, si esa vaina no esta ahi entonces es None,

      
        """
        current = self.root
        level = 1
        while current is not None:
            if current.value == value:
                return level
            elif value < current.value:
                current = current.left
            else:
                current = current.right
            level += 1
        return None