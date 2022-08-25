"""
NamedTuple can have properties and NamedTuple can have attributes with default
values, but NamedTuple can't properly use property as default value.
Therefore, this hack: 
build NamedTuple with c as attribute, then overwrite c with property. 
"""

from typing import NamedTuple

class X(NamedTuple):
	def _get_c(self): 
		if self._asdict()['c'] == None:
			return self.a + self.b
		else:
			return self._asdict()['c']

	a: int 
	b: float 

	c: float = None
X.c = property(X._get_c)  
# default value derived from other attributes, but can be overwritten

x = X(1,2, c=8)
print(x.c)

x = X(1,2)
print(x.c)