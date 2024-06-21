from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):

    id = models.IntegerField(_("Contact ID"), primary_key=True)
    full_name = models.CharField(_("Full Name"), max_length=100)
    phone_number = PhoneNumberField(_("Phone Number"), unique=True)
    email = models.EmailField(_("Contact Email"), max_length=254)
    job = models.CharField(_("Contact Job"), max_length=200)
    address = models.CharField(_("Contact Address"), max_length=100)
    skills = models.TextField(_("Contact Skills"))
    notes = models.TextField(_("Additional Notes"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})
