"""pdb_demo.py - Example of pdb from chapter 4"""

class PdbDemo(object):

    def __init__(self, name, num_loops):
        self._name = name
        self._count = num_loops

    def count(self):
        for i in range(self._count):
            print(i)
        return '{} executed {} of {} loops'\
               .format(self._name, i+1, self._count)

if __name__ == '__main__':
    obj_name = 'pdb demo'
    print('Starting ' + obj_name + '...')
    pd = PdbDemo(obj_name, 5)
    result = pd.count()
    print(result)
