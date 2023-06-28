from django.db import models

class OTP_db(models.Model):
    email=models.CharField(max_length=100)
    otp=models.CharField(max_length=4)

    def __str__(self) -> str:
        return "OTP of"+self.email