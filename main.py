
from distance import damerau_levenshtein, keyboard_distance

# Exemple fictive
exemple = [
    ("magazin", "magazn"),
    ("magazin", "magazinn"),
    ("magazin", "magzain"),
    ("magazin", "magaz1n"),
    ("magazin", "magszin"),
    ("magazin", "atelier")
]


print(f"{'Original':<15} {'Modificat':<15} {'DL':<12} {'QWERTY':<10}")
print("-")

for original, modificat in exemple:
    dl = damerau_levenshtein(original, modificat)
    qwerty = keyboard_distance(original, modificat)

    print(f"{original:<15} {modificat:<15} {dl:<12} {qwerty:<10}")
