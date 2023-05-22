# redirect добавили для перехода на новую страницу после авторизации
from django.shortcuts import render, redirect #позволяет возрващать шаблоны в виде http response
from django.http import HttpResponse
#добавим модуль для добавления шаблона форм в том числе для входа (через запятую)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#добавим модуль для добавления пользователя
from django.contrib.auth.models import User
#импорт модуля для обработки ошибок связанных с совпадением логина
from django.db import IntegrityError
# чтобы перенаправить пользователя после входа в профиль на новую страницу модуль
# и через запятую модуль выхода logout
# также далее через запятую импортируем функцию для проверки введенных данных при авторизации
from django.contrib.auth import login, logout, authenticate

#для ограничения доступа к станице для неавторизированных пользователей
from django.contrib.auth.decorators import login_required

# для регистации модели добавим, чтобы пользоваться классом requestOrder
from sitetomadmin.models import requestOrder

# импортируем класс для работы с БД
from sitetomadmin.forms import requestOrderForm

# для того, чтобы попасть на домашнюю страницу не нужно писать tomadmin.ru/home
# домашняя это голый домен tomadmin.ru
def home(request): 
    #return HttpResponse('Сайт на стадии разработки') #выведем на главной странице этот текст
    return render(request, 'sitetomadmin/home.html') #откромем целиком страницу http - указываем путь к шаблону, то есть нашей страницы http

#def foo(request):
#    return HttpResponse('Заполнение формы')

def signupuser(request): #принимаем запрос
    # обычное подключение новой страницы с содержимым 
    # return render(request, 'sitetomadmin/signupuser.html') #отобразить html страницу для входа
    # чтобы организовать форму для регистрации
    # первый параметр обязательно request, а затем название нашего шаблона sitetomadmin/signupuser.html
    # внутри sitetomadmin создадим вручную файл signupuser.html 
    # при добавлении 3го параметра {'form':UserCreationForm()} мы подключим стандартную форму входа от django (это готовый модуль)
    # но не забыть подключить перед этим from django.contrib.auth.forms import UserCreationForm вначале
    
    # Когда мы вводим данные в поля обычной формы и нажимаем кнопку, мы используем метод GET
    # метод POST работает при вводе информации через специальные формы, как для регистрации с пометкой POST
    if request.method == 'GET':
        return render(request, 'sitetomadmin/signupuser.html', {'form':UserCreationForm()}) 
        #return render(request, '/tomadmin/sitetomadmin/templates/sitetomadmin/signupuser.html')
    # иначе будет запрос POST
    else:
        # если пароль в первом поле равен паролю во втором поле, то создадим пользователя
        if request.POST['password1'] == request.POST['password2']:
            try:
                # создать нового пользователя в виде объекта и сохраним в переменную
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # сохраним объект в базу данных
                user.save()
                # после того, как пользователь зайдет в свой профиль нужно его перенарпавить на другую страницу
                login(request, user)
                # переходим на новую страницу
                return redirect('helpuser')

            # в случае невозможности сохранения нового пользователя возникает ошибка IntegrityError (по причине уже существующего логина) 
            # при возникновении ошибки IntegrityError
            # не забыть импортировать вначале сам модуль IntegrityError
            except IntegrityError:
                #поэтому вернемся на страницу с формой регистрации, только добавиться четвертый параметр 'error' с сообщением
                # в html signupuser отобразим по ключу error сообщение о том что такое имя пользователя уже используется {{ error }}
                return render(request, 'sitetomadmin/signupuser.html', {'form':UserCreationForm(), 'error':'Такое имя пользователя уже используется в системе. Пожалуйста задайте другой логин.'})

        else:
            #Ошибка регистрации пользователя (пароли не совпадают)
            #поэтому вернемся на страницу с формой регистрации, только добавиться четвертый параметр 'error' с сообщением
            # в html signupuser отобразим по ключу error сообщение о не совпадении паролей {{ error }}
            return render(request, 'sitetomadmin/signupuser.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают'})

def loginuser(request):
    # взяли полностью функцию signupuser и немного изменили ее
    if request.method == 'GET':
        return render(request, 'sitetomadmin/loginuser.html', {'form':AuthenticationForm()}) 
    
    else:
        #проверим введенный логин и пароль с помощью встроенной функции django
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        #если пользователя с такими данными нет, то перенаправим его на страницу входа
        if user is None:
            return render(request, 'sitetomadmin/loginuser.html', {'form':AuthenticationForm(), 'error':'Данные введены неверно'})
        #если данные введены верно
        else:
            # после того, как пользователь зайдет в свой профиль нужно его перенарпавить на другую страницу
            login(request, user)
            # переходим на новую страницу
            return redirect('helpuser')


# создадим функцию для выхода пользователя только через POST запрос
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        # перенапривим пользователя на домашнюю страницу
        return redirect('home')

# https://docs.djangoproject.com/en/4.1/topics/auth/default/
# 'sitetomadmin/signupuser.html', {'form':UserCreationForm()}
@login_required (login_url='/login/') #приписка для ограниченя доступа по указанному адресу для авторизованных пользователей 
def helpuser(request):
    #получим данные с формы для сохранения в БД
    # form = requestOrderForm()
    # # создадим словарь, заполним который как раз с данными из формы
    # data = {
    #     'form': form
    # }

    #новая попытка сделать запись в БД при нажатии кнопки отправить
    # if request.method == 'POST':
    #     all_order = requestOrder.objects.all() #objects - менеджер, а all() - метод этого менеджера
    #     new_order = requestOrder(person = 'Сергей')
    #     new_order.save()
    # all_order = requestOrder.objects.all()
    # return render(request, 'sitetomadmin/helpuser.html', {'all_order': all_order})


    # if request.method == 'GET':
    #     return render(request, 'sitetomadmin/helpuser.html') # с заполненными данными из формы для возврата return render(request, 'sitetomadmin/helpuser.html', data)
    # else: #if request.method == 'POST'
    #     # name = request.POST['name']
    #     # new_order = requestOrder(person = request.POST['name'])
    #     # new_order.save()
    #     # requestOrder.objects.create(person = "Сергей")
    #     new_order = requestOrder(person = 'Сергей')
    #     new_order.save()
    



    #27.02.2023
    # если обратились к странице, то выведем форму
    if request.method == 'GET':
        return render(request, 'sitetomadmin/helpuser.html') 
    
    #['person', 'computer', 'classroom', 'order', 'date_finish', 'time_finish', 'family_user_tg', 'id_user']
    # Если нажали кнопку, то это POST запрос, то значит отправили данные в базу и вывели также снова все данные
    elif request.method == 'POST':
        new_order = requestOrder(person = request.POST['name'], computer = request.POST['numpc'], classroom = request.POST['numcab'], order = request.POST['problem'], date_finish = request.POST['dateform'], time_finish = request.POST['timeform'])
        new_order.save()
        all_order = requestOrder.objects.all()
        return render(request, 'sitetomadmin/helpuser.html', {'all_order': all_order}) 




    #по простому показать страницу без работы с БД
    #return render(request, 'sitetomadmin/helpuser.html')


################ РАБОТА С БАЗОЙ ДАННЫХ
@login_required (login_url='/login/') #приписка для ограниченя доступа по указанному адресу для авторизованных пользователей 
def historder(request):
    #импортируем из models.py нашу модель requestOrder 
    #получаем все записи, а точнее объекты из нашей таблицы (БД)
    
    #при обновлении страницы сразу создается новая запись в базе с одним полем person 
    # all_order = requestOrder.objects.all() #objects - менеджер, а all() - метод этого менеджера
    # new_order = requestOrder(person = 'Сергей')
    # new_order.save()
    # return render(request, 'sitetomadmin/historder.html', {'all_order': all_order})

    # загружаем все заявки, чтобы отобразить потом их на странице
    all_order = requestOrder.objects.all()
    return render(request, 'sitetomadmin/historder.html', {'all_order': all_order}) 
    

    


    #добавим фильтр по записям, которые нам нужны
    #например последние 10 шт
    #или кода появится поле с датой (date_order), можно получить за конкретный день
    # filter_order =  requestOrder.objects.filter(date_order = 'получить сегодняшнюю дату')
    
    # пройтись по всем элементам кадой записи модели
    # for order in all_order:
    #     print(i.person, i.order)

    # создать новую запись в БД
    # new_order = requestOrder(date_order = "11.12.23", person = "Сергей", classroom = "19", order = "Не работает ноутбук", status = "В работе")
    # сохранить новую запись в БД
    # new_order.save()
    # или более короткий способ внести новую запись
    # requestOrder.objects.create(date_order = "11.12.23", person = "Сергей", classroom = "19", order = "Не работает ноутбук", status = "В работе")

    #изменить какую либо запись в БД
    #если нужно найти только одну запись, например по номеру id, то метод get
    # status_to_change = requestOrder.objects.get(id=5)
    #изменим поле 
    # status_to_change.status = "Готово"
    # status_to_change.save()

    # удаление полей из БД
    # requestOrder.objects.get(id=5).delete()


    

