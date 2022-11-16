#Placeholder for qiskit implementation of a node architecture
import itertools

class Node(object):
    id_obj = itertools.count()
    def __init__(self,node_name, timeline):
        #reference will be sequence/topology/node & QuNetSim/Component/host
        #logger
        #time_line, what time the node will be create

        #node_id
        self.node_id = Node.id_obj # will replace to uuid4().int for future use in large network
        #node_name
        self.node_name = node_name #this is like 
        #node_classical_channel, we will use rustworkx, to speed up, also it may apply qiskit optimization in the future, for applying other related algorithm in qiskit ecosystem.
        self.classical_channel = {}
        #node_quantum_channel
        self.quantum_channel = {}
        #classical storage
        self.classical_storage = None
        #quantum storage
        self.quantum_storage = None
        #component, for future use for create other type of node
        self.components = {}
    
    def add_connection(self):
        """
        adding quantum_channel or classical_channel to the specific node
        """
        pass
    def delete_connection(self):
        pass

    def send_message(self):
        """
        how it receive classical message, will include in protocols.py
        """
        pass
    def receive_message(self):
        """
        how it receive classical message, will include in protocols.py
        """
        pass

class CustomNode():
    """
    this will be custom circuit input as startup
    """

class QKDNode():
    """
    Quantum Key Distribution Node
    """

