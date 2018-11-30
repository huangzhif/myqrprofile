from django import forms

from .models import ExamModel


class ExamForm(forms.ModelForm):

    class Meta:
        model = ExamModel
        fields = ['qrpic', 'remark', 'contrast', 'brightness']
        # exclude = ["newname"]
