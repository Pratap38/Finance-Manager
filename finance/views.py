from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm  # custom signup form
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import Transaction, Goal
from django.utils import timezone
# ✅ Root redirect
def root_redirect(request):
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'signup.html', {'error': "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': "Username already exists."})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup.html')
# Dashboard view
@login_required
def dashboard_view(request):
    transactions = Transaction.objects.filter(user=request.user)

    total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    total_saving = total_income - total_expense

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'total_saving': total_saving,
    }

    return render(request, 'dasboard.html', context)

# ✅ Add Goal view
@login_required
def add_goal_view(request):
    return render(request, 'addgoal.html')

# ✅ Add Transaction view
@login_required
def add_transaction_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = float(request.POST.get('amount'))
        transaction_type = request.POST.get('transaction_type').lower()
        date = request.POST.get('date')
        category = request.POST.get('category')

        Transaction.objects.create(
            user=request.user,
            title=title,
            amount=amount,
            transaction_type=transaction_type,
            date=date,
            category=category
        )
        return redirect('dashboard')

    return render(request, 'addtransaction.html')
# ✅ View Transactions
@login_required
def transaction_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transaction.html', {'transactions': transactions})

class RegisteredUserLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        if user.groups.filter(name='RegisteredUsers').exists():
            return super().form_valid(form)
        else:
            # Log the user out immediately
            logout(self.request)
            return redirect('login')  # or return a page that says "Unauthorized"