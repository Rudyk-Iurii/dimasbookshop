from .models import Book
from django.db.models import Q
from django.conf import settings
from .forms import BookForm, ContactForm
from django.core.mail import send_mail
from django.shortcuts import render, Http404, get_object_or_404, redirect
import pandas as pd
import crispy_forms
# Create your views here.



def home(request):
    instance = Book.objects.all().order_by("title")
    query = request.GET.get("q")
    if query:
        instance = instance.filter(
            Q(title__icontains=query)|
            Q(author__icontains=query)


        ).distinct()
    context = {
        "instance": instance
    }
    return render(request, "home.html", context)


def book_add(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.save()
        return redirect(book.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "book_add.html", context)


def book_edit(request, id=None):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        book = form.save(commit=False)
        book.save()
        context = {
            "book": book,
            "form": form,
            "result": book.get_absolute_url()
        }
        return redirect(book.get_absolute_url())

    context = {
        "book": book,
        "form": form,
        "result": "no result"
    }
    return render(request, "book_add.html", context)


def book_detail(request, id=None):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    book = get_object_or_404(Book, id=id)
    # if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    # share_string = quote_plus(instance.iata)
    quary = book.author
    same_author = Book.objects.all().filter(author__icontains=quary)

    context = {
        "book": book,
        "same_author": same_author
    }
    return render(request, "book_detail.html", context)


def book_delete(request, id=None):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/')


def book_migrate(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    book_list = Book.objects.all()
    if request.method == "POST":
        instance = pd.read_excel("Books/Books.xlsx")
        for index, row in instance.iterrows():
            try:
                if row["Название"] not in book_list and row['Автор']:
                    book = Book()
                    book.title = row["Название"]
                    book.author = row["Автор"]
                    book.price = row["Цена"]
                    book.condition = row["Описание"]
                    book.save()
                    print(index, row['Название'], row['Автор'])
                    # print(type(row["Автор"]))
            except:
                print("Value Error")
        context = {"result": "migrated"}
        return render(request, 'book_migrate.html', context)
    context = {"result": "waiting for migration"}
    return render(request, 'book_migrate.html', context)


def contact_form(request):
    title = "Contact us!"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = "Книжный магазин"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, form_email]
        contact_message = "{}, заявка принята:\n{} \nПочта {}".format(
            form_full_name,
            form_message,
            form_email)
        # print(form_email, form_message, form_full_name)
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
                fail_silently=False,
        )
        send_mail(subject,
                  contact_message,
                  from_email,
                  ["smmgroup.info@gmail.com"],
                  auth_password="duplicateemailpass",
                  auth_user="smmgroup.info@gmail.com"
                  )

    context = {
        "form": form,
        "title": title
    }
    return render(request, "contact_form.html", context)


def payment_method(request):
    return render(request, "payment_method.html", {})


def privacy_policy(request):
    return render(request, "privacy_policy.html", {})


def thanks(request):
    return render(request, "thanks.html", {})
