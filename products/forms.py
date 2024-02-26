from django import forms
from .models import *


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ('slide1pics','slide1heading','slide1subheading','slide1writeup',\
                  'slide2pics','slide2heading','slide2subheading','slide2writeup',\
                  'slide3pics','slide3heading','slide3subheading','slide3writeup',\
                  'slide4pics','slide4heading','slide4subheading','slide4writeup',\
                  )
        widgets = {
            'slide1pics': forms.FileInput(attrs = {'class':'form-control', 'placeholder':'Input the title'}),
            'slide1heading': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Input the title'}),
            'slide1subheading': forms.TextInput(attrs = {'class':'form-control'}),
            'slide1writeup': forms.TextInput(attrs = {'class':'form-control'}),
            
        }



   