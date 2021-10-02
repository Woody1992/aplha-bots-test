from django.db import models


class ReferralUser(models.Model):
    referral_code = models.CharField(max_length=8)
    name = models.CharField(max_length=155)

    def __str__(self):
        return f"{self.name}, referral - {self.referral_code}"


class FormResults(models.Model):
    chat_id = models.CharField(max_length=55)
    tg_username = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=55)
    answers = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.name} - @{self.tg_username}'

    class Meta:
        verbose_name_plural = 'Form Results'
