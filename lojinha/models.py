from django.db import models

# Create your models here.
class Bolo(models.Model):
    sabores_opcoes = [
        ('ch','chocolate'),
        ('mr', 'Morango'),
        ('pr', 'prestigio'),
        ('bn', 'Baumilia'),
        ('cr','Churros'),
        ('nh','Ninho'),
    ]
    recheios_opcoes = [
        ('br', 'Brigadeiro'),
        ('dl', 'Doce de leite'),
        ('fv', 'Frutas Vermelhas'),
        ('nt', 'Nutella'),
        ('bj','Beijinho'),
        ('nh', 'Ninho'),

    ]

    coberturas_opcoes = [
        ('gr', 'Granulado'),
        ('ct', 'Chantilly'),
        ('mr', 'Morango'),
        ('re', 'Requeijão Cremoso'),
    ]

    sabor = models.CharField(max_length=2, choices=sabores_opcoes)
    recheio = models.CharField(max_length=2, choices=recheios_opcoes)
    cobertura = models.CharField(max_length=2,choices=coberturas_opcoes,default='sc')
    peso = models.DecimalField(decimal_places=2, max_digits=3, default=1.00)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    pagamentos_opcoes = [
        ('av', 'Pagamento a vista'),
        ('p2', 'Parcelado em 2 vezes'),
        ('p3', 'Parcelado em 3 vezes'),
    ]

    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=pagamentos_opcoes, default='av')

    