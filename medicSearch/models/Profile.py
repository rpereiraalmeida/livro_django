# Importamos todas as models da pasta models
from medicSearch.models import*



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    # atributo image adicionado apos instalação da biblioteca Pillow
    image = models.ImageField(null=True, blank=True)
    # Adicionando campos ManyToMany
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    specialities = models.ManyToManyField(Speciality, blank=True, related_name='specialities')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')

    def __str__(self):
        return '{}'.format(self.user.username)

    # notação informa que o metodo post create_user_profile deve ser acionado
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    # notação informa que o metodo post save_user_profile deve ser acionado
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass