from typing import NamedTuple, Callable, Any


class AnonymousTuple:
	"""
	NamedTuple that builds its attributes dynamically from __init__().
	To be used as immutable dict. 
	"""
	def __init__(self, **kwargs):
		value_list = [v for v in kwargs.values()]
		attr_list = [(k, type(v)) for k, v in kwargs.items()]
		NT = NamedTuple('AnonymousTuple',attr_list)(*value_list)	
		super().__setattr__('_tuple', NT)
	
	def __getattr__(self, __name: str):
		return getattr(self._tuple,__name)
	
	def __setattr__(self, __name: str, __value) -> None:
		raise AttributeError("can't set any attributes")
	
	def __repr__(self) -> str:
		return self._tuple.__repr__()
	
	# declaration for autocomplete
	_replace : Callable[[Any],"AnonymousTuple"]
	_asdict : Callable[["AnonymousTuple"],dict]


at = AnonymousTuple(s=3,t=4)

print("---")
print(at.t)
print("...")
print(hasattr(at, 't'))
print(hasattr(at, 'g'))
# at.s = 7  <-- illegal
# at.g = 4  <-- illegal
print(at)
print(at.s)
print(at._asdict())
# print(at.g)  <-- illegal
at2 = AnonymousTuple(**at._asdict())
print(at2)
at3 = at2._replace(s=8)
print(at3)

at11 = AnonymousTuple(u=9,v=8)
at11.u
at11