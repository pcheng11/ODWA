from src import s3_client, instanceId



def record_http_request(timeStamp):
    response = s3_client.put_metric_data(
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
    print(response)
