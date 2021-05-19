from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

# Create your views here.


class LoginView(View):

    def post(self,request):

        # 取到表单中提交上来的参数
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not all([username, password]):
            print('参数错误')
        else:
            print(username, password)
            if username == 'laowang' and password == '1234':
                # 状态保持，设置用户名到cookie中表示登录成功
                response = redirect(reverse('transfer'))
                response.set_cookie('username', username)
                return response
            else:
                print('密码错误')
        return render(request,'login.html')
    def get(self,request):
        return render(request,'login.html')

class TransferView(View):

    def post(self,request):
        # 从cookie中取到用户名
        username = request.COOKIES.get('username', None)
        # 如果没有取到，代表没有登录
        if not username:
            return redirect(reverse('index'))

        # 转账的业务逻辑有问题,我们需要添加再次验证
        # user_sms_code=request.POST.get('sms_code')
        # server_sms_code = redis.get('sms_code')

        # 黑客是获取不到随机码的
        # 黑客是获取不到短信验证码的

        # user_sms_code=request.POST.get('smscode')
        # server_sms_code='1234'
        # if user_sms_code != server_sms_code:
        #     return HttpResponse('哥们你找削呢,敢转我的帐,你不知道验证码吧')

        user_sms_code=request.POST.get('csrftoken')
        server_sms_code=request.COOKIES.get('csrf_token')

        if user_sms_code != server_sms_code:
            return HttpResponse('哥们你找削呢,敢转我的帐,你不知道验证码吧')

        to_account = request.POST.get("to_account")
        money = request.POST.get("money")

        print('假装执行转操作，将当前登录用户的钱转账到指定账户')
        return HttpResponse('转账 %s 元到 %s 成功' % (money, to_account))

    def get(self, request):
        from django.middleware.csrf import get_token
        # 生成一个随机码
        csrf_token=get_token(request)

        response = render(request, 'transfer.html',context={'csrf_token':csrf_token})

        # csrf_token 放在 cookie中
        # 是因为同源策略的原因
        # 黑客(钓鱼)网站是用于获取不到我们当前网站的cookie信息的
        response.set_cookie('csrf_token',csrf_token)

        return response
