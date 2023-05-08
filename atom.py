from typing import List

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
	force : list[float]
		The force (in eV/Angstrom).
	"""
	
	def __init__(self, species: str, pos: List[float], force: List[float]):
		"""
		Parameters
		----------
		species : str
			The species (chemical symbol).
		pos : list[float]
			The position in Cartesian coordinates (given in Angstrom).
		force : list[float]
			The force (in eV/Angstrom).
		"""

		self.species = species
		self.pos = pos
		self.force = force
