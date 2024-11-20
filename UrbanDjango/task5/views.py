from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# def sign_up_by_html(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#
#         print(f'username: {username}')
#         print(f'password: {password}')
#         print(f'repeat_password: {repeat_password}')
#         print(f'age: {age}')
#
#         return HttpResponse(f'Приветствуем, {username}!')
#
#     return render(request, 'fifth_task/registration_page.html')
#
#
# def sign_up_by_django(request):
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
from django.shortcuts import render

# Псевдо-список существующих пользователей
users = ['Alex', 'Mike', 'Kate', 'Frank']

def sign_up_by_django(request):
    info = {}  # Пустой словарь для контекста

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка условий
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request, 'fifth_task/registration_page.html', {'info': info, 'success_message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', {'info': info})


def sign_up_by_html(request):
    info = {}  # Пустой словарь для контекста

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка условий
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request, 'fifth_task/registration_page.html', {'info': info, 'success_message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', {'info': info})

