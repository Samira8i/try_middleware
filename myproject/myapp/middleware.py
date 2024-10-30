class GreetingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Привет!")  # Сообщение на этапе обработки запроса
        response = self.get_response(request)
        print("Пока!")  # Сообщение на этапе обработки ответа
        return response


class AdminCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    print(f"Вас зовут {request.user.username}")
                else:
                    print("Неизвестный посетитель")
            else:
                print("Неизвестный посетитель")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

        response = self.get_response(request)
        return response

