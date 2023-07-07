from django import forms


class CreateGroupForm(forms.Form):
    title = forms.CharField(label="Title", max_length=20, required=True)
    description = forms.CharField(label="Description", required=False)
    settlers_limit = forms.IntegerField(label="Settlers limit", min_value=1, required=True)
    start_of_lease = forms.DateField(label="Start of lease",
                                     widget=forms.SelectDateWidget(
                                        empty_label=("Choose Year", "Choose Month", "Choose Day")),
                                     required=False)
    end_of_lease = forms.DateField(label="End of lease",
                                   widget=forms.SelectDateWidget(
                                    empty_label=("Choose Year", "Choose Month", "Choose Day")),
                                   required=False)
