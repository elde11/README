from django import forms

from .models import Grade


class GradeForm(forms.ModelForm):
    grade = forms.IntegerField(max_value=10,min_value=1)

    class Meta:
        model = Grade
        fields = [
            "grade",
        ]

  