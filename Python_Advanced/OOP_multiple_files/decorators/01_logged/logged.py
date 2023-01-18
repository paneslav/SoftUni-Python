def logged(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        str_res = ''
        str_res += f"you called {func_ref.__name__}({', '.join([str(x) for x in args])})\n"
        str_res += f"it returned {result}"
        return str_res

    return wrapper
