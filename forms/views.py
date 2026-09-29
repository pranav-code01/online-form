from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Form, Response


@login_required
def home(request):
    forms = Form.objects.filter(owner=request.user)
    return render(request, 'home.html', {'forms': forms})


@login_required
def create_form(request):
    if request.method == 'POST':
        Form.objects.create(
            owner=request.user,
            title="Student Registration Form"
        )
        return redirect('/')

    return render(request, 'create_form.html')


def view_form(request, form_id):

    form = get_object_or_404(Form, id=form_id)

    if request.method == 'POST':

        name = request.POST['name']
        roll_no = request.POST['roll_no']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']

        Response.objects.create(
            form=form,
            name=name,
            roll_no=roll_no,
            email=email,
            mobile=mobile,
            address=address
        )

        return render(request, 'view_form.html', {
            'form': form,
            'success': 'Your form has been successfully submitted!'
        })

    return render(request, 'view_form.html', {
        'form': form
    })


@login_required
def responses(request, form_id):

    form = get_object_or_404(
        Form,
        id=form_id,
        owner=request.user
    )

    response_data = Response.objects.filter(form=form)

    return render(request, 'responses.html', {
        'form': form,
        'responses': response_data
    })


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


def logout_view(request):

    logout(request)

    return redirect('/login/')