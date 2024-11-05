from django.db import models

# Requisito RF08 - Manter UF (MG, SP, RJ, BA, RS)
class UF(models.Model):
    sigla = models.CharField(max_length=2, choices=[
        ('MG', 'Minas Gerais'),
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
        ('BA', 'Bahia'),
        ('RS', 'Rio Grande do Sul'),
    ])

    class Meta:
        verbose_name_plural = 'Unidades Federais'
        
    def __str__(self):
        return self.sigla

# Requisito RF02 - Manter Gêneros
class Generos(models.Model):  
    nome = models.CharField(max_length=50)  

    class Meta:
        verbose_name_plural = 'Gêneros dos livros' 

    def __str__(self):
        return self.nome

# Requisito RF07 - Manter Cidades
class Cidades(models.Model):  
    nome = models.CharField(max_length=50)  
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)  # Nome da chave estrangeira para UF alterado para "uf" (em minúsculo)

    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome

# Requisito RF03 - Manter Editoras
class Editora(models.Model):
    nome = models.CharField(max_length=50)  
    site = models.URLField(max_length=200)  # Melhor usar URLField para o site
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)  # Nome da chave estrangeira alterado para "cidade"

    class Meta:
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return self.nome

# Requisito RF04 - Manter Autores
class Autores(models.Model):
    nome = models.CharField(max_length=50)   
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)  # Nome da chave estrangeira alterado para "cidade"

    class Meta:
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome

# Requisito RF01 - Manter Usuários
class Usuario(models.Model):
    nome = models.CharField(max_length=50)   
    cpf = models.CharField(max_length=11)  # CPF é uma string com 11 caracteres
    data_nasc = models.DateField()  # Definido como DateField
    email = models.EmailField()
    telefone = models.CharField(max_length=15)  # Telefone como string para permitir DDD
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)  # Nome da chave estrangeira alterado para "cidade"

    class Meta:
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome

# Requisito RF05 - Manter Livros
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    data_publicacao = models.DateField()

    class Meta:
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.nome

# Requisito RF06 - Manter Empréstimo de Livros
class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_devolucao = models.DateField()

    class Meta:
        verbose_name_plural = 'Empréstimos'

    def __str__(self):
        return f'Empréstimo de {self.livro.nome} para {self.usuario.nome}'
