from django.shortcuts import redirect, render
from .forms import CommentForm  
from .models import Comment

def book_comments(request, pk): 
    comments = Comment.objects.filter(book_id=pk) 
    form = CommentForm()
    return render(request, 'comments/includes/comments.html', {'comments': comments, 'form': form})

def add_comment(request, pk):
    comments = Comment.objects.filter(book_id=pk)  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.book_id = pk
            comment.user = request.user    
            comment.save()
            return redirect('directories:view-book', pk=pk)   
    else:
        form = CommentForm()     
        return render(request, 'comments/includes/comments.html', {
            'comments': comments, 
            'form': form
        })