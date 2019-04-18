from django.db import models
import random

# Create your models here.


class DeadBody(models.Model):
    prof_index = models.CharField(max_length=12)
    profession_rus = models.CharField(max_length=12)
    items_string = models.TextField()

    def __str__(self):
        return self.prof_index

    def random_item(self):
        inventory = str(self.items_string).split(', ')
        chosen = inventory[random.randrange(0, len(inventory))]
        first_symbol = chosen[0]
        all_symbols = (chosen[1:])
        first_symbol = first_symbol.title()
        return first_symbol + all_symbols
