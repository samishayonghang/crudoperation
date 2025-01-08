from.models import Review,Authentic
from django import forms 


class ReviewForm(forms.ModelForm):
   class Meta:
      model=Review
      fields=['Title','Author','Genre','Description','Comments','Rating']
      widgets={
         'Title':forms.TextInput(attrs={'placeholder':'Enter your Book title'}),
         'Author':forms.TextInput(attrs={'placeholder':'Enter the Author name',}),
          'Genre':forms.RadioSelect(attrs={'class':'genre-select'}),

      }
class LoginForm(forms.ModelForm):
   class Meta:
      model= Authentic
      fields=['username','password']

class SignupForm(forms.ModelForm):
   class Meta:
      model= Authentic
      fields=['first_name','last_name', 'username','email','password']