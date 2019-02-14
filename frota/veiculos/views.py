from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import departamentoForm,responsavelForm
from .models import responsavel, departamento
#,veiculoForm,combustivelForm,postoForm,tabelacombustivelForm,manutencaoForm, empresaForm, requisicaoForForm


# Create your views here.
#def novo_departamento(request):
#    if request.method == 'POST':
#       form = departamentoForm(request.POST)
#       if form.is_valid():
#           form.save()
#           #return redirect('veiculos/novo_departamento.html')
#           return redirect('veiculos:novo-departamento')
#       else:
#           print(form.errors)
#    else:
#        form = departamentoForm()
#    return render(request, 'veiculos/novo_departamento.html', {'form':form})

def novo_departamento(request):
    if request.method == 'POST':
       #return redirect('veiculos:novo-responsavel')
       form = departamentoForm(request.POST)
       if form.is_valid():
          form.save()
       else:
           print(form.errors)
    else:
#        return HttpResponse('Responsavel adcionado com Sucesso!!!')
        form = departamentoForm()
    return render(request, 'veiculos/novo_departamento.html', {'form':form})

def novo_responsavel(request):
    if request.method == 'POST':
       form = responsavelForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           #return HttpResponse('Responsavel adcionado com Sucesso!!!')
           return redirect('veiculos:novo-responsavel')
       else:
           print(form.errors)
    else:
        form = responsavelForm()
    return render(request, 'veiculos/novo_responsavel.html', {'form':form})

def lista_departamento(request):
    departamentos=departamento.objects.all()
    orm = departamento.objects.all()
    return render(request, 'veiculos/lista_departamento.html',{'deptos':orm})


def lista_responsaveis(request):
    usuarioveic = responsavel.objects.all()
    return render(request, 'veiculos/lista_responsaveis.html',{'colaborador':usuarioveic})


def deleta_departamento(request, id_departamento):
    departamentos = departamento.objects.get(id=id_departamento).delete()
    return render(request, 'veiculos/lista_departamento.html',{'deptos':departamentos})
    #return redirect('veiculos/lista_departamentos.html' )







# exemplo uppload
'''
from django.views.generic import View

from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
    SuperuserRequiredMixin,
)

from calazanblog.gallery.models import Album, Photo


AjaxPhotoUploadView(LoginRequiredMixin,
                    SuperuserRequiredMixin,
                    JSONResponseMixin,
                    AjaxResponseMixin,
                    View):
    """
    View for uploading photos via AJAX.
    """
    def post_ajax(self, request, *args, **kwargs):
        try:
            album = Album.objects.get(pk=kwargs.get('pk'))
        except Album.DoesNotExist:
            error_dict = {'message': 'Album not found.'}
            return self.render_json_response(error_dict, status=404)

        uploaded_file = request.FILES['file']
        Photo.objects.create(album=album, file=uploaded_file)

        response_dict = {
            'message': 'File uploaded successfully!',
        }

        return self.render_json_response(response_dict, status=200)


'''