from ase.io import write

from cell import Cell

def write_extxyz(cells: list[Cell], path: str):
    write(path, images=[cell.to_ase() for cell in cells], format='extxyz')