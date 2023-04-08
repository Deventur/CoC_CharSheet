from django.db import models
from django.contrib.auth.models import User


class Characteristics(models.Model):
    str = models.PositiveSmallIntegerField(default=5)
    con = models.PositiveSmallIntegerField(default=5)
    siz = models.PositiveSmallIntegerField(default=5)
    dex = models.PositiveSmallIntegerField(default=5)
    app = models.PositiveSmallIntegerField(default=5)
    int = models.PositiveSmallIntegerField(default=5)
    pow = models.PositiveSmallIntegerField(default=5)
    edu = models.PositiveSmallIntegerField(default=5)


class Arts(models.Model):
    art_name1 = models.CharField(max_length=20)
    art_val1 = models.PositiveSmallIntegerField(default=5)
    art_name2 = models.CharField(max_length=20)
    art_val2 = models.PositiveSmallIntegerField(default=5)


class Skills(models.Model):
    accounting = models.PositiveSmallIntegerField(default=10)
    anthropology = models.PositiveSmallIntegerField(default=1)
    archaeology = models.PositiveSmallIntegerField(default=1)

    arts = models.OneToOneField(Arts, on_delete=models.CASCADE)

    astronomy = models.PositiveSmallIntegerField(default=1)
    bargain = models.PositiveSmallIntegerField(default=5)
    biology = models.PositiveSmallIntegerField(default=1)
    chemistry = models.PositiveSmallIntegerField(default=1)
    climb = models.PositiveSmallIntegerField(default=40)
    conceal = models.PositiveSmallIntegerField(default=15)
    craft = models.PositiveSmallIntegerField(default=5)  # Сделать мультистрочным
    credit_rating = models.PositiveSmallIntegerField(default=15)
    cthulhu_mythos = models.PositiveSmallIntegerField(default=0)
    disguise = models.PositiveSmallIntegerField(default=1)
    dodge = models.PositiveSmallIntegerField(default=0)  # (dex*2%)
    drive_auto = models.PositiveSmallIntegerField(default=20)
    electrical_repair = models.PositiveSmallIntegerField(default=10)
    fast_talk = models.PositiveSmallIntegerField(default=5)
    first_aid = models.PositiveSmallIntegerField(default=30)
    geology = models.PositiveSmallIntegerField(default=1)


class Investigative(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(default=1)

    sex = models.CharField(
        max_length=6,
        default='Man'
    )

    characteristics = models.OneToOneField(Characteristics, on_delete=models.CASCADE)
    skill = models.OneToOneField(Skills, on_delete=models.CASCADE)
    luck = models.PositiveSmallIntegerField(default=1)
