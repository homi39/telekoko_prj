from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm

class IndexView(View):
    def get(self,request):
          return render(request, "telekoko/index.html")


class FeelingCreateView(View):
    #初期表示
    def get(self, request):
        form = UserForm()
        return render(request,"telekoko/feeling_form.html",{"form": form})
    #保存処理（保存後はトップページにリダイレクト、失敗すれば遷移しない）
    def post(self,request):
        form  = UserForm(request.post)
        if form.is_valid():
            form.save()
            return redirect("telekoko:index")
        return render(request, "telekoko/feeling_form.html",{"form": form})

index = IndexView.as_view()
feeling_create = FeelingCreateView.as_view()