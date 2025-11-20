import numpy as np

def generate_random_sales(min_val, max_val, size):
    """Retourne un tableau aléatoire d'entiers entre min_val et max_val."""
    return np.random.randint(min_val, max_val + 1, size)
