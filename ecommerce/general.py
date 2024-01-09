from .models import Category,Setting

def global_data(request):
    data = {
        'categoryData' : Category.objects.all(),
        'settingData' : Setting.objects.last,
    }
    return data