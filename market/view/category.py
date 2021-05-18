
from ..models import Category

class CategoryView:
    # def __init__(self, cayegory_type):
    #     self.category_type = cayegory_type
    
    def add(data):
        try:
            Category(type_name = data['type_name']).save()
            return {
                "status": "success"
            }
        except Category.DoesNotExist:
            return {
                "status": "error"
            }

    def get_all():
        data = Category.objects.all().values()
        return data

    def get(id):
        try:
            data = Category.objects.get(id=id)
            return {
                "status": "success",
                "id": data.id,
                "type": data.type_name
            }
        except Category.DoesNotExist:
            return {
                "status": "error",
                "message": "id not found"
            }
    
    def delete(id):
        try:
            data = Category.objects.get(id=id)
            data.delete()
            return {
                "status": "successfuly deleted",
            }
        except Category.DoesNotExist:
            return {
                "status": "error",
            }
    
    def update(id, new_data):
        try:
            data = Category.objects.get(id=id)
            data.type_name = new_data.get('type_name')
            data.save()
            return {
                "status": "successfuly update",
            }
        except Category.DoesNotExist:
            return {
                "status": "error",
            }