import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets, status
from pimo.models import Order, Offer, Post
from users.models import user
from pimo.serializers import OrderSerializer, OfferSerializer, PostSerializer, OrderCreateSerializer
from django.forms import modelformset_factory
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer



from .models.offer import OfferForm
from .models.order import OrderForm
from users.models.user import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from pimo import server


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.action == 'create':
            serializer = OrderCreateSerializer

        return serializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def index(request):
    queryset = Order.objects.all()
    books = Order.objects.all()
    three_books = []
    r = 0
    for i in range(3, len(books), 3):
        buff = [books[i - 2], books[i - 1], books[i]]
        three_books.append(buff)
        r = i
    while r < len(books):
        three_books.append([books[r]])
        r += 1
    return render(request, 'pimo/Main-Page.html', {'orders': queryset, 'offers': queryset, 'counter': three_books})


def index2(request):
    queryset = Order.objects.all()
    queryset2 = Offer.objects.all()
    return render(request, 'pimo/My-Orders.html', {'orders': queryset, 'offers': queryset2})


@csrf_exempt
def index3(request):
    host = '127.0.0.1'
    port = 1060
    if request.method == 'POST' and 'run_script' in request.POST:
        # import function to run
        from pimo import server , client

        # call function
        server.main()
        client.main(host, int(port))
        # return user to required page
        return redirect('../My-Offers.html/')
    queryset = Order.objects.all()
    queryset2 = Offer.objects.all()
    return render(request, 'pimo/My-Offers.html', {'orders': queryset, 'offers': queryset2})


@csrf_exempt
def index4(request):
    queryset = Order.objects.all()
    queryset2 = Offer.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            obj = form.save(commit=False)
            obj.created_by = request.user
            print(form)
            print("Valid Form")
            form.save()
            return redirect("../My-Orders.html/")
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            return render(request, 'pimo/Create-Order.html', {'orders': queryset, 'offers': queryset2, 'form': form})
        # if a GET (or any other method) we'll create a blank form
    else:
        form = Order()
    form = OrderForm()
    return render(request, 'pimo/Create-Order.html', {'orders': queryset, 'offers': queryset2, 'form': form})


@csrf_exempt
def index5(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("../../index/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            print(form.cleaned_data.get('username'))
            print(form.cleaned_data.get('password'))
            print("Invalid Form")
            print(form.errors)
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'pimo/login.html', {'form': form})


@csrf_exempt
def index6(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.password = make_password(user.password)
            user.save()
            messages.success(request, "Registration successful.")
            return redirect("../index/")
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request, 'pimo/registration.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("../../index/")



@csrf_exempt
def make_offer(request):
    form = OfferForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Offer = form.save()
            Offer.save()
            print("Valid Form")
            messages.info(request, "Success")
            return redirect('/index')
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            messages.error(request, "Please correct the form")
    return render(request,'pimo/accdec.html', {'form': form})


@csrf_exempt
def offers(request):
    form = OfferForm(request.POST)
    queryset = Order.objects.all()
    queryset2 = Offer.objects.all()
    if request.method == 'POST':
        stat = form.cleaned_data.get('stat')
        stat = 'A'
    return render(request,'pimo/Offers.html', {'orders': queryset, 'offers': queryset2, 'form': form})
