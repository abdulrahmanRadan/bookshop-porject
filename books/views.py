from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
import matplotlib.pyplot as plt
import networkx as nx
import io
import base64
from .forms import *
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'categoryform':CategoryForm(),
        'form':BookForm(),
        'books':Book.objects.all(),
        'category':Category.objects.all(),
        'allbooks': Book.objects.filter(active=True).count(),
        'bookssold': Book.objects.filter(status='sold').count(),
        'booksrental': Book.objects.filter(status='rental').count(),
        'booksavailable': Book.objects.filter(status='availble').count(),
    }
    return render(request, 'pages/index.html', context)


def show(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
            



    context = {
        'categoryform':CategoryForm(),
        'books':search,
        'category':Category.objects.all(),
    }
    return render(request,'pages/books.html',context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form':book_save,
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')
def deletecat(request, id):

    cat_delete = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        cat_delete.delete()
        return redirect('/')
    return render(request, 'pages/deletecat.html')

def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_city')
    else:
        form = CityForm()
    return render(request, 'graph_app/add_city.html', {'form': form})

def add_road(request):
    if request.method == 'POST':
        form = RoadForm(request.POST)
        if form.is_valid():
            city1 = form.cleaned_data['city1']
            city2 = form.cleaned_data['city2']
            distance = form.cleaned_data['distance']
            Road.objects.create(city1=city1, city2=city2, distance=distance)
            return redirect('add_road')
    else:
        form = RoadForm()

    return render(request, 'graph_app/add_road.html', {'form': form})

def graph_view(request):
    # إنشاء الرسم البياني للطرق
    G = nx.Graph()

    # إضافة المدن والأطراف (الطرق) من قاعدة البيانات
    roads = Road.objects.all()
    cities = City.objects.all()

    for road in roads:
        G.add_edge(road.city1.name, road.city2.name, weight=road.distance)
    
    plt.figure(figsize=(12, 8))  # ضبط حجم الشكل
    path = None
    path_length = None
    longest_path = None
    longest_path_length = None

    if request.method == 'POST':
        form = PathForm(request.POST)
        if form.is_valid():
            start_city = form.cleaned_data['start_city'].name
            end_city = form.cleaned_data['end_city'].name
            path = nx.shortest_path(G, source=start_city, target=end_city, weight='weight')
            path_length = nx.shortest_path_length(G, source=start_city, target=end_city, weight='weight')

            # حساب أطول مسار
            all_paths = list(nx.all_simple_paths(G, source=start_city, target=end_city))
            longest_path = max(all_paths, key=lambda p: sum(G[u][v]['weight'] for u, v in zip(p[:-1], p[1:])))
            longest_path_length = sum(G[u][v]['weight'] for u, v in zip(longest_path[:-1], longest_path[1:]))
    else:
        form = PathForm()

    # عرض الرسم البياني
    pos = nx.spring_layout(G,k=1.5)  # تحديد تخطيط العقد
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue")  # رسم الرسم البياني
    labels = nx.get_edge_attributes(G, 'weight')  # الوزن كتسميات للحواف
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # رسم الوزن على الحواف

    # رسم أقصر مسار باللون الأخضر
    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=2)

    # رسم أطول مسار باللون الأحمر
    if longest_path:
        longest_path_edges = list(zip(longest_path[:-1], longest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=longest_path_edges, edge_color='red', width=2)

    # حفظ الرسم البياني كصورة
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')

    context = {
        'graph_image': image_base64,
        'form': form,
        'path': path,
        'path_length': path_length,
        'longest_path': longest_path,
        'longest_path_length': longest_path_length,
    }

    return render(request, 'graph_app/graph.html', context)

def load_cities(request):
    city1_id = request.GET.get('city1_id')
    cities = City.objects.exclude(id=city1_id)
    return JsonResponse(render_to_string('graph_app/city_dropdown_list_options.html', {'cities': cities}), safe=False)