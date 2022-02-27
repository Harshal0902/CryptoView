from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

from pathlib import Path
import random
from .models import *

from django.contrib.auth.decorators import login_required
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.



def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def layout(request):
    return render(request, 'layout.html')

def postNFT(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='media/nft')
        filename = fs.save(myfile.name, myfile)
        temp = nft()
        temp.user = request.user
        temp.image = filename
        temp.price = request.POST['price']
        temp.save()
        return redirect('orders')
        
    return render(request, 'postNFT.html')

def userHome(request):
    return render(request, 'userHome.html')

def userOrder(request):
    temp = nft.objects.all()
    return render(request, 'userOrder.html',{'nfts':temp})

def chatroom(request):
    return render(request, 'chatroom.html')



