from django.contrib import admin
from .models import UF, Generos, Cidades, Editora, Autores, Usuario, Livro, Emprestimo

# Registra os modelos no Django Admin
admin.site.register(UF)
admin.site.register(Generos)
admin.site.register(Cidades)
admin.site.register(Editora)
admin.site.register(Autores)
admin.site.register(Usuario)
admin.site.register(Livro)
admin.site.register(Emprestimo)


