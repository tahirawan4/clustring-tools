from django.contrib.postgres.fields import ArrayField
from django.db import models


class SemanticLabel(models.Model):
    intent = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Respons(models.Model):
    text = models.TextField(null=True, blank=True)
    orig_text = models.TextField(null=True, blank=True)
    prob = ArrayField(models.FloatField(), blank=True)
    manual_semantic_label = models.ForeignKey(SemanticLabel, null=True, blank=True)

    def __str__(self):
        return str(self.id)
