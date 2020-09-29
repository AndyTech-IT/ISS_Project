from django.db import models

class Salespeople(models.Model):
    SNUM = models.IntegerField('Номер агента')
    SNAME = models.CharField('Имя агента', max_length=20)
    CITY = models.CharField('Город, где работает агент', 
        max_length=20)
    COMM = models.FloatField('Коммисионные торгового агента')

    def __str__(self):
        return self.SNAME

    class Meta:
        verbose_name = 'Торговый агент'
        verbose_name_plural = 'Торговые агенты'
    pass

class Customers(models.Model):
    CNUM = models.IntegerField('Номер покупателя')
    
    CNAME = models.CharField('Имя покупателя', 
        max_length=20)

    CITY = models.CharField('Город проживания покупателя', 
        max_length=20)

    RATING = models.IntegerField
    ('Некоторый рейтинг, присвоенный покупателю')

    SNUM = models.IntegerField
    ('Номер торгового агента, за которым закреплен покупатель')

    def __str__(self):
        return self.CNAME

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
    pass

class Orders(models.Model):
    ONUM = models.IntegerField('Номер заказа')
    AMT = models.FloatField('Сумма заказа')
    ODATE = models.DateField('Дата  заказа')
    CNUM = models.IntegerField('Номер покупателя')
    SNUM = models.IntegerField('Номер торгового агента')

    def __str__(self):
        return str(self.ONUM)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
    pass


