from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group


class userr(AbstractUser):
    phoneNo = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'

    groups = models. ManyToManyField(
    Group,
    related_name='users', # Use a descriptive related_name
    )
    user_permissions = models. ManyToManyField(
    Permission,
    related_name='users', # Use a descriptive related_name
    )

class Image(models.Model):
    filename = models.CharField(max_length=100)
    filepath = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Images'

class UserProfile(models.Model):
    user = models.OneToOneField(userr, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    notification_preference = models.BooleanField(default=True)
    project_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'UserProfiles'


class Domain(models.Model):
    project_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'ProjectDomains'


class Team(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(userr, on_delete=models.CASCADE, related_name='team_head')
    member1 = models.ForeignKey(userr, on_delete=models.CASCADE, related_name='team_member1')
    member2 = models.ForeignKey(userr, on_delete=models.CASCADE, related_name='team_member2')
    member3 = models.ForeignKey(userr, on_delete=models.CASCADE, related_name='team_member3')
    member4 = models.ForeignKey(userr, on_delete=models.CASCADE, related_name='team_member4')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'TeamsRegistered'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=255)
    description = models.TextField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    lead = models.ForeignKey(userr, on_delete=models.SET_NULL, null=True, default=None)
    project_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.title} - {self.lead}"

    class Meta:
        db_table = 'Projects'


class ProjectLead(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    head = models.ForeignKey(userr, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.head} - {self.project}"
    
    class Meta:
        db_table = 'ProjectLead'