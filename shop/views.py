from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    return HttpResponse('<button>Welcome to shop!</button>')


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {'products': products,
                                                      'categories': categories,
                                                      'category': category,
                                                      })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,})


# class RegisterFormView(FormView):
#     form_class = UserCreateForm
#     success_url = "/accounts/login/"
#     template_name = "register.html"
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         return super(RegisterFormView, self).form_invalid(form)
#
#
# def user_autent(request):
#     username = request.POST["username"]
#     email = request.POST["email"]
#     phone = request.POST["phone"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, email=email, phone=phone, password=password)
#     if user is not None:
#         login(request, user)
#     else:
#         pass
#
#
# class LoginFormView(FormView):
#     form_class = AuthenticationForm
#     template_name = "login.html"
#     success_url = "/accounts/"
#
#     def form_valid(self, form):
#         user = form.get_user()
#         login(self.request, user)
#         return super(LoginFormView, self).form_valid(form)
#
#
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect("/accounts/")
#
#
# def logout_view(request):
#     logout(request)
#     # redirect
#     pass
