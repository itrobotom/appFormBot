from django.db import models

#создаем новый класс, который наследуется от Model, в котором будут поля с данными по заявке
class requestOrder(models.Model):
    #при добавлении полей нужно повторно сделать миграцию
    date_order = models.CharField(max_length=30)
    person = models.CharField(max_length=30) #максимальная длина имени 20 знаков, person = models.CharField(max_length=20, blank=False) поле не может быть пустым  blank=False
    computer = models.CharField(max_length=30)
    classroom = status = models.CharField(max_length=20)
    order = models.CharField(max_length=400)
    status = models.CharField(max_length=30)
    date_finish = models.CharField(max_length=30)
    time_finish = models.CharField(max_length=30)
    #поля для данных при отправке статуса в ЛС по TG
    family_user_tg = models.CharField(max_length=30)
    id_user = models.CharField(max_length=30) #id пользователя в телеграм

    #констуктор класса для отображения имен записей в БД через админку по фамилии или имени, кто оставил заявку
    def __str__(self):
        return self.person
        #кода добавится запрос даты перед записью в БД через f строку выведем название с датой
        #return f'{self.person} {self.date_order}'
