from django import forms
from django.core import validators

# /check if user input of name starts with z
# def check_for_z(value):
#     if value[0].lower != 'z':
#         raise forms.ValidationError("Name must start with Z")
# dont forget to pass validators=[check_for_z] in forms.CharField()

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # to confirm the mail second time
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

    # checks whether twice entered mails matchs
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails doesnt match")

# to get a bot method on there is another method to do that. That is inbuilt method of django
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
# the second method is import validators from django.core and in forms class validate usinfg max_lenght of validate method
