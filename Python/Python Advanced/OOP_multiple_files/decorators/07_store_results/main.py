class store_results:

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        func_name = self.func.__name__
        func_result = self.func(*args)
        text = f"Function '{func_name}' was called. Result: {func_result}"

        with open(self._logfile, 'a') as log:
            log.write(text + '\n')



@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)