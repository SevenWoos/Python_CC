import printing_models as pm

# Import the printing_models module to use the print_models() and show_completed_models() functions.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm.print_models(unprinted_designs, completed_models)
pm.show_completed_models(completed_models)