from django import forms

from posts.models import Post


class MyForm(forms.Form):
    CHOICES = [('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')]

    my_name = forms.CharField(
        max_length=10,
        required=False,
        initial='Hello',
        label='something else',
        help_text='this helps the user understand',
        widget=forms.Textarea(
            attrs={'cols': 80, 'rows': 10, 'placeholder': 'Enter your name'}
        )
    )

    my_text = forms.CharField(
        widget=forms.Textarea,
    )

    radio = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
    )

    multiple_select = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

class PostForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'autocomplete': 'off'
        })
    )
    class Meta:
        model = Post
        fields = '__all__'

    widgets = {
        'language': forms.RadioSelect(
            attrs={'class': 'radio-select'},
        )

    }





