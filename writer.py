from ase.io import write
from tqdm import tqdm

from cell import Cell

def write_extxyz(cells: list[Cell], path: str):
    write(path, images=[cell.to_ase() for cell in tqdm(cells, 'Converting to ASE')], format='extxyz')
