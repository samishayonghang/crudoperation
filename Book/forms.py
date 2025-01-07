from.models import Review
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
