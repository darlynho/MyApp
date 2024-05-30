from typing import Any, Dict, Tuple
from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    value = models.CharField(max_length=30000)
    reponse = models.CharField(max_length=30000, default='aucune')
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> Tuple[int, Dict[str, int]]:
        return super().delete(using, keep_parents)