from src import cw_client, instanceId
from datetime import timedelta, datetime


def record_http_request(timeStamp):
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