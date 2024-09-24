from .cart import Cart

# it is used availble for the globally to the template when
# Context processors are executed in all the requests that use
# RequestContext
def cart(request):
    return {'cart': Cart(request)}