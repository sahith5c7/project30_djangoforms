from django import forms
g=[['MALE','male'],['FEMALE','female']]

c=[['PYTHON','PYTHON'],['DJANGO','DJANGO'],['SQL','SQL']]

class NameForm(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':7,'rows':5}))
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
