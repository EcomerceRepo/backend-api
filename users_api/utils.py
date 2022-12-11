import jwt
from .models import User

def getUserByToken(request):
    token = request.COOKIES.get("jwt")
    if not token:
        return None
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    return User.objects.filter(id=payload["id"]).first()
