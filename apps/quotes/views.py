from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from .models import Quote


# =================================================
# 						HELPERS
# =================================================
def current_user(request):
    return User.objects.get(id=request.session['user_id'])


def flash_errors(request, errors):
    for error in errors:
        messages.error(request, error)


# =================================================
# 						RENDER
# =================================================
def index(request):

#CHECK IS THERE IS A USER_ID IN SESSION
    if 'user_id' not in request.session:

# RETURN REDIRECT TO THE INDEX.HTML IF USER_ID NOT IN SESSION
        return redirect('/')

#ELSE SET VARIABLE "USER" TO EQUAL CURRENT_USER // FROM CURRENT_USER HELPER METHOD ABOVE
    user = current_user(request)

#PASS VARIABLES THROUGH CONTEXT
    context = {
        'user': user, 
        'quotes': Quote.objects.all().exclude(favorited_by = user),
        'favorites': user.favorites.all()
    }
    return render(request, 'quotes/index.html', context)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PASS USERID IN THE PARAMETER BECAUSE WE ARE GOING TO USE IT TO DISPLAY THE POSTS FROM THAT USER
def show_user(request, userid):

#SET USER VARIABLE (CAN BE WHATEVER) TO EQUAL THE ID OF THE USER
    user = User.objects.get(id = userid)

#PASS VARIABLES THROUGH CONTEXT
    context = {

#USE THE VARIABLE FROM ABOVE TO EQUAL USER
        'user': user,

#MAKE A KEY QUOTES TO THE QUOTES THAT THE USER POSTED
        'quotes': Quote.objects.filter(posted_by = user),

#MAKE A KEY NAME COUNT THAT WILL COUNT FROM THE USER POSTS
        'count': Quote.objects.filter(posted_by = user).count()
        }
    return render(request, 'quotes/user.html', context)


# =================================================
# 						PROCESS
# =================================================
def create(request):
    if request.method == "POST":
        errors = Quote.objects.validate(request.POST)

        if not errors:
            user = current_user(request)
            Quote.objects.create_quote(request.POST, request.session["user_id"])

        flash_errors(request, errors)
    return redirect('/quotes')


def add_favorite(request,quote_id):

    user = User.objects.get(id=request.session["user_id"])

    favorite = Quote.objects.get(id=quote_id)

    user.favorites.add(favorite)
    #  favorite.favorited_by.add(user)      //same thing as above

    return redirect('/quotes')


def delete_favorite(request,quote_id):
    user = User.objects.get(id=request.session["user_id"])
    favorite = Quote.objects.get(id=quote_id)
    user.favorites.remove(favorite)
    return redirect('/quotes')

