from src import cw_client, instanceId
from celery.task import periodic_task
from datetime import timedelta, datetime


def record_http_request(timeStamp, route):
    response = cw_client.put_metric_data(
        Namespace='AWS/EC2',
        MetricData=[
            {
                'MetricName': 'httpRequestRate',
                'Dimensions': [
                    {
                        'Name': 'InstanceId',
                        'Value': instanceId
                    },
                ],
                'Timestamp': timeStamp,
                'Value': 1,
                'StorageResolution': 60,
                'Unit': 'Count'
            },
        ]
    )


@periodic_task(run_every=timedelta(seconds=60))
def periodically_record_http_request():
    response = cw_client.put_metric_data(
        Namespace='AWS/EC2',
        MetricData=[
            {
                'MetricName': 'httpRequestRate',
                'Dimensions': [
                    {
                        'Name': 'InstanceId',
                        'Value': instanceId
                    },
                ],
                'Timestamp': datetime.now(),
                'Value': 0,
                'StorageResolution': 60,
                'Unit': 'Count'
            },
        ]
    )
