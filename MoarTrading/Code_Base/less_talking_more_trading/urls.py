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
from less_talking_more_trading.views import (options_data_view, order_trigger_order_view, sale_trigger_sale_view, Market_Query_view,
    Market_hours_view, Movers_Query_view, Movers_data_view, Club_chart_view)
from django.contrib.auth.decorators import login_required                                     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view.as_view(), name='home'),
    path('data_test/', data_test_view.as_view(), name='data_test'),
    path('form_example/', form_example_view.as_view(), name='form_example'),
    path('order_trigger_order/',  login_required(order_trigger_order_view.as_view()), name='order_trigger_order'),
    path('club_chart/',  login_required(Club_chart_view.as_view()), name='club_chart'),
    path('sale_trigger_sale/',  login_required(sale_trigger_sale_view.as_view()), name='sale_trigger_sale'),
    path('market_hours_query/',  login_required(Market_Query_view.as_view()), name='market_hours_query'),
    path('movers_query/',  login_required(Movers_Query_view.as_view()), name='movers_query'),
    path('basic_order/', login_required(basic_order_view.as_view()), name='basic_order'),
    path('options_order/', login_required(options_view.as_view()), name='options_order'),
    path('options_query/', login_required(options_query_view.as_view()), name='options_query'),
    path('options_data/', login_required(options_data_view.as_view()), name='options_data'),
    path('market_hours/', login_required(Market_hours_view.as_view()), name='market_hours'),
    path('movers_data/', login_required(Movers_data_view.as_view()), name='movers_data'),
    path('sell_basic/', login_required(basic_sell_view.as_view()), name='sell_basic'),
    path('site_users/', include('django.contrib.auth.urls')),
    path('', include('site_users.urls')),
]
