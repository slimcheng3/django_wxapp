#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import os
from test_weather import settings
from django.http import HttpResponse, JsonResponse, FileResponse, Http404
import utils.response
from django.views import View
import hashlib

def image(request):
    if request.method == "GET":
        md5 = request.GET.get("md5")
        imgfile = os.path.join(settings.RESOURCE_DIR, 'images\%s.jpg' % (md5))
        if os.path.exists(imgfile):
            # data = open(imgfile, 'rb').read()
            # return HttpResponse(data, content_type='image/jpg')
            return FileResponse(open(imgfile,'rb'), content_type='image/jpg')
        else:
            return Http404()
    elif request.method == "POST":
        pass


class ImageViewList(View,utils.response.CommonResponseMixin):
    def get(self, request):
        image_files = os.listdir(settings.IMAGES_DIR)
        resposne_data = []
        for item in image_files:
            resposne_data.append(
                {
                "name": item,
                "md5": item[:-4]
                }
            )
        resposne_data = self.wrap_json_response(data=resposne_data)
        return JsonResponse(data=resposne_data, safe=False)


class ImageView(View,utils.response.CommonResponseMixin):
    def get(self, request):
        md5 = request.GET.get("md5")
        imgfile = os.path.join(settings.RESOURCE_DIR, 'images\%s.jpg' % (md5))
        if os.path.exists(imgfile):
            # data = open(imgfile, 'rb').read()
            # return HttpResponse(data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            return Http404()

    def post(self, request):
        files = request.FILES
        response = []
        for key,value in files.items():  # key是图片上传空间name值，value是文件句柄对象
            content = value.read() #二进制
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            response.append({
                "name": key,
                "md5": md5
            })
        message = "put method success"
        response = self.wrap_json_response(data=response, code=utils.response.ReturnCode.SUCCESS,message=message)
        # print(response)
        return JsonResponse(data=response, safe=False)

    def put(self, request):
        message = "put method success"
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        md5 = request.GET.get("md5")
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if os.path.exists(imgfile):
            os.remove(imgfile)
            message = "delete success"
        else:
            message = "file(%s) not found" % imgfile
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

def image_text(request):
    if request.method == "GET":
        md5 = request.GET.get("md5")
        imgfile = os.path.join(settings.RESOURCE_DIR, 'images\%s.jpg' % (md5))
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(code=utils.response.ReturnCode.WRONG_PARMAS)
        else:
            response_data = {}
            response_data["name"] = md5 + '.jpg'
            response_data['url'] = '/service/image?md5=%s.jpg' % (md5)
            response = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)







if __name__ == "__main__":
    image()
