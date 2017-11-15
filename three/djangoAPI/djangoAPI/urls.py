from django.conf.urls import url, include
from django.contrib import admin
# 新增以下兩行 -------------------------------
from graphene_django.views import GraphQLView
from graphAPI.schema import schema
# -------------------------------------------

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
# 新增以下 -------------------------------
    url(r'^graph/', GraphQLView.as_view(graphiql=True, schema=schema)),
# ---------------------------------------
    url(r'^src/', TemplateView.as_view(template_name="index.html"))
] 
