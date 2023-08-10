from django.db import models
from django.conf import settings
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW','SportWear'),
    ('OW','OuterWear'),
    
)
LABEL_CHOICES = (
    ('Discount','primary'),
    ('Sale','secondary'),
    ('New','danger'),
    
)
    
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True,null=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    label = models.CharField(choices=LABEL_CHOICES,max_length=9)
    slug = models.SlugField()
    description = models.TextField()


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("order:productdetail",kwargs={
            'slug': self.slug
        })
    def get_add_to_cart_url(self):
        return reverse("order:add-to-cart",kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("order:remove-from-cart",kwargs={
        'slug': self.slug
    })
        

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    startdate = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk} by {self.user.email} - Ordered: {self.ordered}"



# __str__ method in a Django model is used to define a human-readable string representation of an 
# instance of that model. When you try to convert an instance of the model to a string (e.g., when it's 
# displayed in the admin panel or used in print statements), Django calls the __str__ method to determine
#  what text should be displayed.