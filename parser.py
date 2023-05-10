from ase import Atoms
from ase.io import write
from tqdm import tqdm
from typing import List

from atom import Atom
from cell import Cell

# The different type of ledger lines
STAR_LEDGER = '*' * 50
EQUAL_LEDGER = '=' * 50
MINUS_LEDGER = '-' * 50

def get_value(raw: List[str], name: str) -> str:
    """Returns the value associated with the given name as a string.
    
    Parameters
    ----------
    raw: list[str]
        A list of lines in the raw file.
    name: str
        The name of the desired value.

    Returns
    -------
    str
        The value as a string.
    """

    return raw[raw.index(name) + 2]

def get_list(raw: List[str], name: str, ledger: str) -> List[str]:
    """Returns the values associated with the given name as a string list.
    
    Parameters
    ----------
    raw: list[str]
        A list of lines in the raw file.
    name: str
        The name of the desired values.
    ledger: str
        The ledger that ends the values section.

    Returns
    -------
    list[str]
        The values as a string list.
    """

    start: int = raw.index(name) + 2
    return ' '.join(raw[start:raw.index(ledger, start)]).split()

def get_int(raw: List[str], name: str) -> int:
    """Returns the value associated with the given name as an int.
    
    Parameters
    ----------
    raw: list[str]
        A list of lines in the raw file.
    name: str
        The name of the desired value.

    Returns
    -------
    int
        The value as an int.
    """

    return int(get_value(raw, name))

def get_float(raw: List[str], name: str) -> float:
    """Returns the value associated with the given name as a float.
    
    Parameters
    ----------
    raw: list[str]
        A list of lines in the raw file.
    name: str
        The name of the desired value.

    Returns
    -------
    float
        The value as a float.
    """

    return float(get_value(raw, name))

def get_float_list(raw: List[str], name: str, ledger: str) -> List[float]:
    """Returns the values associated with the given name as a float list.
    
    Parameters
    ----------
    raw: list[str]
        A list of lines in the raw file.
    name: str
        The name of the desired values.
    ledger: str
        The ledger that ends the values section.

    Returns
    -------
    list[float]
        The values as a float list.
    """

    return list(map(float, ' '.join(list(map(lambda l: ' '.join(l.split()), get_list(raw, name,
            ledger)))).split()))

def get_vec3(raw: List[str], name: str) -> List[float]:
    """Returns the value associated with the given name as a three-dimensional float vector.
    
    Parameters
    ----------
    raw: list[str]
        A list of lines in the raw file.
    name: str
        The name of the desired value.

    Returns
    -------
    list[float]
        The value as a three-dimensional float vector.
    """

    return list(map(float, get_value(raw, name).split()))

def get_vec3_list(raw: List[str], name: str, ledger: str) -> List[List[float]]:
    """Returns the values associated with the given name as a three-dimensional float vector list.
    
    Parameters
    ----------
    raw: list[str]
        A list of lines in the raw file.
    name: str
        The name of the desired values.
    ledger: str
        The ledger that ends the values section.

    Returns
    -------
    list[list[float]]
        The values as a three-dimensional float vector list.
    """

    floats: List[float] = get_float_list(raw, name, ledger)
    return [floats[i:i + 3] for i in range(0, len(floats), 3)]

def parse_mlab(path: str) -> List[Cell]:
    """Converts the given ML AB file into a list of cells.
    
    Parameters
    ----------
    path: str
        The path to the input file.

    Returns
    -------
    list[Cell]
        A list of cells containing the data of the input file.
    """

    # Read the input file into a list of lines.
    with open(path) as file:
        ml_ab: List[str] = [' '.join(line.split()) for line in file]
    
    # Get the number of cells in the ML_AB file.
    cell_count: int = get_int(ml_ab, 'The number of configurations')

    # Create a list of cells.
    cells: List[Cell] = []
    for cell_index in tqdm(range(1, cell_count + 1), 'Parsing input file'):
        # Extract the relevant lines for the current cell from the input file.
        start: int = ml_ab.index(f'Configuration num. {cell_index}')
        raw: List[str] = ml_ab[start:ml_ab.index('XY YZ ZX', start) + 3]

        # Read the cell data for the current cell.
        lattice: List[List[float]] = get_vec3_list(raw, 'Primitive lattice vectors (ang.)',
                EQUAL_LEDGER)
        energy: float = get_float(raw, 'Total energy (eV)')
        stress: List[List[float]] = [get_vec3(raw, 'XX YY ZZ'), get_vec3(raw, 'XY YZ ZX')]

        # Read the atom data for the current cell.
        species_counts: List[str] = get_list(raw, 'Atom types and atom numbers', EQUAL_LEDGER)
        species: List[str] = species_counts[0::2]
        counts: List[int] = list(map(int, species_counts[1::2]))
        pos: List[List[float]] = get_vec3_list(raw, 'Atomic positions (ang.)', EQUAL_LEDGER)
        forces: List[List[float]] = get_vec3_list(raw, 'Forces (eV ang.^-1)', EQUAL_LEDGER)

        # Create a list of the atoms in the current cell.
        atoms: List[Atom] = []
        for j, (s, c) in enumerate(zip(species, counts)):
            for k in range(c):
                l: int = sum(counts[:j]) + k
                atoms.append(Atom(s, pos[l], forces[l]))

        # Create and append the current cell to the list of cells.
        cells.append(Cell(lattice, energy, stress, atoms))
    return cells
