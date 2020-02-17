
# By value & By reference call

The interpreter looks at the type of the value referred to by the object reference (the memory address) and, 
if the variable refers to a **mutable value**, call-by-reference semantics apply. If the type of the data 
referred to is **immutable**, call-by- value semantics kick in. Consider now what this means for our data.

Lists, dictionaries, and sets (being mutable) are always passed into a function by reference— any changes made to the variable’s data structure within the function’s suite are reflected in the calling code. The data is mutable, after all.


Strings, integers, and tuples (being immutable) are always passed into a function by value— any changes to the variable within the function are private to the function and are not reflected in the calling code. As the data is immutable, it cannot change.




# Produce a module

Start by writing a ```setup.py``` file as provided.

Produce the installation:

```python3 setup.py sdist```


Install with pip:

```pip3 install functions.tar.gz```