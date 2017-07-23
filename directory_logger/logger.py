''' The main logging system for the package '''
import os
from time import gmtime, strftime

class Logger:
    '''
    This class is responsible for all the logging of the directory
    contents.
    '''

    def __init__(self, name):
        '''
        Constructor for the class.  See below for mode options.

        <code>
            'r': open for reading
            'w': open for writing, truncating the file first
            'X': open for exclusive creation, failing if the file already exists
            'a': open for writing, appending to the end of the file if it exists
            'b': binary mode
            't': text mode (default)
            '+': open a disk file for updating (reading and writing)
        </code>

        Parameters
        ----------
        name : str
            The name of the file you wish to log too.
        '''
        if name is not None:
            self._filename = name
        else:
            # We need to flag something here.
            pass


    def write(self, string):
        '''
        Used to write to the file pointer

        Return
        ------
        None
        '''
        if not isinstance(string, str):
            string = str(string)

        with open(self._filename, 'a') as file:
            file.write(self.timestamp() + ' - ' + string + os.linesep)

    def timestamp(self):
        '''
        Used to get the current timestamp

        Return
        ------
        str
        '''
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())
