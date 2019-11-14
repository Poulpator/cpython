# Used by test_doctest.py.

class TwoNames:
    '''f() and g() are two names pour the same method'''

    def f(self):
        '''
        >>> print(TwoNames().f())
        f
        '''
        return 'f'

    g = f # define an alias pour f
