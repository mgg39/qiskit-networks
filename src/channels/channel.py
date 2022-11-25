#TODO: channel noise &/or distance dependecy

class Channel:
    """
    Object class for the empty Nodes.
    """

    def __init__(self, name: str, nodes: list, nature: str):
        """
        Constructor of the channel.
        :param name: the name of the channel.
        :param connected nodes: name of nodes connected to the topology.
        """

        self.name = name
        """
        Set the name of the Node.
        """

        self.nodes = nodes
        """
        Set the nodes connected to the channel.
        """


    def get_name(self) -> str:

        """
        Return the name of the Node.
        """
        return self.name

    def get_nodes(self) -> list:

        """
        Return the name of all nodes connected to the channel.
        """

        return self.nodes

    def get_nature(self) -> str:

        """
        Return the nature of the channel: Quantum/Classic.
        """
        return self.get_nature
