from life import Life
from random import choice

def check_nebgs(field):
    for cell in field.cells:
        if cell.value:
            for neb in cell.nebgs.values():
                if neb.value:
                    if cell.value:
                        sexs = [cell.value.sex,neb.value.sex]
                        if 'male' in sexs and 'female' in sexs:
                            new_cell = cell.get_empty_neb()
                            if not new_cell: neb.get_empty_neb()

                            if new_cell:
                                Life.born_new(new_cell, cell.value, neb.value)
                                

                        if sexs[0] == "male" and sexs[1] == "male":
                            if cell.value.age > 10 and neb.value.age > 10:
                                cell.value.die()
                                neb.value.die()
                        
                            