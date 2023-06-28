from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Order
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Account
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth import get_user_model



@login_required
def profile(request):
    user = request.user
    try:
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        account = None
    orders = Order.objects.filter(user=user)
    groups = user.groups.all()
    context = {'user': user, 'account': account, 'orders': orders, 'groups': groups}
    return render(request, 'user_profile/profile.html', context)


User = get_user_model()

class AccountUpdateForm(UserChangeForm, forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    class Meta:
        model = Account
        fields = ['phone', 'view_personal_info', 'gender', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in UserChangeForm.base_fields:
            self.fields[fieldname] = UserChangeForm.base_fields[fieldname]
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        del self.fields['last_login']
        del self.fields['is_superuser']
        del self.fields['groups']
        del self.fields['user_permissions']
        del self.fields['is_staff']
        del self.fields['is_active']
        del self.fields['date_joined']
        
    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return super().save(commit=commit)


class AccountUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("staff:login")
    model = Account
    form_class = AccountUpdateForm
    template_name = 'user_profile/update_profile.html'
    success_url = reverse_lazy('user_profile:profile')