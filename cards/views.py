from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import ECard
from .forms import ECardForm, SignupForm


# =========================
# HOME
# =========================

def home(request):

    cards = ECard.objects.all()[:6]

    return render(
        request,
        'cards/home.html',
        {'cards': cards}
    )


# =========================
# SIGNUP
# =========================

def signup_view(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = SignupForm()

    return render(
        request,
        'cards/signup.html',
        {'form': form}
    )


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(
                request,
                'cards/login.html',
                {
                    'error': 'Invalid username or password'
                }
            )

    return render(
        request,
        'cards/login.html'
    )


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect('home')


# =========================
# CARD LIST
# =========================

@login_required(login_url='login')
def card_list(request):

    cards = ECard.objects.filter(
        owner=request.user
    )

    return render(
        request,
        'cards/card_list.html',
        {'cards': cards}
    )


# =========================
# CARD DETAIL
# =========================

@login_required(login_url='login')
def card_detail(request, pk):

    card = get_object_or_404(
        ECard,
        pk=pk,
        owner=request.user
    )

    return render(
        request,
        'cards/card_detail.html',
        {'card': card}
    )


# =========================
# CREATE CARD
# =========================

@login_required(login_url='login')
def card_create(request):

    if request.method == 'POST':

        form = ECardForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            card = form.save(commit=False)

            card.owner = request.user

            card.save()

            return redirect('card_list')

    else:

        form = ECardForm()

    return render(
        request,
        'cards/card_form.html',
        {
            'form': form,
            'title': 'Create E-Card'
        }
    )


# =========================
# UPDATE CARD
# =========================

@login_required(login_url='login')
def card_update(request, pk):

    card = get_object_or_404(
        ECard,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':

        form = ECardForm(
            request.POST,
            request.FILES,
            instance=card
        )

        if form.is_valid():

            form.save()

            return redirect(
                'card_detail',
                pk=card.pk
            )

    else:

        form = ECardForm(
            instance=card
        )

    return render(
        request,
        'cards/card_form.html',
        {
            'form': form,
            'title': 'Edit E-Card'
        }
    )


# =========================
# DELETE CARD
# =========================

@login_required(login_url='login')
def card_delete(request, pk):

    card = get_object_or_404(
        ECard,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':

        card.delete()

        return redirect('card_list')

    return render(
        request,
        'cards/card_confirm_delete.html',
        {'card': card}
    )