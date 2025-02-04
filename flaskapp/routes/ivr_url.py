#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
This file is a part of heartvoices.org project.
The software embedded in or related to heartvoices.org
is provided under a some-rights-reserved license. This means
that Users are granted broad rights, including but not limited
to the rights to use, execute, copy or distribute the software,
to the extent determined by such license. The terms of such
license shall always prevail upon conflicting, divergent or
inconsistent provisions of these Terms. In particular, heartvoices.org
and/or the software thereto related are provided under a GNU GPLv3 license,
allowing Users to access and use the software’s source code.
Terms and conditions: https://www.goandtodo.org/terms-and-conditions
Created Date: Sunday September 26th 2021
Author: GO and to DO Inc
E-mail: heartvoices.org@gmail.com
-----
Last Modified: Tuesday, October 26th 2021, 10:22:36 am
Modified By: GO and to DO Inc
-----
Copyright (c) 2021
"""


from flaskapp.routes.bluprints import TwilioBluprint, MobileAPIBluprint
from flaskapp.tools.utils import ensure_twilio_voice_response
from flaskapp.views.ivrflow import (
    get_username,
    get_client_type,
    save_client_type,
    call_to_friend,
    find_friend_timezone,
    end_call,
    call_to_operator,
    save_blood_pressure,
    save_feedback_service,
    save_feedback,
    search_via_google,
    get_next_reminder,
    voice_joined,
    voice,
    after_call,
    get_term_cond,
    get_privacy,
    get_profile,
    new_user,
    unsubscribe,
    get_month_data
)


IVRFlowBlueprint = TwilioBluprint('IVRFlowBlueprint', __name__)
MobileBluprint = MobileAPIBluprint('MobileAPIBluprint', __name__)


IVRFlowBlueprint.after_request(ensure_twilio_voice_response)


# Bulk registration of views is essintialy
# possbile because in our case the url-enpoints have
# the same names as function names, e.g.
# voice_joined -> /voice_joined
# voice        -> /voice
# ... etc
# However, this default behavior could be overriden
# see the usege of MobileBlueprint.bulk_register.
# See details in `bulk_register` docstring.
IVRFlowBlueprint.bulk_register(
        voice_joined,
        voice,
        after_call,
        get_username,
        save_client_type,
        find_friend_timezone,
        end_call,
        save_blood_pressure,
        save_feedback_service,
        get_month_data
)


MobileBluprint.bulk_register(
        get_username,
        get_client_type,
        call_to_friend,
        call_to_operator,
        save_feedback,
        search_via_google,
        get_next_reminder,
        new_user,
        unsubscribe,
        get_term_cond,
        get_privacy,
        get_profile,
        get_month_data,

        # Some view names aren't the same as url-endpoint names,
        # so we provide additional information in `route_urls`,
        # i.e. `get_username` view function
        # will be associated to `/username` enpoint,
        # default behavior of `bulk_register` is overriden by
        # mapping variable `route_urls`.
        route_urls={
            'get_username': 'username',
            'get_client_type': 'check_client_type',
            'search_via_google': 'search',
            'get_term_cond': 'term_cond',
            'get_privacy': 'privacy',
            'get_profile': 'authenticate/get_profile'
        }
)