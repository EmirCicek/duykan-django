from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from AppMy.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


# Create your views here.


def kayitPage(request):
    if request.method == "POST":
        ad = request.POST.get("ad")
        soyad = request.POST.get("soyad")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        kayit_kod = request.POST.get("kayit-kod")
        # print(adsoyad,username,email,password,kayit_kod)
        if ad and soyad and username and email and password and kayit_kod:
            if not User.objects.filter(username = username).exists(): # Eğer aynı kullanıcı adına sahip biri sistemde yoksa
                if not User.objects.filter(email = email).exists(): # Eğer aynı email sahip biri sistemde yoksa
                    if str(kayit_kod) == "5251": # Çalışan ekleme kodu
                        user = User.objects.create_user(first_name=ad, last_name=soyad,username = username, password = password, email = email)
                        user.save()
                        return redirect("/")
                    elif str(kayit_kod) == "2511": # Super kullanıcı ekle
                        user = User.objects.create_superuser(first_name=ad, last_name=soyad,username = username, password = password, email = email)
                        user.save()
                        return redirect("/")

    context = {}
    return render(request, 'user/kayit.html', context)

def girisPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
        

    context = {}
    return render(request, 'user/giris.html', context)


@login_required(login_url="giris")
def hesap_ayarlariPage(request):
    if request.method == "POST":
        user = request.user
        ad = request.POST.get("ad")
        soyad = request.POST.get("soyad")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Update user fields
        user.first_name = ad
        user.last_name = soyad
        user.username = username
        user.email = email

        if password:
            user.set_password(password)  # Hash the password

        user.save()

        # Update session auth hash if password changed
        if password:
            update_session_auth_hash(request, user)

        return redirect("/")  # Redirect to home page or preferred location

    else:
        context = {"user": request.user}
        return render(request, "hesap_ayarlari.html", context)
