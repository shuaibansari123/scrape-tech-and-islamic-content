from .models import *
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget


admin.site.register(ImFeeling)
admin.site.register(Battle)
admin.site.register(Wife)
admin.site.register(MuhammadChildren)
admin.site.register(Hadith)
admin.site.register(Prayer)
admin.site.register(FamilyMember)
admin.site.register(RamadanDua)
admin.site.register(VideoPlaylist)
admin.site.register(Playlist)

class NameOfAllahForm(forms.ModelForm):
    class Meta:
        model = NameOfAllah
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

@admin.register(NameOfAllah)
class NameOfAllahAdmin(admin.ModelAdmin):
    form = NameOfAllahForm


@admin.register(Surah)
class SurahAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')
    search_fields = ('title', 'number')

@admin.register(SurahTranslation)
class SurahTranslationAdmin(admin.ModelAdmin):
    list_display = ('surah', 'language')
    search_fields = ('surah__title', 'language')

@admin.register(DuaDhikr)
class DuaDhikrAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(ProphetStory)
class ProphetStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(Seerah)
class SeerahAdmin(admin.ModelAdmin):
    list_display = ('section', 'subsection', 'title', )
    search_fields = ('section', 'subsection', 'title', )
