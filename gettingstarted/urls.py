from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import mamba.views

# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    #path("", mamba.views.app_documentation, name="app_index"),
    path("", mamba.views.index, name="app_index"),
    path("mamba", mamba.views.index, name="mamba_index"),
    path("mamba/docs/list", mamba.views.list_documents, name="list_documents"),
    path("mamba/docs/start-workflow/<document_file_uuid>", mamba.views.start_embedded_workflow, name="start_embedded_workflow"),
    path("mamba/docs/data/<document_file_uuid>", mamba.views.document_file_data, name="document_file_data")
]
