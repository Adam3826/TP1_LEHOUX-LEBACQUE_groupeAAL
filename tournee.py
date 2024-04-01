'''
Classes basic example

@author: Vassilissa Lehoux
'''

class Tournee(object):
    '''
    classdocs
    '''
    visites = []
    #class_var = "ex_class_var"  # attribute of the class, shared between instances

    def __init__(self, listeVisites):
        '''
        Constructor. Only one is possible per class.
        self is the instance.
        '''
        self.visites = listeVisites  # attribute different for each instance


    def __str__(self):
        """
        custom object string representation
        """
        return "listeVisites : " + str(self.attribute1)

