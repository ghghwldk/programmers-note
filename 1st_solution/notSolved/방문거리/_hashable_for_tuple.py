'''
Are tuples hashable in Python?

Tuples can be hashable only tuple holds hashable reference.

If tuple hold unhashable objects such as lists or dict.
The Tuple can't hasable

if we use the hash method for the unhashable tuple,
then TypeError occurs.
'''