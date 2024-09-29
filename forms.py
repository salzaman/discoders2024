from django import forms

genre = ['pop', 'rock', 'hip-hop', 'rap', 'r&b',
          'metal', 'salsa', 'lo-fi', 'reggaeton']

class RecommendationForm(forms.Form):
    user_input = forms.ChoiceField(label="What's your jam?", choices = genre)
