import os
import random

class Icosahedron:
    """
    Model for stellated icosahedra.
    """
    @staticmethod
    def find(icosahedron_id):
        """
        Find STL file for stellated icosahedron with given id.
        Args:
            icosahedron_id (str): id of the icosahedron.
        Returns:
            str: file path of the STL file.
        """
        file_path = f"stl/icosahedra/{icosahedron_id}.stl"
        if os.path.exists(file_path):
            return file_path
        return None

    @staticmethod
    def random():
        """
        Find STL file for a random stellated icosahedron.
        Returns:
            str: file path of the STL file.
        """
        directory = 'stl/icosahedra'
        icosahedra = [os.path.join(directory, f) for f in os.listdir(directory)]
        file_path = random.choice(icosahedra)
        return file_path
    