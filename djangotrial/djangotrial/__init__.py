# from django.db import models

# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, null=False)
#     slug = models.CharField(max_length=50, null=False)
#     description = models.CharField(max_length=50, null=False)
#     parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, null=False)
#     slug = models.CharField(max_length=50, null=False)
#     description = models.CharField(max_length=50, null=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name