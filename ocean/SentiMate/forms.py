from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .TestB import questions
from .TestA import questionsA
from .TestC import facebook_scrapper, predict, questionsC
from django.core.files import File
from django.conf import settings
import pickle 
import os
import pandas as pd
import numpy as np
import time


class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'emailid', 'facebook', 'linkedin', 'instagram', 'gender', 'bio', 'profile_pic']

# class TestBForm(forms.Form):	
class CompareForm(forms.Form):
   query=forms.CharField(max_length = 100)


class TestBForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		super(TestBForm, self).__init__(*args, **kwargs)
		ANSWER_CHOICES = ((1,1), (2,2),(3,3), (4,4), (5,5))
		tags = list(questions.get_keys_for_questions())
		question = list(questions.get_values_for_questions())
		for i in range(0, 50):
			self.fields[tags[i]] = forms.ChoiceField(choices=ANSWER_CHOICES, widget=forms.RadioSelect(), help_text = question[i])

	def process(self):
		ocean = []
		tags = list(questions.get_keys_for_questions())
		ocean.append(8 + int(self.cleaned_data['OPN1']) - int(self.cleaned_data['OPN2']) + int(self.cleaned_data['OPN3']) - int(self.cleaned_data['OPN4']) + int(self.cleaned_data['OPN5']) - int(self.cleaned_data['OPN6']) + int(self.cleaned_data['OPN7']) + int(self.cleaned_data['OPN8']) + int(self.cleaned_data['OPN9']) + int(self.cleaned_data['OPN10']))
		ocean.append(14 + int(self.cleaned_data['CSN1']) - int(self.cleaned_data['CSN2']) + int(self.cleaned_data['CSN3']) - int(self.cleaned_data['CSN4']) + int(self.cleaned_data['CSN5']) - int(self.cleaned_data['CSN6']) + int(self.cleaned_data['CSN7']) - int(self.cleaned_data['CSN8']) + int(self.cleaned_data['CSN9']) + int(self.cleaned_data['CSN10']))
		ocean.append(20 + int(self.cleaned_data['EXT1']) - int(self.cleaned_data['EXT2']) + int(self.cleaned_data['EXT3']) - int(self.cleaned_data['EXT4']) + int(self.cleaned_data['EXT5']) - int(self.cleaned_data['EXT6']) + int(self.cleaned_data['EXT7']) - int(self.cleaned_data['EXT8']) + int(self.cleaned_data['EXT9']) - int(self.cleaned_data['EXT10']))
		ocean.append(14 - int(self.cleaned_data['AGR1']) + int(self.cleaned_data['AGR2']) - int(self.cleaned_data['AGR3']) + int(self.cleaned_data['AGR4']) - int(self.cleaned_data['AGR5']) + int(self.cleaned_data['AGR6']) - int(self.cleaned_data['AGR7']) + int(self.cleaned_data['AGR8']) + int(self.cleaned_data['AGR9']) + int(self.cleaned_data['AGR10']))
		ocean.append(38 - int(self.cleaned_data['EST1']) + int(self.cleaned_data['EST2']) - int(self.cleaned_data['EST3']) + int(self.cleaned_data['EST4']) - int(self.cleaned_data['EST5']) - int(self.cleaned_data['EST6']) - int(self.cleaned_data['EST7']) - int(self.cleaned_data['EST8']) - int(self.cleaned_data['EST9']) - int(self.cleaned_data['EST10']))
		ocean = [ocean]
		file_path = os.path.join(settings.BASE_DIR, 'SentiMate/TestB/model.pkl')
		with open(file_path, 'rb') as f:
			model = pickle.load(f) 
		file_path = os.path.join(settings.BASE_DIR, 'SentiMate/TestB/clusters.csv')
		dataclusters = pd.read_csv(file_path)
		cluster = model.predict(ocean)
		scores = np.array(dataclusters.iloc[cluster,1:6], dtype = 'int')[0]
		return scores

class TestAForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		super(TestAForm, self).__init__(*args, **kwargs)
		questions, ANSWER_CHOICES = questionsA.get_questions_and_options()
		for i in range(0, 10):
			self.fields['Question' + str(i)] = forms.ChoiceField(choices=ANSWER_CHOICES[i], help_text = questions[i])

	def process(self):
		time.sleep(3)
		scores, ocean = [], []
		for i in range(10):
			x = int(self.cleaned_data['Question' + str(i)])
			scores.append(x)
			if i%2 == 1:
				t = scores[i - 1] + scores[i]
				ocean.append(int(np.round(t/6*100, 2)))
		return ocean

class TestCForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=PasswordInput())

	def process(self):
		username, password = self.cleaned_data['username'], self.cleaned_data['password']
		bot = facebook_scrapper.fb_bot()
		bot.login(username,password)
		posts_scraped,status = bot.post_scraping()
		if status == "success":
			posts_scraped = bot.remove_blank(posts_scraped)
			if posts_scraped == []:
				return [], True, "empty"
			else:
				bot.convert_to_csv(posts_scraped)
				ocean = predict.predict()
				return ocean, True, "fill"
		else:
			return [], False, ""


class TestC1Form(forms.Form):
	def __init__(self, *args, **kwargs):
		super(TestC1Form, self).__init__(*args, **kwargs)
		tags = list(questionsC.get_keys_for_questions())
		question = list(questionsC.get_values_for_questions())
		for i in range(0, 5):
			self.fields[tags[i]] = forms.CharField(widget=forms.Textarea, help_text = question[i])

	def process(self):
		ocean = []
		tags = list(questionsC.get_keys_for_questions())
		ocean.append(self.cleaned_data[tags[0]])
		ocean.append(self.cleaned_data[tags[1]])
		ocean.append(self.cleaned_data[tags[2]])
		ocean.append(self.cleaned_data[tags[3]])
		ocean.append(self.cleaned_data[tags[4]])
		scores = predict.model_predict(ocean,len(ocean))
		return scores
		
