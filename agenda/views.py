'''from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.http import HttpResponse

# Create your views here.

#def index(request):
#	return HttpResponse('<h2> Hey</h2>')


from models import ItemAgenda

def lista(request):
	lista_itens = ItemAgenda.objects.all()
	return render("lista.html",{'lista_itens': lista_itens})
'''
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
#from django.views.decorators.csrf import csrf_protect
#from django.views.generic import list_detail
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import ItemAgenda
from .forms import FormItemAgenda

def lista(request):
	lista_itens = ItemAgenda.objects.all()
	return render_to_response("lista.html",{'lista_itens': lista_itens})

@csrf_exempt
def adiciona(request):
	form = FormItemAgenda()
	return render_to_response("adiciona.html", {'form': form})
		
'''
@login_required
def lista(request):
    return list_detail.object_list(
        request,
        queryset = ItemAgenda.objects.filter(usuario=request.user),
        template_name = "lista.html",
        template_object_name="itens",
        paginate_by=2,
    )		
'''		
	