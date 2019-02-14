from django.db import models
from datetime import datetime

# Create your models here.

class departamento(models.Model):
    nome = models.CharField(u'Nome do Departamento', max_length=30, blank=True)
    centrocusto = models.CharField(u'Centro de Custo', max_length=10, blank=True)

    def __str__(self):
        return self.nome

class responsavel(models.Model):

    PRIORIDADE_CHOICES = (
        ('U','Usuario'),       #Somente responsavel pelo Veiculo
        ('M','Profissional'),   #Qualquer Usuario do cadastro
        ('P','Profissional Especializado'),           #Apenas profissionais habilitados
            )
    PRIORIDADE_CHOICES_CNH = (
        ('A','A - Moto'),      
        ('B','B - Carro'),   
        ('C','C - Veiculo de carga acima 3,5 Ton'), 
        ('D','D - Veiculo de Passageiros acima de 8 Lugares'), 
        ('E','E - Veiculo com unidade acoplada acima de 6 Ton'), 
            )

    nome         = models.CharField(u'Nome do Responsável', max_length=30)
    departamento = models.ForeignKey(departamento, verbose_name='Departamento', on_delete=models.CASCADE)
    tipo = models.CharField(u'Tipo', max_length=1, choices=PRIORIDADE_CHOICES)
    cnhcat = models.CharField(u'Categoria CNH ', max_length=2, choices=PRIORIDADE_CHOICES_CNH)
    
    email        = models.CharField(u'E-mail', max_length=30)
    telefone     = models.CharField(u'Telefone Contato', max_length=15)
    cnh          = models.FileField(upload_to="media/", blank=True)
    aut          = models.FileField(upload_to="media/", blank=True)
      
    def __str__(self):
          return self.nome


class veiculo(models.Model):
    PRIORIDADE_CHOICES = (
            ('E','Exclusivo'),       #Somente responsavel pelo Veiculo
            ('C','Compartilhado'),   #Qualquer Usuario do cadastro
            ('F','Frota'),           #Apenas profissionais habilitados
            ('R','Restrito'),        #Apenas profissionais habilitados especializados 
        )
        
    placa = models.CharField(u'Placa', max_length=8)
    tipo = models.CharField(u'Tipo', max_length=1, choices=PRIORIDADE_CHOICES)
    marcamodelo  = models.CharField(u'Marca/Modelo', max_length=40)
    apelido  = models.CharField(u'Apelido', max_length=20)
    Ano  = models.IntegerField(u'Ano Fabricação')
    modelo  = models.IntegerField(u'Modelo Fabricação')
    cor  = models.CharField(u'Cor', max_length=15)
    combustivel  = models.CharField(u'Combustível', max_length=30)
    cidade  = models.CharField(u'Cidade', max_length=15)
    responsavel  = models.ForeignKey(responsavel, verbose_name='Responsável', on_delete=models.CASCADE)
    Odometro  = models.IntegerField(u'Odômetro')

    def __str__(self):
            return self.apelido

class combustivel(models.Model):
      descricao = models.CharField(u'Nome do Combustivel', max_length=30)

      def __str__(self):
            return self.descricao
class posto(models.Model):
    Descricao = models.CharField(u'Nome do Posto', max_length=50)

    def __str__(self):
            return self.Descricao

class tabelacombustivel(models.Model):
    #posto = models.IntegerField(u'Código posto')
    #combustivel = models.IntegerField(u'Combustível')
    #valor = models.DecimalField(u'Valor', max_digits=5, decimal_places=4)
    posto  = models.ForeignKey(posto, verbose_name='Posto', on_delete=models.CASCADE)
    combustivel  = models.ForeignKey(combustivel, verbose_name='Combustivel', on_delete=models.CASCADE)
    valor = models.DecimalField(u'Valor', max_digits=5, decimal_places=4)
    
class manutencao(models.Model):
    Descricao = models.CharField(u'Nome da manutenção', max_length=50)

    def __str__(self):
            return self.Descricao

class empresa(models.Model):
    PRIORIDADE_CHOICES = (
        ('FAEF','FAEF'),
        ('FAIP','FAIP'),
        ('FAIT','FAIT'),
        ('EDUVALES','EDUVALES'),
    )
    fantasia = models.CharField(u'Fantasia', max_length=10, choices=PRIORIDADE_CHOICES)
    nome = models.CharField(u'Nome da Empresa', max_length=50)
    cnpj = models.CharField(u'CNPJ', max_length=14)

    def __str__(self):
            return self.fantasia

class requisicao(models.Model):
    PRIORIDADE_CHOICES = (
        ('TC','Completar'),
        ('LT','Litros'),
        ('LG','Litros no Galão'),
        ('LP','Litros Veiculo Professor'),
    )
    data = models.DateTimeField(default=datetime.now())
    empresa  = models.ForeignKey(empresa, verbose_name='empresa', on_delete=models.CASCADE)
    responsavel = models.ForeignKey(responsavel, verbose_name='Responsavel Abastecimento', on_delete=models.CASCADE)
    veiculo = models.ForeignKey(veiculo, verbose_name='Veiculo', on_delete=models.CASCADE)
    km = models.IntegerField(u'KM atual')
    posto = models.ForeignKey(posto, verbose_name='posto', on_delete=models.CASCADE)
    combustivel = models.ForeignKey(combustivel, verbose_name='Combustível', on_delete=models.CASCADE)
    quantidade = models.IntegerField(u'Quantidade', blank=True)
    tipoabastecimento = models.CharField(u'Tipo Abastecimento', max_length=2, choices=PRIORIDADE_CHOICES)

'''
class Album(TimeStampedModel):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    cover_photo = models.ForeignKey('Photo', related_name='+', blank=True,
                                    null=True)
    is_public = models.BooleanField(default=True)
    date_added = models.DateField(null=True, blank=True)
    tags = TaggableManager(blank=True, help_text=None)
    order = models.PositiveIntegerField(default=9999)

# exemplo Galeria em massa arrastar

class Photo(TimeStampedModel):
    album = models.ForeignKey(Album)
    file = models.ImageField(upload_to=upload_to)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    tags = TaggableManager(blank=True, help_text=None)

'''