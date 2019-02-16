
from functools import wraps
from sanic.response import redirect


def jwt_required():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            json_token = request.cookies.get('lock-jwt')
            refresh_token = request.cookies.get('lock-rtk')

            if json_token != None and refresh_token != None:
                response = await f(request, *args, **kwargs)
                return response

            return redirect('/')
        return decorated_function
    return decorator