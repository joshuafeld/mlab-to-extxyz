from atom import Atom
from cell import Cell

# The different type of ledger lines
STAR_LEDGER = '*' * 50
EQUAL_LEDGER = '=' * 50
MINUS_LEDGER = '-' * 50

def get_value(raw: list[str], name: str) -> str:
    """Returns the value associated with the given name as a string."""
    return raw[raw.index(name) + 2]

def get_list(raw: list[str], name: str, ledger: str) -> list[str]:
    """Returns the values associated with the given name as a string list."""
    start = raw.index(name) + 2
    return ' '.join(raw[start:raw.index(ledger, start)]).split()

def get_int(raw: list[str], name: str) -> int:
    """Returns the value associated with the given name as an int."""
    return int(get_value(raw, name))

def get_float(raw: list[str], name: str) -> float:
    """Returns the value associated with the given name as a float."""
    return float(get_value(raw, name))

def get_float_list(raw: list[str], name: str, ledger: str) -> list[float]:
    """Returns the values associated with the given name as a float list."""
    return list(map(float, ' '.join(list(map(lambda l: ' '.join(l.split()), get_list(raw, name, ledger)))).split()))

def get_vec3(raw: list[str], name: str) -> list[float]:
    """Returns the value associated with the given name as a three-dimensional float vector."""
    return list(map(float, get_value(raw, name).split()))

def get_vec3_list(raw: list[str], name: str, ledger: str) -> list[list[float]]:
    """Returns the values associated with the given name as a three-dimensional float vector list."""
    floats = get_float_list(raw, name, ledger)
    return [floats[i:i + 3] for i in range(0, len(floats), 3)]

# Read the input file into a list of lines.
with open('ML_AB') as file:
    ml_ab = [' '.join(line.split()) for line in file]

# Get the number of cells in the ML_AB file.
cell_count: int = get_int(ml_ab, 'The number of configurations')

# Create a list of cells.
cells: list[Cell]
for cell_index in range(1, cell_count + 1):
    if cell_index % 10 == 0:
        print(f'Parsing cell {cell_index}/{cell_count}')

    # Extract the relevant lines for the current cell from the input file.
    start: int = ml_ab.index(f'Configuration num. {cell_index}')
    raw: list[str] = ml_ab[start:ml_ab.index('XY YZ ZX', start) + 3]

    # Read the cell data for the current cell.
    lattice: list[list[float]] = get_vec3_list(raw, 'Primitive lattice vectors (ang.)', EQUAL_LEDGER)
    energy: float = get_float(raw, 'Total energy (eV)')
    stress: list[list[float]] = [get_vec3(raw, 'XX YY ZZ'), get_vec3(raw, 'XY YZ ZX')]

    # Read the atom data for the current cell.
    species_counts: list[str] = get_list(raw, 'Atom types and atom numbers', EQUAL_LEDGER)
    species: list[str] = species_counts[0::2]
    counts: list[int] = list(map(int, species_counts[1::2]))
    pos: list[list[float]] = get_vec3_list(raw, 'Atomic positions (ang.)', EQUAL_LEDGER)
    forces: list[list[float]] = get_vec3_list(raw, 'Forces (eV ang.^-1)', EQUAL_LEDGER)

    # Create a list of the atoms in the current cell.
    atoms = []
    for j, (s, c) in enumerate(zip(species, counts)):
        for k in range(c):
            l: int = sum(counts[:j]) + k
            atoms.append(Atom(s, pos[l], forces[l]))

    # Create and append the current cell to the list of cells.
    cells.append(Cell(lattice, energy, stress, atoms))

# TODO: Do something with the created cells list.
