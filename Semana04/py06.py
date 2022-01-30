# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = 'Test'

if condition:
    print('1 - Evaluated to True')
else:
    print('1 - Evaluated to False')

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')