from django.conf.urls import patterns, include, url

urlpatterns = patterns('frageAntwo.views',
                       url( r'^(?P<pk>\d+)$','home', name='frageAntwo_home'),
                       url( r'^OhneAkz$','frageOhneAkzAntwo', name='frageAntwo_frageOhneAkzAntwo'))

