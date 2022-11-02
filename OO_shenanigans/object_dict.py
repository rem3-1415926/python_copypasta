# -*- coding: utf-8 -*-

class objdict(dict):
	"""
	dict that can have its content accessed as attributes.
	works fully in both ways (dict and object)
	"""
	def __getattr__(self, name):
		if name in self:
			return self[name]
		else:
			raise AttributeError("No such attribute: " + name)

	def __setattr__(self, name, value):
		self[name] = value

	def __delattr__(self, name):
		if name in self:
			del self[name]
		else:
			raise AttributeError("No such attribute: " + name)
	
	def _asdict(self):
		return dict(self)

if __name__ == "__main__":
	foo = objdict({'a': 1, 'b': 2})
	print(foo['a'])
	print(foo.b)
	foo.c = 3
	foo['d'] = 4
	del foo.a 
	del foo['b']
	print(foo)


class objectview(object):
	"""
	object type of view to a dict, so its content can be accessed as attributes.
	does not support dict type access; doesn't come with __repr__() of dict
	"""
	def __init__(self, d):
		self.__dict__ = d

if __name__ == "__main__":
	bar = objectview({"x":1,"y":2})
	print(bar.x)
	# print(bar['y'])  <-- does not work
	# bar["z"] = 3  <-- does not work
	bar.u = 4
	del bar.x
	# del bar['y']  <-- does not work
	print(bar)  # <-- no inherent __repr__()