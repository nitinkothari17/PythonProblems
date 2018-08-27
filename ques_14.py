from collections import namedtuple
from operator import attrgetter

tuples = namedtuple('tuples' , 'name age height')
seq = [tuples("Tom",19,80),tuples("John",20,90),tuples("Jony",17,91),tuples("Jony",17,93),tuples("Json",21,85)]
print sorted(seq)
 
