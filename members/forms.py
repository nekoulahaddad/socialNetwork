from django import forms
from .models import Profile,Work



class WorkForm(forms.ModelForm):
	class Meta:
		model = Work
		fields = ['work_place','work_date']

class WorkandEducationForm(WorkForm):
	education_place = forms.CharField()
	class Meta(WorkForm.Meta):
		fields = WorkForm.Meta.fields + ['education_place']