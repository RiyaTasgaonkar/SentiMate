from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .TestB import questions
import pickle
import pandas as pd
import numpy as np

class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'emailid', 'facebook', 'linkedin', 'instagram', 'gender', 'bio']

class TestBForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		super(TestBForm, self).__init__(*args, **kwargs)
		ANSWER_CHOICES = ((1,1), (2,2),(3,3), (4,4), (5,5))
		tags = list(questions.get_keys_for_questions())
		question = list(questions.get_values_for_questions())
		for i in range(0, 50):
			self.fields[tags[i]] = forms.ChoiceField(choices=ANSWER_CHOICES, widget=forms.RadioSelect(),help_text = question[i])


	def process(self):
		ocean = []
		tags = list(questions.get_keys_for_questions())
		ocean.append(8 + int(self.cleaned_data['OPN1']) - int(self.cleaned_data['OPN2']) + int(self.cleaned_data['OPN3']) - int(self.cleaned_data['OPN4']) + int(self.cleaned_data['OPN5']) - int(self.cleaned_data['OPN6']) + int(self.cleaned_data['OPN7']) + int(self.cleaned_data['OPN8']) + int(self.cleaned_data['OPN9']) + int(self.cleaned_data['OPN10']))
		ocean.append(14 + int(self.cleaned_data['CSN1']) - int(self.cleaned_data['CSN2']) + int(self.cleaned_data['CSN3']) - int(self.cleaned_data['CSN4']) + int(self.cleaned_data['CSN5']) - int(self.cleaned_data['CSN6']) + int(self.cleaned_data['CSN7']) - int(self.cleaned_data['CSN8']) + int(self.cleaned_data['CSN9']) + int(self.cleaned_data['CSN10']))
		ocean.append(20 + int(self.cleaned_data['EXT1']) - int(self.cleaned_data['EXT2']) + int(self.cleaned_data['EXT3']) - int(self.cleaned_data['EXT4']) + int(self.cleaned_data['EXT5']) - int(self.cleaned_data['EXT6']) + int(self.cleaned_data['EXT7']) - int(self.cleaned_data['EXT8']) + int(self.cleaned_data['EXT9']) - int(self.cleaned_data['EXT10']))
		ocean.append(14 - int(self.cleaned_data['AGR1']) + int(self.cleaned_data['AGR2']) - int(self.cleaned_data['AGR3']) + int(self.cleaned_data['AGR4']) - int(self.cleaned_data['AGR5']) + int(self.cleaned_data['AGR6']) - int(self.cleaned_data['AGR7']) + int(self.cleaned_data['AGR8']) + int(self.cleaned_data['AGR9']) + int(self.cleaned_data['AGR10']))
		ocean.append(38 - int(self.cleaned_data['EST1']) + int(self.cleaned_data['EST2']) - int(self.cleaned_data['EST3']) + int(self.cleaned_data['EST4']) - int(self.cleaned_data['EST5']) - int(self.cleaned_data['EST6']) - int(self.cleaned_data['EST7']) - int(self.cleaned_data['EST8']) - int(self.cleaned_data['EST9']) - int(self.cleaned_data['EST10']))
		ocean = [ocean]
		model = pickle.load(open("C:\\Users\\Riya\\Desktop\\SentiMate\\ocean\\SentiMate\\TestB\\model.pkl", 'rb')) 
		dataclusters = pd.read_csv('C:\\Users\\Riya\\Desktop\\SentiMate\\ocean\\SentiMate\\TestB\\clusters.csv')
		cluster = model.predict(ocean)
		scores = np.array(dataclusters.iloc[cluster,1:6], dtype = 'int')[0]
		return scores
