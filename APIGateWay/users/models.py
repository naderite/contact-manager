from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    uid = models.IntegerField(_("User ID"), primary_key=True)
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254, unique=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
