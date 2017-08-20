from django.db import models
 #create your models here.
class cakes(models.Model):
    """Almacena las publicaciones realizadas por el equipo
    administrativo """
    title = models.CharField(max_length=50,help_text= 'Ingrese el titulo de la pagina web')
    name= models.CharField(max_length=50,help_text='Ingrese el nombre del cakes que desea')
    kind=models.CharField(max_length=30,help_text='Ingrese el tipo de pastel que desea')
    synopsis=models.CharField(max_length=500,help_text='Pequena resena')


class sale(models.Model):
    prices=models.ForeignKey(cakes,help_text='Ingrese el precio')
    customers=models.CharField(max_length=30,help_text='Ingrese el nombre del cliente')

class comment(models.Model):
    sale=models.ForeignKey(sale,help_text='seleccione la publicacion')
    comment = models.CharField (max_length=1000,help_text='Escriba su comentario')
    pubdate=models.DateTimeField(auto_now=True)
