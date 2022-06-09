import numpy as np
from shape import Shape
import random


def get_random_shape():
    variants = {
        'z_right': [
            [0, -1],  #   *    
            [0, 0],  #    **  
            [1, 0],  #     *  
            [1, 1]   #        
        ],
        'z_left': [
            [0, -1],  #   *    
            [0, 0],  #   **   
            [-1, 0],  #  *     
            [-1, 1]   #        
        ],
        'square': [
            [0, 0],  #        
            [1, 0],  #  **    
            [1, 1],  #  **    
            [1, 0]   #        
        ],
        'l_rigth': [
            [0, 0],  #  *     
            [0, 1],  #  *     
            [0, 2],  #  **    
            [1, 2]   #        
        ],
        'l_left': [
            [0, 0],  #    *   
            [0, 1],  #    *   
            [0, 2],  #   **   
            [1, 2]   #        
        ],
        'T': [
            [-1, 0],  #  ***   
            [0, 0],  #    *   
            [1, 0],  #        
            [0, 1]   #        
        ],
        'I': [
            [0, -1],  #   *    
            [0, 0],  #    *   
            [0, 1],  #    *   
            [0, 2]   #    *   
        ],
    }

    random_shape = random.choice(list(variants.keys()))

    return variants.get(random_shape)


class game:
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

