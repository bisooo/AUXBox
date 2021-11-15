from django import forms

GENRES = (
    ('Hip Hop' , 'Hip Hop'),
    ('RnB' , 'RnB'),
    ('Jazz' , 'Jazz'),
    ('Soul', 'Soul'),
    ('Reggae', 'Reggae'),
    ('3Daqat', '3Daqat')
)

class EventForm(forms.Form):
    title = forms.CharField(max_length=50, label='Title:')
    spotify_genre = forms.ChoiceField(label='Vibe:', choices=GENRES)
    location = forms.CharField(max_length=50, label='Location:')
    date = forms.DateField(widget=forms.TextInput(attrs={'type' : 'date'}), label='Date:')
    time = forms.TimeField(widget=forms.TimeInput, label='Time:')
    min_price = forms.IntegerField(min_value=0,label='Min. Price Request:')
    description = forms.CharField(widget=forms.Textarea, label='Description:')


