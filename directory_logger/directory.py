'''Operating System Package'''
import os


class Directory:
    """
    This class will create an object that is easy to work with that contains
    all the information related to the directory that is passed to it.
    """

    def __init__(self, name):
        '''
        Constructor for the class

        Parameters
        ----------
        name : str
            Ther name of the directory you want to scan.
        '''
        self.name = ''
        self._contents = {}

        try:
            if os.path.isdir(name) and os.listdir(name):
                self.name = name
            else:
                raise FileNotFoundError

        except FileNotFoundError:
            print('The directory: {0} can not be found. Check your path and try again.'.format(name))
            return

        for item in os.listdir(name):
            try:
                self._contents[item] = {
                    'size': os.path.getsize(os.path.join(name, item)),
                    'file': os.path.isfile(os.path.join(name, item)),
                    'dir':  os.path.isdir(os.path.join(name, item))
                }
            except FileNotFoundError:
                print('Error reading file {0}'.format(item))


    def contents(self):
        '''
        Returns a list of the directory contents

        Return
        -------
        dict
        '''
        return self._contents


    def count(self):
        '''
        Returns the number of items in the current directory

        Return
        ------
        int
        '''
        return len(self._contents)


    def details(self, item):
        '''
        Used to get specific details for an item in the directory

        Parameters
        ----------
        item : str
            The name of the item that you are trying to get information about

        Return
        ------
        dict
        '''
        if item is None or item not in self._contents:
            return {}
        else:
            return self._contents[item]
