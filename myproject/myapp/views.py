from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html', {'message': 'Добро пожаловать на главную страницу!'})

def another_view(request):
    return render(request, 'myapp/non_existent_template.html')  # Шаблон не существует
