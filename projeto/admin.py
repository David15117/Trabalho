from django.contrib import admin
from projeto.models import *
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Evento)
admin.site.register(PessoaJurifica)
admin.site.register(PessoaFisica)
admin.site.register(Autor)
admin.site.register(ArtigoCientifico)
admin.site.register(EventoCientifico)

