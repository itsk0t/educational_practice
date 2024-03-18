from django import forms
from applications.models import Applications


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['document_id',
                  'full_name',
                  'date_birth',
                  'passport_series',
                  'passport_number',
                  'phone',
                  'address',
                  'files',
                  'comment',
                  ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'ФИО'}),
            'date_birth': forms.DateInput(attrs={'class': 'form-control w-75', 'placeholder': 'Дата рождения'}),
            'passport_series': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Серия паспорта'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Номер паспорта'}),
            'phone': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Номер телефона'}),
            'address': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Адрес проживания'}),
            'document_id': forms.Select(attrs={'class': 'form-control w-75', 'placeholder': 'Документ'}),
            # 'files': forms.FileField(),
            'comment': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'Комментарий'}),
            'user_id': forms.IntegerField()
        }