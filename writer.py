from ase.io import write
from tqdm import tqdm
from typing import List

from cell import Cell

def write_extxyz(cells: List[Cell], path: str):
    """Writes cell data to extended XYZ file format.

    Parameters
    ----------
    cell: list[Cell]
        The cell data.
    path: str
        The path to the output file.
    """

    # Convert cells to ASE Atoms and write the data to extended XYZ file format.
    write(path, images=[cell.to_ase() for cell in tqdm(cells, 'Converting to ASE')],
            format='extxyz')
