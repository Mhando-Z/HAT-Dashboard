from django.db import models
import uuid

# Create your models here.

# Herosection


class HeroSection(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    subtitle = models.CharField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="heroSection/")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dateIssued']

# ptresident


class PresidentSpeech(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    subtitle = models.CharField(null=True, blank=True, max_length=300)
    name = models.CharField(null=True, blank=True, max_length=300)
    cheo = models.CharField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="presidentSection/")
    image2 = models.ImageField(null=True, blank=True,
                               upload_to="presidentSection/")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

# About Us section


class AboutUs(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    subtitle = models.CharField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="AboutUS/")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

# contacts section


class Contacts(models.Model):
    location = models.CharField(null=True, blank=True, max_length=300)
    postcode = models.IntegerField(null=True, blank=True)
    physicalAdress = models.CharField(null=True, blank=True, max_length=300)
    facebook = models.CharField(null=True, blank=True, max_length=300)
    instagram = models.CharField(null=True, blank=True, max_length=300)
    linkedin = models.CharField(null=True, blank=True, max_length=300)
    twitter = models.CharField(null=True, blank=True, max_length=300)
    email1 = models.CharField(null=True, blank=True, max_length=300)
    email2 = models.CharField(null=True, blank=True, max_length=300)
    email3 = models.CharField(null=True, blank=True, max_length=300)
    phoneNumber1 = models.CharField(
        blank=True, max_length=300, null=True, default=0)
    phoneNumber2 = models.CharField(
        blank=True, max_length=300, null=True, default=0)
    phoneNumber3 = models.CharField(
        blank=True, max_length=300, null=True, default=0)
    phoneNumber4 = models.CharField(
        blank=True, max_length=300, null=True, default=0)
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.location

# Policies

# Policies


class Policies(models.Model):
    policy1 = models.CharField(null=True, blank=True, max_length=300)
    policy2 = models.CharField(null=True, blank=True, max_length=300)
    policy3 = models.CharField(null=True, blank=True, max_length=300)
    policy4 = models.CharField(null=True, blank=True, max_length=300)
    policy5 = models.CharField(null=True, blank=True, max_length=300)
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.policy1

    class Meta:
        ordering = ['-dateIssued']


# Gallery Section


class Gallery(models.Model):
    title = models.CharField(null=True, blank=True,
                             max_length=300, default="Hat image")
    image = models.ImageField(null=True, blank=True, upload_to="Gallery/")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dateIssued']


# Gallery Section


class Resources(models.Model):
    title = models.CharField(null=True, blank=True,
                             max_length=300, default="")
    author = models.CharField(null=True, blank=True,
                              max_length=300, default="")
    description = models.TextField(null=True, blank=True)
    document = models.FileField(null=True, blank=True, upload_to='Resouces_Docs/',
                                help_text="Upload the research paper in PDF format.")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dateIssued']


# Companies Section


class Companies(models.Model):
    title = models.CharField(null=True, blank=True,
                             max_length=300, default="Company Name")
    image = models.ImageField(null=True, blank=True,
                              upload_to="CompaniesLogo/")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dateIssued']


# Announcements Section


class Announce(models.Model):
    title = models.CharField(null=True, blank=True,
                             max_length=300, default="Hat")
    description = models.TextField(null=True, blank=True)
    document = models.FileField(null=True, blank=True, upload_to='Announce_Docs/',
                                help_text="Upload the research paper in PDF format.")
    image = models.ImageField(null=True, blank=True,
                              upload_to="Announcements/")

    image2 = models.ImageField(
        null=True, blank=True, upload_to="Announcements/")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dateIssued']

# Announcements Section


# class Reference(models.Model):
#     resource = models.ForeignKey(
#         'Resource', related_name='references', on_delete=models.CASCADE)
#     reference_text = models.CharField(max_length=300, blank=True, null=True)


class Resource(models.Model):
    title = models.CharField(null=True, blank=True,
                             max_length=300, default="Hat")
    subtitle = models.CharField(null=True, blank=True, max_length=300)
    author = models.CharField(null=True, blank=True,
                              max_length=300, default="Hat")
    description = models.TextField(null=True, blank=True)
    document = models.FileField(null=True, blank=True, upload_to='research_papers/',
                                help_text="Upload the research paper in PDF format.")
    image = models.ImageField(null=True, blank=True, upload_to="Resources/")
    image2 = models.ImageField(null=True, blank=True, upload_to="Resources/")
    video_url = models.CharField(
        null=True, blank=True, max_length=300, default="")
    ref1 = models.CharField(null=True, blank=True,
                            max_length=300, default="Hat")
    ref2 = models.CharField(null=True, blank=True,
                            max_length=300, default="Hat")
    ref3 = models.CharField(null=True, blank=True,
                            max_length=300, default="Hat")
    ref4 = models.CharField(null=True, blank=True,
                            max_length=300, default="Hat")
    ref5 = models.CharField(null=True, blank=True,
                            max_length=300, default="Hat")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-dateIssued']


# Call for Conference


class Conference(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    subtitle = models.CharField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    date_of_conference = models.DateTimeField(null=True, blank=True)
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

# terms section


class TermsofService(models.Model):
    term1 = models.CharField(null=True, blank=True, max_length=300)
    term2 = models.CharField(null=True, blank=True, max_length=300)
    term3 = models.CharField(null=True, blank=True, max_length=300)
    term4 = models.CharField(null=True, blank=True, max_length=300)
    term5 = models.CharField(null=True, blank=True, max_length=300)
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.term1

    class Meta:
        ordering = ['-dateIssued']


# Staffs


class Staffs(models.Model):
    name = models.CharField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="Staffs/")
    position = models.CharField(null=True, blank=True, max_length=300)
    contact1 = models.CharField(null=True, blank=True, max_length=300)
    contact2 = models.CharField(null=True, blank=True, max_length=300)
    contact3 = models.CharField(null=True, blank=True, max_length=300)
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

# footer section


class Footer(models.Model):
    title = models.CharField(null=True, blank=True,
                             max_length=300, default="Footer")
    contacts = models.ForeignKey(
        Contacts, null=True, blank=True, on_delete=models.SET_NULL)
    policies = models.ForeignKey(
        Policies, null=True, blank=True, on_delete=models.SET_NULL)
    termsofService = models.ForeignKey(
        TermsofService, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True,
                             upload_to="Logo/")
    dateIssued = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
