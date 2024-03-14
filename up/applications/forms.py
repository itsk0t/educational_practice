from django import forms
from applications.models import Applications


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['full_name',
                  'date_birth',
                  'passport_series',
                  'passport_number',
                  'phone',
                  'address',
                  'document_id',
                  'files',
                  'comment',
                  ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ФИО'}),
            'date_birth': forms.DateInput(attrs={'class': 'form-input', 'placeholder': 'Дата рождения'}),
            'passport_series': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Серия паспорта'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Номер паспорта'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Номер телефона'}),
            'address': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Адрес проживания'}),
            'document_id': forms.Select(attrs={'class': 'form-input', 'placeholder': 'Документ'}),
            # 'files': forms.FileField(),
            'comment': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Комментарий'}),
            # 'user_id': forms.IntegerField()
        }