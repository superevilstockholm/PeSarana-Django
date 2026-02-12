from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from student.models import Student
from user.models import User

from .forms import SignUpForm

# Create your views here.
def login(request: HttpRequest):
    return render(request=request, template_name='login.html')

def signup(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            nisn = form.cleaned_data['nisn']
            dob = form.cleaned_data['dob']
            student = Student.objects.filter(nisn=nisn).first()
            if not student:
                form.add_error('nisn', 'NISN tidak ditemukan.')
            elif student.user:
                form.add_error('nisn', 'NISN sudah terikat dengan akun.')
            elif student.dob != dob:
                form.add_error('dob', 'Tanggal lahir tidak cocok.')
            else:
                user = User.objects.create_user(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                student.user = user
                student.save()
                return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})