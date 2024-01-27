from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.MAX_LENGTH_NAME,
    help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
    # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
# to avoid the max length repetition etc, could have a stored vairble inside teh model that states teh max length of a feild

    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=Page.URL_MAX_LENGTH, help_text="Please enter the URL of the page.") 
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) # essentually an automatic entry

    class Meta:
        model = Page
# we can either exclude the category field from the form,
        exclude = ('category',)
 # or specify the fields to include (don't include the category field).
 #fields = ('title', 'url', 'views')
    def clean(self):
    # basically, cleans up the data. MUST: return cleaned_data dictionairy, 
    
    
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'): # seems like this bit needs to make all urls http://
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data
