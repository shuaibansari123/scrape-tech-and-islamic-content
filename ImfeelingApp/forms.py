from django import forms
from .models import Playlist, VideoPlaylist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title']

class VideoPlaylistForm(forms.ModelForm):
    class Meta:
        model = VideoPlaylist
        fields = ['playlist', 'title', 'file', 'description', 'image', 'image_url']

class PlaylistURLForm(forms.Form):
    playlist_url = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Paste Any YouTube Playlist URL here',
        })
    )
    uploader_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name (Optional)',
        })
    )
    uploader_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email (Optional)',
        })
    )