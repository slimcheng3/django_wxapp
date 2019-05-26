from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from utils.response import wrap_json_response, ReturnCode
import json
from utils.wx.auth import c2s, already_authorized
from authorization.models import User
from django.views import View
from utils.response import CommonResponseMixin

def test_session(request):
    request.session['message'] = "Test Django Session OK"
    response = wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response,safe=False)

def __authorize_by_code(request):
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    print(post_data)
    code = post_data.get('code').strip()
    app_id = post_data.get("appId").strip()
    nick_name = post_data.get("nickName").strip()

    response = {}
    if not code or not app_id:
        response['message'] = "authoreized failed, need entire authorization data. "
        response['code'] = ReturnCode.BROKEN_AUTHORIZED_DATA
        return JsonResponse(data=response, safe=False)

    data = c2s(app_id,code)
    openid = data.get('openid')
    if not openid:
        response = wrap_json_response(code=ReturnCode.FAILED, message="auth failed")
        return JsonResponse(data=response, safe=False)

    request.session['openid'] = openid
    request.session['is_authorized'] = True

    if not User.objects.filter(openid=openid):
        new_user = User(openid=openid, nickname=nick_name)
        new_user.save()

    response = wrap_json_response(code=ReturnCode.SUCCESS, message="auth success")
    return JsonResponse(data=response, safe=False)
    pass


def authorize(request):
    return __authorize_by_code(request)


class UserView(View, CommonResponseMixin):
    def get(self, request):
        if not already_authorized(request):
            response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED, message="未授权")
            return JsonResponse(data=response, safe=False)
        openid = request.session.get('openid')
        user = User.objects.get(openid=openid)
        data = {}
        data['openid'] = user.openid
        data['focus'] = {}
        data['focus']['city'] = json.loads(user.focus_cities)
        data['focus']['stock'] = json.loads(user.focus_stocks)
        data['focus']['constellation'] = json.loads(user.focus_constellations)
        response = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False)

    def post(self, request):
        if not already_authorized(request):
            response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED, message="未授权")
            return JsonResponse(data=response, safe=False)
        openid = request.session.get('openid')
        user = User.objects.get(openid=openid)

        received_body = request.body.decode('utf-8')
        received_body = eval(received_body)

        cities = received_body.get('city')
        stocks = received_body.get('stock')
        constellations = received_body.get('constellation')

        if cities == None:
            cities = []
        if stocks == None:
            stocks = []
        if constellations == None:
            constellations = []

        user.focus_cities = json.dumps(cities)
        user.focus_constellations = json.dumps(constellations)
        user.focus_stocks = json.dumps(stocks)
        user.save()

        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message="success save")
        return JsonResponse(data=response,safe=False)

def get_status(request):
    if already_authorized(request):
        data = {"is_authorized": 1}
    else:
        data = {"is_authorized": 0}
    response = wrap_json_response(data=data)
    return JsonResponse(data=response, safe=False)


def logout(request):
    request.session.clear()
    response = wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)




