
from urllib import request
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .models import  Category, Client, Product, Basket
from .forms import EditProductForm, ProductForm
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.decorators import login_required

    
def products(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)

    if category_id:
        products = products.filter(category_id=category_id)

    if query:
        products = products.filter(Q(name_prod__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'product/products.html', {
        'products':products,
        'query': query, 
        'categories':categories,
        'category_id':category_id
        })
    
class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        related_products = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=kwargs['pk'])[0:3]
        context = {
            'product': product,
            'related_products': related_products 
            }
        return render(request, 'product/product_detail.html', context)

class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create_product.html'
    success_url = reverse_lazy('core:mainpage')
    
    def form_valid(self, form):
        # Получите текущего пользователя
        current_user = self.request.user

        # Создайте экземпляр модели Product с commit=False
        product = form.save(commit=False)

        # Измените поле created_by на текущего пользователя
        product.created_by = current_user

        # Сохраните экземпляр Product в базе данных
        product.save()
        self.success_url = reverse('core:mainpage')

        return super().form_valid(form)
    
@login_required
def edit(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('product:detail', pk=item.id)
    else:
        form = EditProductForm(instance=item)

    return render(request, 'product/create_product.html', {
        'form': form,
        'title': 'Edit product',
    })


def add_to_basket(request, product_id):
    """
    Add a product to the user's basket.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to be added.

    Returns:
        HttpResponseRedirect: Redirects the user to the 'basket' page if the user is authenticated,
        otherwise redirects the user to the 'login' page.
    """
    if request.user.is_authenticated:
        Basket.objects.create(buyer_id = request.user.id, product_id = product_id)
        return HttpResponseRedirect(reverse('basket'))
    return HttpResponseRedirect(reverse('login'))


class ListBasket(ListView):
    model = Basket
    template_name = 'main/components/list_basket.html'
    context_object_name = 'basket'
        
    
@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    product.delete()
    
    return redirect('dashboard:index')