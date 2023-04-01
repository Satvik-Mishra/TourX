from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
        else:
            print(form.errors)
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)




