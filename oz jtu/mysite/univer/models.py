from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=128, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Basic_menu(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    menu = models.ForeignKey(Menu, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    basic = models.ForeignKey(Basic_menu, blank=True, null=True, on_delete=models.SET_NULL)
    views = models.PositiveIntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    full_name = models.CharField(max_length=128, blank=False, null=False)
    profession = models.TextField(blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    time = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
