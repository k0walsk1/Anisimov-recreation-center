from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):
    yslyga = forms.CharField(
        label='Выберите услугу',
        widget=forms.Select(choices=Articles.SERVICE_CHOICES, attrs={'class': 'form__input drop'}),
        required=True
    )
    phone = forms.CharField(label='Телефон', max_length=10, widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': '+ 7'}))
    email = forms.CharField(label='Почта', max_length=250, widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'E-mail'}))
    coment = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'class': 'form__input', 'placeholder': 'Комментарий'}))

    class Meta:
        model = Articles
        fields = ['yslyga', 'phone', 'email', 'coment']
