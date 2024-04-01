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
        icosahedra = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
        ]
        file_path = random.choice(icosahedra)
        return file_path

class FaceRegion:
    """
    Model for the face regions of stellated icosahedra.
    """
    _REGIONS = [
        # reflexible face regions
        "00", "10", "20", "30", "40", "50", "60", 
        "70", "80", "90", "a0", "b0", "c0", "d0",
        # non-reflexible face regions
        "51", "52", "61", "62", "91", "92", "a1", "a2"
    ]

    @staticmethod
    def find(region_id):
        """
        Find STL file for face region with given id.
        Args:
            region_id (str): id of the face region.
        Returns:
            str: file path of the STL file.
        """
        file_path = f"stl/faces/{region_id}.stl"
        if os.path.exists(file_path):
            return file_path
        return None

    @staticmethod
    def random():
        """
        Find STL file for a random face region.
        Returns:
            str: file path of the STL file.
        """
        directory = 'stl/faces'
        faces = [os.path.join(directory, f) for f in os.listdir(directory)]
        file_path = random.choice(faces)
        return file_path
