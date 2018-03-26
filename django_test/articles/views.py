from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from articles.models import Article,comment
from forms import ArticleForm,CommentForm
from django.http import HttpResponseRedirect
from django.utils import timezone


def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']
    
    return render_to_response('articles.html',{'articles':Article.objects.all(),'language':language,'session_language':session_language})


def language(request,language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang',language)
    request.session['lang'] = language
    return response


def article(request,article_id=1):
    return render_to_response('article.html',{'article':Article.objects.get(id=article_id)} )


# Create your views here.

def hello(request):
    name  = 'Mike'
    html = '<html><body> Hi %s,this seems to be working</body></html>'%name
    return HttpResponse(html)

def hello_template(request):
    name = "Gautam"
    t = get_template('hello.html')
    html = t.render(Context({'name':name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name = "gautam" 
    return render_to_response('hello.html',{'name':name})
    
    
class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'
    
    def get_context_data(self,**Kwargs):
        context = super(HelloTemplate,self).get_context_data(**Kwargs)
        context['name'] = 'Gautam'
        return  context
    
          
          
def create(request):
    if request.POST:
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True);
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
        return render(request,'create_article.html',{'form':form})
    
        
        
def like_article(request,article_id): 
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count+=1    
        a.likes = count
        a.save()
        return HttpResponseRedirect('/articles/get/%s' % article_id)
    
    
    
    
def add_comment(request,article_id):
    a = Article.objects.get(id=article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a  # link btw article and comment
            c.save()
            return HttpResponseRedirect('/articles/get/%s'%article_id)
    else:
        f = CommentForm()
        return render(request,'add_comment.html',{'form':f,'article':a})
    
    
    
def search_titles(request):
    if request.method=="POST":
        search_text = request.POST['request_text']
    else:
        search_text = ''
    articles = Article.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html',{'articles':articles})