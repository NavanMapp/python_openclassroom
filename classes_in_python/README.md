Instructions

In our example, we'll be creating the blueprint for a person. Compared to most languages, the syntax for defining a simple class is very minimal in Python.

In this activity, we will create our first class, called Person. The steps are as follows:

In your terminal, declare the class using the Python keyword class, followed by the class name Person. In the block, we have the Python keyword pass, which is used as a placeholder for where the rest of our class definition will go:
>>> class Person:
...     pass
...
>>>

Run the type function on this class we've created; it will yield the type type:
>>> type(Person)
<class 'type'>
>>>

This is a bit confusing, but what this means is just as there are data structures of type list or dict, we've also, in a sense, extended the Python language to include a new kind of data structure called Person. In Python, a class and a type are synonymous. This Person structure can encapsulate different attributes and methods that will be specific to that object. We'll look at this in more depth further down the line.