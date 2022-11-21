import numpy as np
import qiskit

class Node:
    """
    Object class for the empty Nodes.
    """

    def __init__(self, name: str, location: list, elements: list, ports: list):
        """
        Constructor of the Node.
        :param name: the name of the Node.
        :param location: defined location of the Node within a topology.
        :param elements: list of network elements within the Node.
        :param ports: list of ports within the Node.
        """

        self.name = name
        """
        Set the name of the Node.
        """

        self.location = location
        """
        Set the location address of the Node.
        """


    def get_name(self) -> str:

        """
        Return the name of the Node.
        """
        return self.name

    def get_location(self) -> list:

        """
        Return the location address of the Node.
        Should be described as a 2D or 3D array.
        """

        if len(self.location) == 2:
            self.dimension_topology = 2
        elif len(self.location) == 3:
            self.dimension_topology = 3
        else:
            self.dimension_topology = np.nan
            print("Node.location has an incorrect dimensionality. Please define the location through the use of a 2D or a 3D grid system.")

        return self.location

    def elements(self) -> list:

        """
        Return the list of element within the Node.
        """
        return self.elements

    def ports(self) -> list:

        """
        Return ports within the Node.
        """
        return self.ports
