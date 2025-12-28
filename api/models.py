from django.db import models

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()    # SQL integer
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reviews"   # SQL table name

    def __str__(self):
        return f"{self.user_name} ({self.rating})"