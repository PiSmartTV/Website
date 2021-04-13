import datetime
from secrets import SystemRandom
from string import ascii_lowercase, digits

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


def get_expire_date():
    return datetime.datetime.now(tz=timezone.utc) \
        + datetime.timedelta(minutes=1)


def generate_code(length=8):
    sr = SystemRandom()

    random_list = [sr.choice(ascii_lowercase + digits) for i in range(length)]

    return ''.join(random_list)


class DeviceCode(models.Model):
    id = models.AutoField(primary_key=True, serialize=True)
    code = models.CharField(
        default=generate_code,
        max_length=8, unique=True,
        null=False
    )

    # TODO: This is stored only to prevent spam, will calculate hash
    # TODO: function to make it more private
    # TODO: Use make_password for this field to make it more private
    ip_address = models.GenericIPAddressField(unique=True, null=False)

    expire_date = models.DateTimeField(default=get_expire_date)
    approved_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True, blank=True
    )
