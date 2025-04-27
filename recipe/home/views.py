from django.shortcuts import render, HttpResponse, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password!")
            return redirect("/login")
        else:
            login(request, user)  # Log in the user
            return redirect("/")
    
    return render(request, 'login.html')


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out successfully.")
    return redirect('/login')

def register_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            return redirect('/register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account registered successfully')
            return redirect('/register')

    return render(request, 'register.html')


@login_required(login_url='/login')
def home(request):
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # print(recipe_name, recipe_description, recipe_image)

        recipe = Recipe(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
        recipe.save()
        return redirect('/')

    recipes = Recipe.objects.all()
    context = {'recipes': recipes}

    return render(request, 'home.html', context)

def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    recipe.delete()
    return redirect('/')

def update_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()

    if request.method == 'POST':
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')

        if request.FILES.get('recipe_image'):
            recipe.recipe_image = request.FILES.get('recipe_image')
        
        recipe.save()
        return redirect('/')

    context = {'recipe': recipe}
    return render(request, 'update.html', context)