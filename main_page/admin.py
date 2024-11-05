from django.http import HttpResponse


def first_lesson_django(request):
    if request.method == 'GET':
        return HttpResponse('Hello Djangos!!!')


def picture_view(request):
    if request.method == 'GET':
        return HttpResponse('https://itproger.com/img/news/1592990176.jpg')
