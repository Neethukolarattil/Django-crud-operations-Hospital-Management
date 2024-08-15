from django.shortcuts import render,redirect
from .models import *
from .views import *
from django.views import View
from .forms import *

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,"home.html")

class AddpView(View):
    def get(self,request):
        form=PatForm()
        return render(request,"addpat.html",{"form":form})
    def post(self,request):
        form_data=PatForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect("plist")
        return render(request,"addpat.html",{"form":form_data})
    
    
class PListView(View):
    def get(self,request):
        data=Patient.objects.all()
        return render(request,"addplist.html",{"patient":data})


class PDeleteView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        pat=Patient.objects.get(id=pid)
        pat.delete()
        return redirect("plist")
    
class PEditView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        print(pid)
        pat=Patient.objects.get(id=pid)
        form=PatForm(instance=pat)
        return render(request,"addpedt.html",{"form":form})
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        pat=Patient.objects.get(id=pid)
        form_data=PatForm(data=request.POST,instance=pat,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect("plist")
        return render(request,"addpedt.html",{"form":form_data})



    



