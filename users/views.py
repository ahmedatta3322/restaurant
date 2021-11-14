from django.core.exceptions import ObjectDoesNotExist 
from django.http import HttpResponseRedirect
from .models import CustomUser
from django.views import generic
from .forms import LoginForm
# Create your views here.
class UserLogin(generic.TemplateView):
    form_class = LoginForm
    template_name="login.html"
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = CustomUser.objects.get(number=cd["number"])
            except CustomUser.DoesNotExist :
                return HttpResponseRedirect('/users/login?DoesNotExist=True')
            
            return HttpResponseRedirect('/success/')
        
