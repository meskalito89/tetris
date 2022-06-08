import numpy as np
from shape import Shape


def create_random_shape(position: tuple[int, int]):
    variants = (
        [[-1, 1], [0, 1], [0, -1], [1, -1]],
        [[-2, 0], [-1, 0], [0, 0], [1, 0]],
    )
    random_index = np.random.randint(0, len(variants))
    return Shape(position, variants[random_index])


class Game:
    def __init__(self):
        self.field = np.zeros((20, 10)).astype('bool')

    def text(self, simbol_true, simbol_false):
        field_text = ''
        for row in self.field:
            field_text += ' '.join(
                map(lambda x: simbol_true if x else simbol_false, row)
            )
            field_text += '\n'

        return field_text

 
game = Game()
print(game.text(0, ' '))
print(create_random_shape((10, 10)))
    
