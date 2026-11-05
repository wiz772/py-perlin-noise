"""
Benchmark : optimisation de la fonction _fade()
Objectif : comparer l'expression polynomiale originale
avec sa forme factorisée (méthode de Horner).
Mesure : temps d'exécution sur 1 million d'appels.
"""

import timeit
import statistics
import math

def fade_original(t: float) -> float:
    return 6*t**5 - 15*t**4 + 10*t**3

def fade_optimized(t: float) -> float:
    return t**3 * (t * (6*t - 15) + 10)


NUMBER = 1_000_000
REPEAT = 5
T = 0.5

# Vérification des résultats
assert math.isclose(fade_original(T), fade_optimized(T), rel_tol=1e-12)

original_times = timeit.repeat(
    lambda: fade_original(T),
    number=NUMBER,
    repeat=REPEAT
)

optimized_times = timeit.repeat(
    lambda: fade_optimized(T),
    number=NUMBER,
    repeat=REPEAT
)

original_median = statistics.median(original_times)
optimized_median = statistics.median(optimized_times)

print(f"Original : {original_median:.4f}s")
print(f"Optimisé : {optimized_median:.4f}s")
print(f"Gain : {(1 - optimized_median / original_median) * 100:.2f}%")
print(f"Accélération : {original_median / optimized_median:.2f}x")
