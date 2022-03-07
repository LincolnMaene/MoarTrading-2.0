"""less_talking_more_trading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from less_talking_more_trading.views import home_view
from less_talking_more_trading.views import data_test_view
from less_talking_more_trading.views import form_example_view, basic_order_view, basic_sell_view, options_view, options_query_view
from less_talking_more_trading.views import options_data_view                                     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view.as_view(), name='home'),
    path('data_test/', data_test_view.as_view(), name='data_test'),
    path('form_example/', form_example_view.as_view(), name='form_example'),
    path('basic_order/', basic_order_view.as_view(), name='basic_order'),
    path('options_order/', options_view.as_view(), name='options_order'),
    path('options_query/', options_query_view.as_view(), name='options_query'),
    path('options_data/', options_data_view.as_view(), name='options_data'),
    path('sell_basic/', basic_sell_view.as_view(), name='sell_basic'),
    path('site_users/', include('django.contrib.auth.urls')),
    path('', include('site_users.urls')),
]
