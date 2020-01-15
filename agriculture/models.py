from django.db import models

from dashboard.models import Sector


class Crops(models.Model):
    crop_name = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Crops"
        verbose_name_plural = "Crops"

    def __str__(self):
        return self.crop_name


class Seeds(models.Model):
    seed_name = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Seeds"
        verbose_name_plural = "Seeds"

    def __str__(self):
        return self.seed_name


class Fertilizers(models.Model):
    name = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Fertilizers"
        verbose_name_plural = "Fertilizers"

    def __str__(self):
        return self.name


class UnusedTerassis(models.Model):
    name = models.CharField(max_length=200)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Unused Terrasis"
        verbose_name_plural = "Unused Terrassis"

    def __str__(self):
        return self.name


class Banana_and_Rehabilitation(models.Model):
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Banana and Rehabilitation"
        verbose_name_plural = "Banana and Rehabilitation"

    def __str__(self):
        return self.name


class Ubwanikiro(models.Model):
    ubwanikiro = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Ubwanikiro"
        verbose_name_plural = "Ubwanikiro"

    def __str__(self):
        return self.ubwanikiro


class Trainings(models.Model):
    training_name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Trainings"
        verbose_name_plural = "Trainings"

    def __str__(self):
        return self.training_name


class Vaccination(models.Model):
    vaccination_name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Vaccination"
        verbose_name_plural = "Vaccinations"

    def __str__(self):
        return self.vaccination_name


class Insemination(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    insemination = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Insemination"
        verbose_name_plural = "Insemination"

    def __str__(self):
        return str(self.sector)


class InkaZizakurikiranwa(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    inka_zizakurikiranwa = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Inka Zizakurikiranwa"
        verbose_name_plural = "Inka Zizakurikiranwa"

    def __str__(self):
        return str(self.sector)


class Girinka(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    girinka = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Girinka"
        verbose_name_plural = "Girinka"

    def __str__(self):
        return str(self.sector)


class Umuhigo(models.Model):
    umuhigo = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    target = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Umuhigo"
        verbose_name_plural = "Umuhigo"

    def __str__(self):
        return self.umuhigo


class Ha_irrigated(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    ha_irrigated = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Ha Irrigated"
        verbose_name_plural = "Ha Irrigated"

    def __str__(self):
        return str(self.sector)


class Pumps_in_Sector(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    number_of_pumps = models.PositiveIntegerField()
    achieved = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Pumps in Sector"
        verbose_name_plural = "Pumps in Sectors"

    def __str__(self):
        return str(self.sector)