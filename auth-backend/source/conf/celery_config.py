import os

broker_url = os.environ.get("CELERY_BROKER_URL")
result_backend = os.environ.get("CELERY_RESULT_URL")

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Europe/Oslo"
enable_utc = True

imports = ("source.tasks.android",)

task_routes = {"source.tasks.android.snkrs": {"queue": "android", "serializer": "json"}}

result_persistent = True
