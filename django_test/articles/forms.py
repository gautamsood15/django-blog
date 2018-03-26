from django.forms import ModelForm
from articles.models import Article,comment

class ArticleForm(ModelForm):
   
    class Meta:                  # used to define something that is not form field .Here it tells the form to use the 
                                 # Article model to save or update information
        model = Article
        fields = ('title','body','pub_date','thumbnail')
       
              
        #form = ArticleForm()
        
        # creating a form to change an existing article
        #articles.Article.objects.get(pk=1)
        #form = ArticleForm(instance=articles)
class CommentForm(ModelForm):
    
    class Meta:
        model = comment
        fields = ('name','body')