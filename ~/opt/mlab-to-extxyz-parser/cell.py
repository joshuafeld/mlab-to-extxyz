from typing import List

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
	stress : list[list[float]]
		The stress tensor (in kbar).
	atoms : list[Atom]
		The contained atoms.
	"""

	def __init__(self, lattice : List[List[float]], energy: float, stress: List[List[float]], atoms: List[Atom]) -> None:
		"""
		Parameters
		----------
		lattice : list[list[float]]
			The three lattice vectors (in Angstrom)
		energy : float
			The total energy (in eV)
		stress : list[list[float]]
			The stress tensor (in kbar)
		atoms : list[Atom]
			The atoms in the cell
		"""

		self.lattice = lattice
		self.energy = energy
		self.stress = stress
		self.atoms = atoms
