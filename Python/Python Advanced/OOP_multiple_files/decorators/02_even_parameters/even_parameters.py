def even_parameters(func_ref):
    def wrapper(*args):
        for item in args:
            if not isinstance(item, int) or item % 2 != 0:
                return f'Please use only even numbers!'

        result = func_ref(*args)

        return result

    return wrapper