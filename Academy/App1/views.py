from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import FormModel,DonateModel,UserDetailModel
# Create your views here.
def index(request):
    if(request.method=="POST"):
        print("Login form entered++++++++++>")
        Name=request.POST['Email']
        Password=request.POST['Password']
        Detail=UserDetailModel.objects.all()
        if((Name,) not in (UserDetailModel.objects.all().values_list('Name'))):
            return render(request,"index.html",{"name_error":True})
        check_pass=UserDetailModel.objects.all().get(Name=Name).Password
        if( (Password!=check_pass) or(Password=="")):
            return render(request,"index.html",{"pass_error":True})
        return redirect("home")
    return render(request,"index.html")

def verify(request):
    return render(request,"verified.html")

def home(request):
   if(request.method == 'POST'):
       return redirect ("verify")
   return render(request,"home.html")

def competition(request):
    return render(request,'competition.html')

def Donate(request):
    tabel=DonateModel.objects.all()
    return render(request,"donation.html",{"List":tabel})

def Forms(request):
    print("FORM++++++++++++++++++++++++++++")
    if(request.method=="POST"):
        print("POST++++++++++++")
        Form=FormModel.objects.all()
        FirstName=request.POST['Firstname']
        LastName=request.POST['LastName']
        if((FirstName,LastName) not in (Form.values_list('FirstName','LastName'))):
            Email=request.POST["Email"]
            City=request.POST["City"]
            State=request.POST["state"]
            pincode=request.POST['pincode']
            competition=request.POST['competition']
            proff=request.POST['file']
            final=FormModel(FirstName=FirstName,LastName=LastName,
                            Email=Email,City=City,State=State,Zip=pincode,
                            competition=competition,File=proff)
            print("+++++++++++Final++++++++++++")
            final.save()
            return redirect("verify")
        else:
            return HttpResponse("Already exisit")
    print("FORM=============================")
    return render(request,'register-form.html')