from prettytable import PrettyTable

class Entidade:
	@classmethod
	def atributos(cls):
		return cls.attr

	@classmethod
	def classname(cls, up=False):
		cn = str(cls.__name__)
		return cn.upper() if up else cn

	@classmethod
	def arquivo(cls):
		name = str(cls.classname())
		return f"dados/{name.lower()}.json"

	def __init__(self, *args):
		atributos = self.atributos()
		if len(args) == len(atributos):
			self.from_list(args)
			return
		elif len(args) == 1:
			args = args[0]

		if type(args) is list:
			self.from_list(args)
			return
		if type(args) is type(self):
			args = vars(args)
		for k in atributos:
			setattr(self, k, args[k])
	
	def copy(self):
		return type(self)(vars(self))

	def from_list(self, *args):
		atributos = self.atributos()
		if len(args) == 1 and len(atributos) > 1:
			args = args[0]
		if len(args) != len(atributos):
			raise TypeError(args)
		for i, k in enumerate(atributos):
			setattr(self, k, args[i])

	def table(self):
		tabela = PrettyTable()
		tabela.field_names = [ "#", self.classname() ]
		for k in self.atributos():
			tabela.add_row([k, getattr(self, k)])
		return tabela

	def row(self, idx=None, attr=None, t=None):
		attr = attr or self.atributos()
		
		row = [ getattr(self, k) for k in attr ]
		row = [ idx, *row ] if idx else row
		
		if t == True:
			t = PrettyTable()
			t.field_names = [ '#', *attr ] if idx else attr

		if type(t) == PrettyTable:
			t.add_row(row)
			return t
		else: return row