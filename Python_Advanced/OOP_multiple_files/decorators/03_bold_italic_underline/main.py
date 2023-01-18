def make_bold(func_ref):
    def wrapper(*args):
        text = func_ref(*args)
        return f'<b>{text}</b>'

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        text = func_ref(*args)
        return f'<i>{text}</i>'

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        text = func_ref(*args)
        return f'<u>{text}</u>'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
