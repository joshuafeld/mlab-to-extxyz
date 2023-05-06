class Atom:
    """
    Represents an atom.

    ...

    Attributes
    ----------
    species : str
        The species (chemical symbol).
    pos : list[float]
        The position in Cartesian coordinates (given in Angstrom).
    forces : list[float]
        The forces (in eV/Angstrom).
    """
    
    def __init__(self, species: str, pos: list[float], forces: list[float]):
        """
        Parameters
        ----------
        species : str
            The species (chemical symbol).
        pos : list[float]
            The position in Cartesian coordinates (given in Angstrom).
        forces : list[float]
            The forces (in eV/Angstrom).
        """

        self.species = species
        self.pos = pos
        self.forces = forces
