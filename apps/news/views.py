from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

# from django.http import HttpResponse
# from docxtpl import DocxTemplate
# from docx import Document
# from io import BytesIO


from apps.home.models import Category

from .models import Yangiliklar, NewsCartegory



def news_view(request, cat_id=None):
    
    context = {
        "cat_news": NewsCartegory.objects.filter(parent=None),
        'categories': Category.objects.filter(parent=None)[:6],
        "catw": NewsCartegory.objects.get(pk=cat_id) if cat_id else NewsCartegory.objects.all(),
        "yangiliklar": Yangiliklar.objects.filter(category__id=cat_id).order_by("-id") if cat_id else Yangiliklar.objects.all().order_by("-id"),
    }

    return render(request, 'news/news.html', context)


def new_detail(request, cat_id):

    yangilik = get_object_or_404(Yangiliklar, id=cat_id)

    url = yangilik.post_url
    stripped_post = url.split('/')[-1]


    context = {
        'categories': Category.objects.filter(parent=None)[:6],
        "cat_news": NewsCartegory.objects.filter(parent=None),
        "yangilik": yangilik,
        "tgurl": stripped_post,
    }

    return render(request, 'news/news_detail.html', context)



# def generate_word_document(request):
#     # Fetch all Yangiliklar objects
#     yangiliklar_objects = Yangiliklar.objects.all()

#     # Create a new Word document
#     document = Document()
    
#     # Add a table with headers
#     table = document.add_table(rows=1, cols=4)  # Adjust the number of columns as needed
#     hdr_cells = table.rows[0].cells
#     hdr_cells[0].text = 'Title'
#     hdr_cells[1].text = 'Description'
#     hdr_cells[2].text = 'Post URL'
#     hdr_cells[3].text = 'Category'
    
#     # Add data rows to the table
#     for yangiliklar in yangiliklar_objects:
#         row_cells = table.add_row().cells
#         row_cells[0].text = yangiliklar.title
#         row_cells[1].text = yangiliklar.desc
#         row_cells[2].text = yangiliklar.post_url
#         row_cells[3].text = str(yangiliklar.category)

#     # Save the document to a BytesIO object
#     doc_stream = BytesIO()
#     document.save(doc_stream)

#     # Create a response with the appropriate headers for a Word document
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
#     )
#     response['Content-Disposition'] = 'attachment; filename=Yangiliklar.docx'

#     # Seek to the beginning of the BytesIO object and write its contents to the response
#     doc_stream.seek(0)
#     response.write(doc_stream.read())

#     return response


