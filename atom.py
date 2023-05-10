from ase import Atoms
from typing import List

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
    
    def __init__(self, species: str, pos: List[float], forces: List[float]) -> None:
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
        """Converts the atom to an ASE Atoms object.

        Returns
        -------
        Atoms
            An ASE Atoms object containing the atom data.
        """

        ase = Atoms(self.species, self.pos)
        ase.arrays['force'] = self.forces
        return ase
