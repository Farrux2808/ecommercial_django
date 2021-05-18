
from ..models import Measurement

class MeasurementView:
    # def __init__(self, cayegory_type):
    #     self.Measurement_type = cayegory_type
    
    def add(data):
        try:
            Measurement(type_name = data['type_name']).save()
            return {
                "status": "success"
            }
        except Measurement.DoesNotExist:
            return {
                "status": "error"
            }

    def get_all():
        data = Measurement.objects.all().values()
        return data

    def get(id):
        try:
            data = Measurement.objects.get(id=id)
            return {
                "status": "success",
                "id": data.id,
                "type": data.type_name
            }
        except Measurement.DoesNotExist:
            return {
                "status": "error",
                "message": "id not found"
            }
    
    def delete(id):
        try:
            data = Measurement.objects.get(id=id)
            data.delete()
            return {
                "status": "successfuly deleted",
            }
        except Measurement.DoesNotExist:
            return {
                "status": "error",
            }
    
    def update(id, new_data):
        try:
            data = Measurement.objects.get(id=id)
            data.type_name = new_data.get('type_name')
            data.save()
            return {
                "status": "successfuly update",
            }
        except Measurement.DoesNotExist:
            return {
                "status": "error",
            }