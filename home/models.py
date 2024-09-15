from django.db import models

##class Grade(models.Model):
    # = models.CharField(max_length=100)
    #subjects = models.TextField()  # قائمة بالمواد الدراسية
    #description = models.TextField(blank=True)  # وصف الصف الدراسي
    #image = models.ImageField(upload_to='grades/', blank=True, null=True)  # صورة للصف الدراسي

    #def __str__(self):
       # return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    rating = models.FloatField()
    likes = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_valid_until = models.DateField()

    def __str__(self):
        return self.name

class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schedule = models.TextField()
    seats_available = models.IntegerField()
    total_seats = models.IntegerField()

    def __str__(self):
        return f'Class by {self.teacher.name}'