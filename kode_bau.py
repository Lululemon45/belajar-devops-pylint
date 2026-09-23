"""Contoh fungsi dengan kualitas kode yang diperbaiki."""


def calculate_result(a, b, c):
    """Menghitung hasil berdasarkan beberapa kondisi."""
    if a and not b and c is None:
        result = 2 + 3 + 1
        print(result)
        return result
    return None


calculate_result(True, False, None)

