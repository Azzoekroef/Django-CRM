from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authentikasi
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "kamu Telah login!")
            return redirect('home')
        else:
            messages.success(request, "ada eror di login, coba lagi")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

#def login_user(request):
#   pass

def logout_user(request):
    logout(request)
    messages.success(request, "kamu telah logout")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #fitur langsung masuk diambil dari data yang baru dimasukan jadi
            #jadi cleaned datana itu data yang bersih atau baru abis diPOST pada form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password = password)
            login(request, user)
            messages.success(request, "kamu Telah berhasil register")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "kamu harus login")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"kamu berhasil menghapusnya")
        return redirect('home')
        
    else:
        messages.success(request, "kamu harus login")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record ditambahkan")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "kamu harus login")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance= current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'record telah di update')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "kamu harus login")
        return redirect('home')