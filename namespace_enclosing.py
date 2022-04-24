global_variable = 'global'


def outer_function():
    outer_value = "outer"

    def inner_function():
        inner_value = "inner"

        def inner_nested_function():
            nested_value = 'nested'

        inner_nested_function()
        # Add locals() below
        print(locals())

    inner_function()


outer_function()

""" 
Enclosing namespaces are created specifically when we work with nested functions and just like local namespace, will 
only exist until the function is done executing. 
"""