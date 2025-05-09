from django.http import HttpResponse

def exam_home(request):
    return HttpResponse("Welcome to the Exam API!")  # Simple response
