from django.http import HttpResponse
from django.template import loader

from .models import Recepie


def recepie_page(request, recepie_id):
    tmpl = loader.get_template('recepie/recepie_page.html')

    recepie = Recepie.objects.get(pk=recepie_id)

    return HttpResponse(tmpl.render({
        "recepie": recepie,
    }))

def index(request):
    tmpl = loader.get_template('recepie/index.html')

    recepies = Recepie.objects.only('id','name').filter(active=True)

    return HttpResponse(tmpl.render({
        "recepies": recepies,
    }))
