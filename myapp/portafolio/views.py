from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class PortafolioView(LoginRequiredMixin, View):
    template_name = 'portafolio.html'

    def get(self, request):
        return render(request, self.template_name)

    # model = Book
    # template_name = 'list_libros.html'
    # # Added query to limit amount of results
    # queryset = Book.objects.filter()[:10]

    # template = "list_libros.html"

    # def get(self, request):
    #     object_list = Book.objects.all()

    #     return render(request, self.template, {"object_list": object_list})

    # def post(self, request):
    #     # return HttpResponse("Holaaaaaaaaa")
    #     url_api = "https://gist.githubusercontent.com/silabuz/dc872e35e237abf1637f24f7a1d9a650/raw/e543e03b72706ddd6fa162ba2155d6a40423adec/books_to_clean.json"
    #     # url_api = "https://silabuzinc.github.io/books/books.json"

    #     response = urllib.request.urlopen(url_api)
    #     books = json.loads(response.read())

    #     for book in books:
    #         try:
    #             del book['bookID']

    #             book['average_rating'] = float(book['average_rating'])
    #             book['num_pages'] = int(book['num_pages'])

    #             format = book['publication_date'].split('/')
    #             if len(format) == 3:
    #                 book['publication_date'] = datetime.date(
    #                     int(format[2]), int(format[0]), int(format[1]))
    #             else:
    #                 book['publication_date'] = datetime.date(2000, 1, 1)

    #             Book.objects.create(**book)
    #         except:
    #             continue

    #     messages.success(request, 'Felicidades, se cargaron los datos a DB.')
    #     return redirect('/library/')


class PortafolioAdd(View):
    template_name = 'portafolio_add.html'

    def get(self, request):
        return render(request, self.template_name)
