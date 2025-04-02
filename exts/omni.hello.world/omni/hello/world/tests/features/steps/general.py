@given(u'a running service')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a running service')


@when(u'we GET the /stats Endpoint')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we GET the /stats Endpoint')


@then(u'we get a response of type application/JSON')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we get a response of type application/JSON')


@then(u'we get a JSON document in the body of the response')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we get a JSON document in the body of the response')


@then(u'the JSON document is valid')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the JSON document is valid')


@then(u'the JSON document contains stats')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the JSON document contains stats')


@then(u'the status code is 200')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the status code is 200')