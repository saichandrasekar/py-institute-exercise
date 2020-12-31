print("Inside writing functions")


def test_function():
    print("Inside test_function")


def test_function_with_arg(arg):
    print("Inside test_function_with_arg", arg)


test_function()

test_function_with_arg("arg-val")


# test_function_with_arg()

# ------------------
def quadratic_outputs(x_param):
    """
    Utility function to return the quadratic value of the input argument, x for a standard function y = f(x) = 3xx +
    2x + 4

    :param x_param:
    :return:
    """
    return (3 * (x_param ** 2)) + (2 * x_param) + 4


print("x", "y")
# for xParam in range(25):
#   print(xParam, quadratic_outputs(xParam))
result = [[x_param, quadratic_outputs(x_param)] for x_param in range(25)]
for index in range(len(result)):
    print(result[index][0], result[index][1])


# --------------------
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")


intro()


def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")


intro(b="Sean Connery")


def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")


intro("Susan")


def add_numbers(a, b=2, c=4):
    print(a + b + c)


add_numbers(a=1, c=3)

#-------------------------


def test_function_error():
    print(abc)

#test_function_error()
print("abc")

def is_int(data):
    global var
    var = 5
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))
