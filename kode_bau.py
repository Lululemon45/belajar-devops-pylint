def bad_function_name(a, b, c, d, e, f):
    """Menjalankan contoh fungsi dengan kondisi tertentu."""
    if a and not b and c is None:
        result = e[0] + f + d
        print(result)
        return result
    return None


bad_function_name(True, False, None, 1, [2], 3)