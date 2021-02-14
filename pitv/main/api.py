from django.http import JsonResponse

from .models import DeviceCode, generate_code, get_expire_date

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def code(request):
    if request.method == 'GET':
        ip_address = get_client_ip(request)

        try:
            old_device_code = DeviceCode.objects.filter(ip_address=ip_address)

            if old_device_code:
                old_device_code = old_device_code.first()
                old_device_code.code = generate_code()
                old_device_code.expire_date = get_expire_date()
                old_device_code.save()

                code = old_device_code.code
            else:
                device_code = DeviceCode.objects.create(ip_address=ip_address)
                code = device_code.code
            
            return JsonResponse({"message": "Created", "code": code}, status=201)
        except Exception as e:
            print(e)
            return JsonResponse({"message": "Internal Server Error"}, status=500)

    # elif request.method == 'POST':

    else:
        return JsonResponse({"message": "Not Implemented"}, status=501)
 