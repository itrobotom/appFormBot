from sitetomadmin.models import requestOrder 
from django.forms import ModelForm, TextInput, DateTimeInput

class requestOrderForm(ModelForm):
    class Meta:
        model = requestOrder
        # укажем поля из models.py, в которых будут данные
        # первое поле 'date_order' не указываю, т.к. оно автоматически должно определяться при отправке
        # поле 'status' тоже удаляем, оно автоматически будет ставиться 'В работе'
        fields = ['person', 'computer', 'classroom', 'order', 'date_finish', 'time_finish', 'family_user_tg', 'id_user']

        # widgets = {
        #     'person': TextInput(attrs={
        #         'class': 'form-control important-input',
        #         'placeholder': 'Фадеев М.А.',
        #         'name': 'name' #для отправки по tg
        #     }),
        #     'date_finish': DateTimeInput(attrs={
        #         'class': 'form-control',
        #         'type': 'date'
        #     }),
        #     'time_finish': DateTimeInput(attrs={
        #         'class': 'form-control',
        #         'type': 'time'
        #     })
        # }
