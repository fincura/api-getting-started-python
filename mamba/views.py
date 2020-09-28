from django.shortcuts import render, redirect
from django.http import HttpResponse

from mamba.api_wrapper import (
    dataviews,
    ensure_api_access,
    files,
    workflows,
    EmbeddedWorkflow
)


def app_documentation(request):
    return render(request, "index.html")


# mamba financial views
#@ensure_api_access
def index(request):
    return redirect('list_documents')


# mamba financial views
@ensure_api_access
def list_documents(request):
    return render(request, "doc_queue.html", {
        'document_files': files.list_document_files(limit=10).results
    })


@ensure_api_access
def start_embedded_workflow(request, document_file_uuid):
    flow = workflows.create_embedded_workflow(
        embedded_workflow=EmbeddedWorkflow(
            document_file_uuid=document_file_uuid,
            embed_type="IFRAME"
        )
    )

    return render(request, "embedded_workflow.html", {
        "document_file_uuid": document_file_uuid,
        "iframe_src_url": flow.load_workflow_url
    })

@ensure_api_access
def document_file_data(request, document_file_uuid):
    dataview = dataviews.retrieve_data_view_from_document_file(
        document_file_uuid=document_file_uuid
    )

    return render(request, "document_file_data.html", {
        "document_file_uuid": document_file_uuid,
        "dataview": dataview
    })
