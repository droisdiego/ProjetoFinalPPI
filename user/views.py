from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

# class AdminRequiredMixin:
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             return redirect('login.html')  # Redirecione para uma página de erro
#         return super().dispatch(request, *args, **kwargs)
