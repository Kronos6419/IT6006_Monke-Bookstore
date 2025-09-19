from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import Profile

# Create your views here.
class RegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/register.html'    
    success_url = reverse_lazy('login') 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()

        Profile.objects.create(
            user=user,
            dob=form.cleaned_data['dob'],
            phone_number=form.cleaned_data['phone_number']
        )
        
        return super().form_valid(form)



