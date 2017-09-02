class Singleton(type):
	def __call__(cls, *args, **kwargs):
		if not hasattr(Singleton, '_instance'):
			setattr(Singleton, '_instance' , super(Singleton, cls).__call__(*args, **kwargs))
		return getattr(Singleton , '_instance')

class Logger(object):
	# A metaclass is the class of the class, i.e a class is an instance of its metaclass
	__metaclass__ = Singleton

obj = Logger()
obj1 = Logger()
print obj
print obj1

# BAD WAY -- issues when doing inheritance, some child class might override __new__ method
class A(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(A, '_private'):
			setattr(A, '_private', super(A, cls).__new__(A))
		return getattr(A, '_private')
