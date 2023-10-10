from django.core import validators
from django import forms

from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
    #sobre escribir el metodo save
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
    
    username = forms.CharField(label="Usuario*",
                               required=True,
                               widget=forms.TextInput(
                                   attrs={"placeholder":"Usuario",
                                          'class':'form-control'}
                               ))
    first_name = forms.CharField(label="Nombre*", 
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={"placeholder":"Nombre",
                                            'class':'form-control'}
                                 ))
    last_name = forms.CharField(label="Apellidos*",
                                required=True,
                                widget=forms.TextInput(
                                    attrs={"placeholder":"Apellidos",
                                           'class':'form-control'}
                                ))
    fechaNac = forms.DateField(label="Fecha de Nacimiento(opcional)",
                                   widget=forms.DateInput(
                                       attrs={'placeholder':"mm/dd/aaaa",
                                                'class':'form-control'}
                                )) 
    email = forms.EmailField(label="Correo electrónico*",
                             required=True,
                            validators=[
                                #por defecto el campo emailfiel saca un mensaje de error entre a valida email adress
                                #validators.EmailValidator("Introduce un Correo electrónico correcto", "Invalid E-mail"),
                                    ],     
                             widget=forms.EmailInput(
                                 attrs={"placeholder":"Correo electrónico",
                                        'class':'form-control'}
                             ))
    password1 = forms.CharField(label="Contraseña*",
                                required=True,
                                validators=[
                                    validators.MinLengthValidator(8,"Tu contraseña debe tener al menos 8 caracteres")
                                    ],
                                widget=forms.PasswordInput(
                                    attrs={'placeholder':"Contraseña",
                                            'class':'form-control'}))  
    password2 = forms.CharField(label="Repite Contraseña*",
                                required=True,
                                validators=[
                                    validators.MinLengthValidator(8,"Tu contraseña debe tener al menos 8 caracteres")
                                    ],
                                widget=forms.PasswordInput(
                                    attrs={'placeholder':"Contraseña",
                                            'class':'form-control'})) 



class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico",
                             required=True,
                             widget=forms.EmailInput(
                                 attrs={'placeholder':"Correo electrónico",
                                        'class':'form-control'}))
    password = forms.CharField(label="Contraseña",
                               required=True,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder':"Contraseña",
                                            'class':'form-control'}))

    
    def clean_email(self):
        # esto que se recoje es un e-mail
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            print(user.email)
        except User.DoesNotExist:
            raise forms.ValidationError("Estas seguro que estas registrado? Usuario no encontrado.")
        return email
    

    def clean_password(self):
        # esto que se recoje es un e-mail
        email = self.cleaned_data.get('email')  
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
            print(user.email)   
        except:
            user = None
        # si el usuario existe y la password es incorrecta
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Contraseña Inválida.")
        elif user is None:
            pass
        #este else es, que el usuario existe y la password es correcta
        else:
            print("pasa por el else de return password")
            return password
        print("pasa por la funcion principal")
        return password
   