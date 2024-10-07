from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.name}'


class FamilyGroup(models.Model):
    group_name = models.CharField(max_length=50, verbose_name="가족명", unique=True)
    members = models.ManyToManyField(Customer, related_name='family_members', verbose_name="가족 구성원")

    def save(self, *args, **kwargs):
        if not self.group_name:
            last_group = FamilyGroup.objects.order_by('id').last()
            if last_group:
                last_number = int(last_group.group_name.split('_')[-1])
                self.group_name = f'family_{last_number + 1}'
            else:
                self.group_name = 'family_1'
        super(FamilyGroup, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.group_name}'