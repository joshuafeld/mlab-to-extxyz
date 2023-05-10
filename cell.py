from typing import List

from ase import Atoms
from atom import Atom

class Cell:
    """
    Represents a cell.

    ...

    Attributes
    ----------
    lattice : list[list[float]]
        The three lattice vectors (in Angstrom).
    energy : float
        The total energy (in eV).
    virial : list[list[float]]
        The Cauchy stress tensor (in kbar).
    atoms : list[Atom]
        The contained atoms.
    """

    def __init__(self, lattice : List[List[float]], energy: float, stress: List[List[float]],
            atoms: List[Atom]) -> None:
        """
        Parameters
        ----------
        lattice : list[list[float]]
            The three lattice vectors (in Angstrom).
        energy : float
            The total energy (in eV).
        stress : list[list[float]]
            The stress tensor (in kbar).
        atoms : list[Atom]
            The atoms in the cell.
        """

        self.lattice = lattice
        self.energy = energy
        # Convert the stess values to the Cauchy stress tensor.
        self.virial = [[stress[0][0], stress[1][0], stress[1][2]],
                [stress[1][0], stress[0][1], stress[1][1]],
                [stress[1][2], stress[1][1], stress[0][2]]]
        self.atoms = atoms

    def to_ase(self) -> Atoms:
        """Converts the cell to an ASE Atoms object.

        Returns
        -------
        Atoms
            An ASE Atoms object containing the atom data.
        """

        ase: Atoms = Atoms(pbc=[1, 1, 1])
        for atom in self.atoms:
            ase += atom.to_ase()
        ase.info['energy'] = self.energy
        ase.info['virial'] = ' '.join([str(item) for sublist in self.virial for item in sublist])
        ase.info['Lattice'] = ' '.join([str(item) for sublist in self.lattice for item in sublist])
        return ase
