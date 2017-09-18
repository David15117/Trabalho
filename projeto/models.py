from django.db import models

# Create your models here.
class Pessoa(models.Model):
	"""docstring for Pessoa"""
	nome = models.CharField(max_length=50)
	email = models.EmailField(max_length=200)
	def __str__(self):
		return self.nome
class Evento(models.Model):
	"""docstring for ClassName"""
	nome = models.CharField(max_length=50)
	eventoPrincipal = models.CharField(max_length=120)
	single = models.CharField(max_length=5)
	dataEHoraDeInicio = models.DateTimeField()
	palavrasChave = models.CharField(max_length=70)
	logotipo = models.CharField(max_length=50)
	realizador=models.ForeignKey(Pessoa, related_name='pessoa', null=True, blank=False)
	cidade = models.CharField(max_length=50)
	uf = models.CharField(max_length=2)
	endereco = models.CharField(max_length=50)
	cep = models.CharField(max_length=8)
	def __str__(self):
		return self.nome
class EventoCientifico(Evento):
	"""docstring for EventoCientifico"""
	sn =  models.CharField(max_length=20)
	def __str__(self):
		return self.sn
class PessoaJurifica(Pessoa):
	"""docstring for PessoaJurifica"""
	cnpj = models.CharField(max_length=13)
	razaoSocial=models.CharField(max_length=50)
	def __str__(self):
		return self.cnpj
class PessoaFisica(Pessoa):
	"""docstring for PessoaFisica"""
	cpf = models.CharField(max_length=20)
	def __str__(self):
		return self.cpf
class Autor(Pessoa):
	currilo = models.TextField(max_length=50)
	def __str__(self):
		return self.currilo
class ArtigoCientifico(models.Model):
	"""docstring for ArtigoCientifico"""
	titulo = models.CharField(max_length=50)
	evento = models.ForeignKey(EventoCientifico, related_name='eventocientifico', null=True, blank=False)
	Autores = models.ManyToManyField(Autor)
	def __str__(self):
		self.titulo
		




		