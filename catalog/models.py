from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class Product(models.Model):
	name = models.CharField(max_length=50, verbose_name='наименование')
	description = models.TextField(verbose_name='описание')
	image = models.ImageField(upload_to='media/photo', **NULLABLE)
	category = models.ForeignKey(on_delete=models.SET_NULL, verbose_name='категория',  **NULLABLE, related_name='products')
	price = models.IntegerField(verbose_name='цена')
	created_at = models.DateField(auto_created=True, verbose_name='дата создания')
	updated_at = models.DateField(auto_now_add=True, verbose_name='дата изменения')

	def __str__(self):
		return self.name, self.description

	class Meta:
		verbose_name = 'продукт'
		verbose_name_plural = 'продукты'
		ordering = ('name', 'category')


class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name='наименование')
	description = models.TextField(verbose_name='описание')

	def __str__(self):
		return self.name, self.description

	class Meta:
		verbose_name = 'категория'
		verbose_name_plural = 'категории'
		ordering = ('name',)
