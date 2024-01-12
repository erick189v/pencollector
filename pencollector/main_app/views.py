from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Pen

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request,'about.html')


def pens_index(request):
   pens = Pen.objects.all()
   return render(request, 'pens/index.html',
                 {
                    'pens': pens
                 }
                )

def pens_detail(request, pen_id):
  pen = Pen.objects.get(id=pen_id)
  return render(request, 'pens/detail.html', { 'pen': pen })

class PenCreate(CreateView):
   model = Pen
   fields = '__all__'

class PenUpdate(UpdateView):
   model = Pen
   fields = ['color','brand','description']

class PenDelete(DeleteView):
   model = Pen
   success_url = '/pens'