# File: `features/steps/api_steps.py`
import json
from behave import given, when, then
from api.base_api_client import BaseAPIClient

def _coerce_value(val: str):
    """Try to convert table values to int/float/bool/json, fallback to string."""
    if val is None:
        return None
    v = val.strip()
    if v == "":
        return ""
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    try:
        return int(v)
    except Exception:
        pass
    try:
        return float(v)
    except Exception:
        pass
    try:
        return json.loads(v)
    except Exception:
        return v

@given('base api url is "{base_url}"')
def step_set_base_url(context, base_url):
    context.client = BaseAPIClient(base_url)
    context.auth_headers = {}

@given('I have a valid authentication token')
def step_have_token(context):
    token = getattr(context, "auth_token", None)
    # fallback to behave userdata if provided via command line/config
    if not token and hasattr(context, "config") and context.config.userdata:
        token = context.config.userdata.get("auth_token")
    context.auth_headers = {"Authorization": f"Bearer {token}"} if token else {}

@given('I do not have an authentication token')
def step_no_token(context):
    context.auth_headers = {}

@given('I have user data with:')
def step_user_data_table(context):
    data = {}
    for row in context.table:
        # table expected as: | key | value |
        key = row[0]
        val = row[1]
        data[key] = _coerce_value(val)
    context.request_body = data

@when('I send a GET request to "{path}"')
def step_send_get(context, path):
    resp = context.client.get(path, headers=context.auth_headers)
    context.response = resp
    try:
        context.response_json = resp.json()
    except Exception:
        context.response_json = None

@when('I send a POST request to "{path}" with body')
def step_post_with_body(context, path):
    body_text = (context.text or "").strip()
    if body_text:
        json_body = json.loads(body_text)
    else:
        json_body = getattr(context, "request_body", None)
        if json_body is None:
            raise AssertionError("POST body missing: provide JSON docstring or a data table with 'I have user data with:'")
    resp = context.client.post(path, json=json_body, headers=context.auth_headers)
    context.response = resp
    try:
        context.response_json = resp.json()
    except Exception:
        context.response_json = None

@when('I send a PUT request to "{path}" with data:')
def step_put_with_data(context, path):
    data = {}
    for row in context.table:
        data[row[0]] = _coerce_value(row[1])
    resp = context.client.put(path, json=data, headers=context.auth_headers)
    context.response = resp
    try:
        context.response_json = resp.json()
    except Exception:
        context.response_json = None

@when('I send a DELETE request to "{path}"')
def step_delete(context, path):
    resp = context.client.delete(path, headers=context.auth_headers)
    context.response = resp
    context.response_json = None
    try:
        context.response_json = resp.json()
    except Exception:
        context.response_json = None

@then('the response status code should be {code:d}')
def step_assert_status(context, code):
    actual = context.response.status_code
    assert actual == code, f"Expected status {code}, got {actual}. Body: {context.response.text}"
@then('the response should contain field "{key}"')
def step_response_has_field(context, key):
    data = context.response_json
    assert data is not None, "Response is not JSON"
    # If 'data' key exists and is a list, check inside it
    if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
        assert any(isinstance(item, dict) and key in item for item in data["data"]), f"Field {key} not found in any item in 'data' array"
    elif isinstance(data, list):
        assert any(isinstance(item, dict) and key in item for item in data), f"Field {key} not found in any item"
    elif isinstance(data, dict):
        assert key in data, f"Field {key} not found in response"
    else:
        assert False, "Response JSON is neither object nor array"

@then('the response should have field "{key}" with value "{value}"')
def step_response_field_value(context, key, value):
    data = context.response_json
    assert data is not None, "Response is not JSON"
    target = None
    if isinstance(data, list) and data:
        # check first match
        for item in data:
            if isinstance(item, dict) and key in item:
                target = item.get(key)
                break
    elif isinstance(data, dict):
        target = data.get(key)
    assert str(target) == value, f"Expected {value} for {key}, got {target}"

@then('capture response field "{key}" as "{var_name}"')
def step_capture_field(context, key, var_name):
    data = context.response_json
    captured = None
    if isinstance(data, dict):
        captured = data.get(key)
    elif isinstance(data, list) and data:
        for item in data:
            if isinstance(item, dict) and key in item:
                captured = item.get(key)
                break
    context.saved = getattr(context, "saved", {})
    context.saved[var_name] = captured

@then('the response should be an array')
def step_response_is_array(context):
    data = context.response_json
    # If 'data' key exists and is a list, treat that as the array
    if isinstance(data, dict) and "data" in data:
        arr = data["data"]
    else:
        arr = data
    assert isinstance(arr, list), "Expected response to be an array (list), got: {}".format(type(arr))
    context._array_under_test = arr

@then('the response array should not be empty')
def step_response_array_not_empty(context):
    # Use array from previous step if available
    arr = getattr(context, '_array_under_test', None)
    if arr is None:
        data = context.response_json
        if isinstance(data, dict) and "data" in data:
            arr = data["data"]
        else:
            arr = data
    assert isinstance(arr, list) and len(arr) > 0, "Expected non-empty array"
