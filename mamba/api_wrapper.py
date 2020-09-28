import os
import sys
import logging
from functools import wraps

from fincura import (
	ApiClient,
	ApiKey,
	ApiKeyApi,
	Configuration,
	DataViewsApi,
	EmbeddedWorkflow,
	EmbeddedWorkflowsApi,
	FilesApi,
)
from fincura.rest import ApiException

TENANT_ID =  os.environ.get('FINCURA_TENANT_ID')
REFRESH_TOKEN = str(os.environ['FINCURA_API_REFRESH_TOKEN'])

FINCURA_ENV = os.environ['FINCURA_ENV']

if FINCURA_ENV == 'local':
	host = "https://api-local.fincura.com:8000"
elif FINCURA_ENV == 'production':
	host = "https://api.fincura.com"
else:
	host = "https://api-%s.fincura.com" % FINCURA_ENV

# Configure API key authorization: ApiKeyAuth
configuration = Configuration(host=host)
configuration.verify_ssl = FINCURA_ENV != 'local' # for debug only
configuration.client_side_validation = False
configuration.api_key['API_Key'] = None
configuration.api_key_prefix['API_Key'] = 'Bearer'

# create an instance of the API class
api_key_client = ApiKeyApi(ApiClient(configuration))
files = FilesApi(ApiClient(configuration))
workflows = EmbeddedWorkflowsApi(ApiClient(configuration))
dataviews = DataViewsApi(ApiClient(configuration))


def ensure_api_access(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		# TODO - check current access, dont refresh if still valid
	    refresh_access_token()
	    return function(request, *args, **kwargs)
	return wrap

def refresh_access_token():
	refresh_response = api_key_client.refresh_api_key(
		api_key=ApiKey(refresh_token=REFRESH_TOKEN, tenant_id=TENANT_ID)
	)
	configuration.access_token = refresh_response.access_token