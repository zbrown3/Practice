print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here:
print(globals())


# Write Checkpoint 2 here:
global_variable = 'global'



# Write Checkpoint 3 here:
def print_global():
  global_variable = 'nested global'
  nested_variable = 'nested value'



print(' \n -- Globals Namespace non-empty script -- \n')
# Write Checkpoint 4 here:
print(globals())

"""
Global namespace exists one level belore the built-in namespace.  It includes all non-nested names in the module (file) we are choosing to run the Python
interpreter on.  The global namespace is created when we run our main program and has a lifetime until the interpreter terminates.

Anytime we use the import statement to bring in a new module into our program, instead of adding every name from that module to our current global namespace, Python
will create a new namespace for it.  This means there might be potentially multiple global namespaces in a single program.
"""