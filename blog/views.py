from django.http import HttpResponse
from django.template import loader

# Create your views here.
def blog(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

    template = loader.get_template('order.html')
    return HttpResponse(template.render())

    template = loader.get_template('order.html')
    return HttpResponse(template.render())
