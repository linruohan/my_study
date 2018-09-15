def decorator_a(func):
    print("decorator_a")
    return func


def decorator_b(func):
    print("decorator_b")
    return func

@decorator_a
@decorator_b
def m():
    print("sd")

m()
