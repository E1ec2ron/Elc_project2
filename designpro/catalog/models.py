from django.db import models

class Application(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Добавте описание заявки")
    category = models.ManyToManyField('CategoryApplic', help_text="Выберите категорию")
    #image = models.ImageField(upload_to='images/')

    APPL_STATUS = (
        ('n', 'Новая'),
        ('w', 'Принято в Работу'),
        ('d', 'Выполнено'),
    )

    status = models.CharField(max_length=1, choices=APPL_STATUS, blank=True, default='n', help_text="Выберите статус")

    def __str__(self):
        return self.title

    def display_category(self):
        return ', '.join([category.name for category in self.category.all()[:3]])
    display_category.short_description = 'category'

class CategoryApplic(models.Model):
    name = models.CharField(max_length=200, help_text="Введите категорию для заявки")

    def __str__(self):
        return self.name
