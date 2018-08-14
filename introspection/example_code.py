import sys

# comment code example_func
def example_func(arg_1, kw_1='kw arg 1', *args, **kw):
    "Example function doc string"
    print(f"example_func call with arg_1={arg_1} kw_1={kw_1} *args={args} kw={kw}")

# comment code for example_class
class example_class:
    "Example class doc string"

    #comment code for example class __init__
    def __init__(self, arg_1, arg_2=1, *args, **kw):
        "Example class __init__ doc string"
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.args = args
        self.kw = kw

    def __str__(self):
        "Example class __str__ doc string"
        print(f"arg_1={self.arg_1} arg_2={self.arg_2} args={self.args} kw={self.kw}")


class example_subclass(example_class):
    pass


def stack_one(arg_1):
    local_data = [1, 2, 3]
    return stack_two(2)

def stack_two(arg_1):
    local_data = dict(a="one", b="two", c="three")
    return stack_three(3)

def stack_three(arg_1):
    local_data = 3.0
    return sys._getframe(0)
