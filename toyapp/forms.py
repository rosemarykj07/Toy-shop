from django import forms
from .models import Reg_tbl

class Regform(forms.ModelForm):
    class Meta:
        model = Reg_tbl
        fields = ['email','psw','rpsw','fname','lname','gender']
        widgets = {
            'email':forms.EmailInput
            (attrs = {'class':'form_control','placeholder':'EMAIL','style':'width:500px;height:50px;border-radius:10px;border-color:green'}),
            'psw':forms.PasswordInput
            (attrs = {'class':'form_control','placeholder':'PASSWORD','style':'width:500px;height:50px;border-radius:10px;border-color:green'}),
            'rpsw':forms.PasswordInput
            (attrs = {'class':'form_control','placeholder':'CONFIRM','style':'width:500px;height:50px;border-radius:10px;border-color:green'}),
            'fname':forms.TextInput
            (attrs = {'class':'form_control','placeholder':'FIRSTNAME','style':'width:500px;height:50px;border-radius:10px;border-color:green'}),
            'lname':forms.TextInput
            (attrs = {'class':'form_control','placeholder':'LASTNAME','style':'width:500px;height:50px;border-radius:10px;border-color:green'}),
            'gender':forms.TextInput
            (attrs = {'class':'form_control','placeholder':'GENDER','style':'width:500px;height:50px;border-radius:10px;border-color:green'})
        
        }







        



        