from django.contrib.auth.models import User
from django.http import JsonResponse
import json

def queryAll(request):
    qs = User.objects.all()
    retJson = []
    for user in qs:
        retJson.append({
            'username': user.username,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'last_login': user.last_login,
            'date_joined': user.date_joined,
        })
    ret = {
      'ret': 0,
      'data': retJson,
    }
    return JsonResponse(ret, safe=False)


def querySelf(request):
    qs = User.objects.all()
    qs = qs.filter(username=request.session.get('username'))
    retJson = []
    for user in qs:
        retJson.append({
            'username': user.username,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'last_login': user.last_login,
            'date_joined': user.date_joined,
        })
    ret = {
      'ret': 0,
      'data': retJson,
    }
    return JsonResponse(ret, safe=False)


superFunctions = {
    'queryAll': queryAll
}

funcTable = {
    'queryAll': queryAll,
    'querySelf': querySelf,
}


def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    action = request.params['action']
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/login'},
            status=302)
    if action in superFunctions and request.session['usertype'] != 'administrator':
        return JsonResponse({
            'ret': 302,
            'msg': '权限不足',
            'redirect': '/'},
            status=302)
    if action in funcTable:
        handler = funcTable[action]
        return handler(request)

    return JsonResponse({
        'ret': 404,
        'msg': '无此api',
        'redirect': '/'},
        status=404)
