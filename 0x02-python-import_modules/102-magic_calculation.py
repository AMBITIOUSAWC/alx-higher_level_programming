def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        return add(a, b + 98)
    else:
        return sub(a, b)
