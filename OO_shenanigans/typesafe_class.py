# -*- coding: utf-8 -*-

def getter_setter_gen(name, type_, do_typecast):
	def getter(self):
		return getattr(self, "__" + name)
	def setter(self, value):
		if do_typecast:
			value = type_(value)
		else: 
			if not isinstance(value, type_):
				raise TypeError(
					f"{name} attribute must be set to an instance of {type_}")
		setattr(self, "__" + name, value)
	return property(getter, setter)

def auto_attr_check(cls=None, do_typecast=True):
	"""allows enforced types for attributes. 
	Default case: try to typecast into desired type. Use `do_typecast=False` 
	to instead raise an error on type mismatch at assignment 
	(applies to entire class as a whole)"""
	from typing import get_type_hints

	def wrapper(cls):
		for attr, type_ in get_type_hints(cls).items():
			setattr(cls, attr, getter_setter_gen(attr, type_, do_typecast))

		return cls

	if cls == None: return wrapper
	else:           return wrapper(cls)

# =============================================================================
# useage examples

@auto_attr_check
class A:
	a : int 
	b : float

obj = A()
obj.a = 3
obj.b = "4"
print(f"sum of A: {obj.a=} + {obj.b=} = {obj.a + obj.b}")

# -----------------------------------------------------------------------------

@auto_attr_check(do_typecast=True)
class B:
	a : int 
	b : float

	def __init__(self):
		self.a = 4

obj = B()
# obj.a = 4
obj.b = "5.7"
print(f"sum of B: {obj.a=} + {obj.b=} = {obj.a + obj.b}")

# -----------------------------------------------------------------------------

@auto_attr_check(do_typecast=False)
class C:
	a : int 
	b : float

obj = C()
try:
	obj.a = 2
	obj.b = 3
	print(f"sum of C: {obj.a=} + {obj.b=} = {obj.a + obj.b}")
except TypeError as e:
	print("Error raised, as expected:")
	print(e)

# -----------------------------------------------------------------------------
from dataclasses import dataclass

@auto_attr_check
@dataclass
class D:
	a : int 
	b : float

obj = D(6, "7.1")
print(f"sum of D: {obj.a=} + {obj.b=} = {obj.a + obj.b}")