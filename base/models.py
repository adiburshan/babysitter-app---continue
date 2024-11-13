from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User



# The Babysitter model
class Babysitter(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='babysitters_profile_pics/', blank=False, null=False, default='static/default_image.jpg')
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)


    def __str__(self):
            return self.name


# The Parents model
class Parents(models.Model):
    family_id = models.AutoField(primary_key=True)
    dad_name = models.CharField(max_length=255)
    mom_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='parents_profile_pics/', blank=False, null=False, default='static/default_image.jpg')
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)

    def __str__(self):
        return self.last_name


# The Kids model
class Kids(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Parents, related_name='kids', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    fields = ['name', 'age', 'family']

    def __str__(self):
        return self.name


# The Info model
class Meetings(models.Model):
    id = models.AutoField(primary_key=True)
    meeting_time = models.DateTimeField()
    family = models.ForeignKey(Parents, related_name='meetings', on_delete=models.CASCADE)
    babysitter = models.ForeignKey(Babysitter, related_name='meetings', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    fields = ['meeting_time', 'family', 'babysitter']

    def __str__(self):
        return f"Meeting on {self.meeting_time} between {self.family} and {self.babysitter}"
    

# The Reviews model
class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Parents, related_name='reviews', on_delete=models.CASCADE)
    babysitter = models.ForeignKey(Babysitter, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    fields = ['review_text', 'rating', 'family', 'babysitter']

    def __str__(self):
        return f"Review for {self.babysitter} by {self.family}"




# The Availability model
class Availability(models.Model):
    id = models.AutoField(primary_key=True)
    babysitter = models.ForeignKey(Babysitter, related_name='availability', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Availability for {self.babysitter}"





class TimeWindow(models.Model):
    id = models.AutoField(primary_key=True)
    availability = models.ForeignKey(Availability, related_name='availability', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"from {self.start_time} to {self.end_time} on {self.date}"




class Requests(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    ]
    
    id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Parents, related_name='requests',  on_delete=models.CASCADE)
    babysitter = models.ForeignKey(Babysitter, related_name='requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request from {self.family} to {self.babysitter} - {self.status}"














# # The Message model
# class Message(models.Model):
#     id = models.AutoField(primary_key=True)
#     # Sender (can be either Parents or Babysitter)
#     sender_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='sender_type')
#     sender_object_id = models.PositiveIntegerField()
#     sender = GenericForeignKey('sender_content_type', 'sender_object_id')

#     # Receiver (can be either Parents or Babysitter)
#     receiver_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='receiver_type')
#     receiver_object_id = models.PositiveIntegerField()
#     receiver = GenericForeignKey('receiver_content_type', 'receiver_object_id')
    
#     content = models.TextField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"You got a message from {self.sender}"