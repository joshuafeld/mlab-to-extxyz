from ase import Atoms

import numpy as np

class Atom:
    """
    Represents an atom.

    ...

    Attributes
    ----------
    species : str
        The species (chemical symbol).
    pos : numpy.ndarray
        The position in Cartesian coordinates (given in Angstrom).
    forces : numpy.ndarray
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
        self.pos = np.array([pos])
        self.forces = np.array([forces])

    def to_ase(self) -> Atoms:
        ase = Atoms(self.species, self.pos)
        ase.arrays['force'] = self.forces
        return ase
