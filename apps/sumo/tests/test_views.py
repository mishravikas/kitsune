from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect

import mock
from nose.tools import eq_
from pyquery import PyQuery as pq
from test_utils import RequestFactory

from sumo.middleware import LocaleURLMiddleware
from sumo.tests import TestCase
from sumo.urlresolvers import reverse
from sumo.views import deprecated_redirect, redirect_to


class RedirectTests(TestCase):
    rf = RequestFactory()

    def test_redirect_to(self):
        resp = redirect_to(self.rf.get('/'), url='home', permanent=False)
        assert isinstance(resp, HttpResponseRedirect)
        eq_(reverse('home'), resp['location'])

    def test_redirect_permanent(self):
        resp = redirect_to(self.rf.get('/'), url='home')
        assert isinstance(resp, HttpResponsePermanentRedirect)
        eq_(reverse('home'), resp['location'])

    def test_redirect_kwargs(self):
        resp = redirect_to(self.rf.get('/'), url='users.confirm_email',
                           activation_key='1234')
        eq_(reverse('users.confirm_email', args=['1234']),
            resp['location'])

    @mock.patch.object(Site.objects, 'get_current')
    def test_deprecated_redirect(self, get_current):
        get_current.return_value.domain = 'su.mo.com'
        req = self.rf.get('/en-US/')
        # Since we're rendering a template we need this to run.
        LocaleURLMiddleware().process_request(req)
        resp = deprecated_redirect(req, url='home')
        eq_(200, resp.status_code)
        doc = pq(resp.content)
        assert doc('meta[http-equiv=refresh]')
        refresh = doc('meta[http-equiv=refresh]')
        timeout, url = refresh.attr('content').split(';url=')
        eq_('10', timeout)
        eq_(reverse('home'), url)


class RobotsTestCase(TestCase):
    # Use the hard-coded URL because it's well-known.
    old_setting = settings.ENGAGE_ROBOTS

    def tearDown(self):
        settings.ENGAGE_ROBOTS = self.old_setting

    def test_disengaged(self):
        settings.ENGAGE_ROBOTS = False
        response = self.client.get('/robots.txt')
        eq_('User-Agent: *\nDisallow: /', response.content)
        eq_('text/plain', response['content-type'])

    def test_engaged(self):
        settings.ENGAGE_ROBOTS = True
        response = self.client.get('/robots.txt')
        eq_('text/plain', response['content-type'])
        assert len(response.content) > len('User-agent: *\nDisallow: /')
