from django.contrib.auth.backends import BaseBackend #Get all users authenticated list in django
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser #required to get user_id
from django.db.models import Q

class Email_OR_Username(BaseBackend):
    #Get user by user_id
    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        try:
            print(f"get_user_model de la funcion get_user {get_user_model().objects.get(id=user_id)}")
            return get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist:
            return None
            
        
    #Authenthication(email or username)    
    def authenticate(self, request, username=None, password=None) -> AbstractBaseUser | None:
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email__iexact=username)) # | Q(username__exact=username)
            print(f"User de la funcion authenticate {user}")
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        

