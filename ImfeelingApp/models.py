from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class ImFeeling(models.Model):
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    body = RichTextUploadingField()
    feeling_name = models.CharField(
        _("Feeling Name"), max_length=100,
        null=False, blank=False
    )
    description = models.TextField(
        _("Description"), null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

# models.py
from django.db import models
from ckeditor.fields import RichTextField

class DuaDhikr(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()  # Using CKEditor for rich text
    image = models.ImageField(upload_to='prayer_images/')  # Field to store the image
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class RamadanDua(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()  
    reference = models.CharField(max_length=255)
    image = models.ImageField(upload_to='prayer_images/')  # Field to store the image
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class ProphetStory(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()  # Using CKEditor for rich text
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Prayer(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = RichTextField()  # For advanced content display
    image = models.ImageField(upload_to='prayer_images/')  # Field to store the image
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
from django.db import models
from django.utils.text import slugify

class NameOfAllah(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='prayer_images/')  # Field to store the image
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Seerah(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(null=True, blank=True)  # This will store the content with formatting
    section = models.CharField(max_length=255)  # To categorize sections
    subsection = models.CharField(max_length=255, blank=True, null=True)  # For subsections
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='seerah_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class FamilyMember(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    content = RichTextField(null=True, blank=True)  # Use RichTextField for rich text content
    image = models.ImageField(upload_to='family_member_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.name
    

class MuhammadChildren(models.Model):
    name = models.CharField(max_length=255)
    content = RichTextField() 
    image = models.ImageField(upload_to='children_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.name

class Battle(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()  # Use RichTextField for rich text content
    image = models.ImageField(upload_to='battle_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.title


class Wife(models.Model):
    name = models.CharField(max_length=255)
    content = RichTextField()  # Use RichTextField for rich text content
    image = models.ImageField(upload_to='wife_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)



class Hadith(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()  # Use RichTextField for rich text content
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='hadith_images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Surah(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return self.title

class SurahTranslation(models.Model):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    content = RichTextField(null=True, blank=True)

    recitator_by = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.surah.title} - {self.language}"
    


class Playlist(models.Model):
    title = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='israr_ahmad/', null=True, blank=True)
    # image_url = models.URLField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
    

def default_json_uploaded_by():
    return {'name': 'shuaib', 'email': 'shuaibansari4044@gmail.com'}

class VideoPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='playlists', on_delete=models.CASCADE , null=True, blank=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos_israr_ahmad/' , null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    # likes =  models.PositiveIntegerField(default=0)
    # comments =  models.JSONField(default=dict)

    description = RichTextField(blank=True , null=True)
    image = models.ImageField(upload_to='israr_ahmad/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    

    uploaded_by = models.JSONField(default=default_json_uploaded_by)

    def __str__(self):
        return self.title
    

