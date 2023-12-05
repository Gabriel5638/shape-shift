from django.db import models

class ContactUs(models.Model):

    class Meta:
        verbose_name_plural = "Contact Us"

    email_address = models.EmailField()
    name = models.CharField(
        max_length=100
        )
    message_subject = models.CharField(max_length=400)
    message = models.TextField()
    message_date = models.DateTimeField(
        auto_now_add=True
        )
    reply_sent = models.BooleanField(default=False)

    REGARDING_LIST = [
        ('refunds', 'Refunds'),
        ('vouchers', 'Vouchers'),
        ('products', 'Products'),
        ('other reason', 'Other reason'),

    ]
    regarding = models.CharField(
        max_length=24,
        choices=REGARDING_LIST,
        default='Select'
        )

    def __str__(self):
        return self.name
