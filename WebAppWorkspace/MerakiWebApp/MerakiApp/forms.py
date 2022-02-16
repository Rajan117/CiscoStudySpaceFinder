from django import forms
from MerakiApp.models import StudySpace


class StudySpaceForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Enter a study space name to search for it.", required=False)

    max_noise = forms.IntegerField(help_text="Enter the maximum noise level.", required=False)
    min_noise = forms.IntegerField(help_text="Enter the minimum noise level.", required=False)

    max_light = forms.IntegerField(help_text="Enter the maximum light level.", required=False)
    min_light = forms.IntegerField(help_text="Enter the minimum light level.", required=False)

    max_people = forms.IntegerField(help_text="Enter the maximum people level.", required=False)
    min_people = forms.IntegerField(help_text="Enter the minimum people level.", required=False)

    class Meta:
        model = StudySpace
        fields = ('name', 'max_noise', 'min_noise', 'max_light', 'min_light', 'max_people', 'min_people', )

