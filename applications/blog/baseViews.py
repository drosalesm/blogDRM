from django.http import JsonResponse
from rest_framework.views import APIView


class BaseJsonResponseView(APIView):
    def custom_response(self, status,code, message=None, data=None):
        response_data = {"status": status,"code":code, "message": message, "data": data}
        return JsonResponse(response_data)

    def success_response(self, message="Success", data=None):
        return self.custom_response(status="success",code="01", message=message, data=data)

    def error_response(self, message="Error", data=None):
        return self.custom_response(status="error",code="03", message=message, data=data)