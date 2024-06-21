# Responsavel por comunicar ao Django quais models 
# refletirao a estrutura da nossa base de dados

# bibliotecas para as models que serão criadas
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

# todas as models a serem utilizadas deverao ser declaradas aqui
from .Rating import Rating
from .DayWeek import DayWeek
from .State import State
from .City import City
from .Neighborhood import Neighborhood
from .Address import Address
from .Speciality import Speciality
from .Profile import Profile