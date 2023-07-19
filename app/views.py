from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import file_form, S_form, F_form
from .models import file, Students, Faculty, User
from .forms import LoginForm, SignUp
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

@login_required
def report(request):
    return render(request,'reports.html')
#pdf_report
def pdf(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",15)
    f=file.objects.all()

    
    lines=[]
    for i in f:
        lines.append("Name:"+str(i.name))
        lines.append("Date:"+str(i.date))
        lines.append("Source:"+str(i.source))
        lines.append("File:"+str(i.fo))
        lines.append('------------------------------------------------------------------------------------------------')
        

    

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='files.pdf')

def pdf1(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",15)
    f=Students.objects.all()

    
    lines=[]
    for i in f:
        lines.append("Name:"+str(i.Name))
        lines.append("USN:"+str(i.Usn))
        lines.append("Email:"+str(i.Email))
        lines.append("Sem:"+str(i.Sem))
        lines.append('------------------------------------------------------------------------------------------------')
        

    

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='Students.pdf')

def pdf2(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",15)
    f=Faculty.objects.all()

    
    lines=[]
    for i in f:
        lines.append("Name:"+str(i.Name))
        lines.append("SSN:"+str(i.Ssn))
        lines.append("Email:"+str(i.Email))
        lines.append('------------------------------------------------------------------------------------------------')
        

    

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='Faculty.pdf')


@login_required
def Names(request):
    num = file.objects.all()
    nums = num.count()
    f = num.filter(fo='Student_file').count()
    f1 = num.filter(fo='Faculty_file').count()
    f2 = num.filter(fo='common_file').count()
    f3 = num.filter(fo='Admin').count()

    context = {
        'num': num,
        'nums': nums,
        'f': f,
        'f1': f1,
        'f2': f2,
        'f3': f3,



    }
    return render(request, 'home_page.html', context)


@login_required
def fileform(request, id=0):
    if request.method == 'GET':
        if id == 0:
            f = file_form()
        else:
            std = file.objects.get(pk=id)
            f = file_form(instance=std)
        return render(request, 'files_form.html', {'file_form': f})
    else:
        if id == 0:
            f = file_form(request.POST, request.FILES)

        else:
            std = file.objects.get(pk=id)
            f = file_form(request.POST, request.FILES, instance=std)
        if f.is_valid():
            f.save()
        return redirect('/files_list')


@login_required
def Student_form(request, id=0):
    form = S_form()
    if request.method == 'GET':
        if id == 0:
            f = S_form()
        else:
            std = Students.objects.get(pk=id)
            f = S_form(instance=std)
        return render(request, 'S_form.html', {'S_form': f})
    else:
        if id == 0:
            f = S_form(request.POST)
        else:
            std = Students.objects.get(pk=id)
            f = S_form(request.POST, instance=std)
        if f.is_valid():
            f.save()
        return redirect('/S_list')


@login_required
def Faculty_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            f = F_form()
        else:
            std = Faculty.objects.get(pk=id)
            f = F_form(instance=std)
        return render(request, 'F_form.html', {'F_form': f})
    else:
        if id == 0:
            f = F_form(request.POST)
        else:
            std = Faculty.objects.get(pk=id)
            f = F_form(request.POST, instance=std)
        if f.is_valid():
            f.save()
        return redirect('F_list')


@login_required
def file_list(request):
    if 's' in request.GET:
        s = request.GET['s']
        mq = Q(Q(name__icontains=s) | Q(
            date__icontains=s) | Q(source__icontains=s))
        context = file.objects.filter(mq)
    else:
        context = file.objects.all()
    return render(request, 'files_list.html', {'context': context})


@login_required
def S_list(request):
    if 's' in request.GET:
        s = request.GET['s']
        mq = Q(Q(Name__icontains=s) | Q(Usn__icontains=s) |
               Q(Email__icontains=s) | Q(Sem__icontains=s))
        context = Students.objects.filter(mq).order_by('-Usn')
    else:
        context = Students.objects.all().order_by('-Usn')
    return render(request, 'S_list.html', {'context': context})


@login_required
def F_list(request):
    if 's' in request.GET:
        s = request.GET['s']
        mq = Q(Q(Name__icontains=s) | Q(
            Ssn__icontains=s) | Q(Email__icontains=s))
        context = Faculty.objects.filter(mq)
    else:
        context = Faculty.objects.all()
    return render(request, 'F_list.html', {'context': context})


@login_required
def fdelete(request, id):
    std = file.objects.get(pk=id)
    fs = FileSystemStorage()
    fs.delete(std.name)
    std.delete()
    return redirect('/files_list')


@login_required
def Sdelete(request, id):
    std = Students.objects.get(pk=id)
    std.delete()
    return redirect('/S_list')


@login_required
def Faculty_delete(request, id):
    std = Faculty.objects.get(pk=id)
    std.delete()
    return redirect('/F_list')


@login_required
def chart(request):
    num = file.objects.all()
    nums = num.count()
    f = num.filter(fo='Student_file').count()
    f1 = num.filter(fo='Faculty_file').count()
    f2 = num.filter(fo='common_file').count()
    f3 = num.filter(fo='Admin').count()
    s1=num.filter(source='Principal office').count()
    s2 = num.filter(source='Department').count()
    s3 = num.filter(source='Dean Academics').count()

    context = {
        'num': num,
        'nums': nums,
        'f': f,
        'f1': f1,
        'f2': f2,
        'f3': f3,
        's1':s1,
        's2':s2,
        's3':s3,

    }

    return render(request, 'chart.html', context)


def login_view(request):
    
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('studenthome')
            elif user is not None and user.is_staff:
                login(request,user)
                return redirect('temp')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            temp1 = form.cleaned_data.get('is_student')
            temp2 = form.cleaned_data.get('is_staff')
            temp3 = form.cleaned_data.get('is_admin')
            if temp1 == True and temp2 == True:
                msg = 'Choose One'
            else:
                if temp1 == True:
                    if Students.objects.filter(Usn=username, Email=email).exists():
                        user = form.save()
                        msg = 'user created'
                        return redirect('login')
                    else:
                        msg = 'USN is not present'

                elif temp2 == True:
                    if Faculty.objects.filter(Ssn=username, Email=email).exists():
                        user = form.save()
                        msg = 'user created'
                        return redirect('login')
                    else:
                        msg = 'SSN is not present'
                elif temp3 == True:
                    user = form.save()
                    msg = 'user created'
                    return redirect('login')
                else:
                    msg = 'Not Valid User'

        else:
            msg = 'form is invalid'

    else:
        form = SignUp()

    return render(request, 'register.html', {'form': form, 'msg': msg})





@login_required
def studenthome(request):
    if 's' in request.GET:
        s = request.GET['s']
        mq = Q(Q(name__icontains=s) | Q(
            date__icontains=s) | Q(source__icontains=s))
        context = file.objects.filter(mq).filter(fo='Student_file')
    else:
        context = file.objects.filter(fo='Student_file')

    return render(request, 'studenthome.html', {'context': context})

def temp(request): 
    if 's' in request.GET:
        s = request.GET['s']
        mq = Q(Q(name__icontains=s) | Q(date__icontains=s) | Q(source__icontains=s))
        context = file.objects.filter(mq).filter(fo='Faculty_file')
    else:
        context = file.objects.filter(fo='Faculty_file')
    return render(request, 'temp.html',{'context': context})