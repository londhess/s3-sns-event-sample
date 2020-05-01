from aws_cdk import (
    aws_s3 as s3,
    aws_s3_notifications as notifications,
    aws_sns as sns,
    aws_lambda as _lambda,
    aws_sqs as sqs,
    aws_sns_subscriptions as aws_sns_subscriptions,
    core
    )


class S3SnsEventSampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define S3 bucket
        my_bucket = s3.Bucket(self,"ssl-s3-sns-event-raw")

        #Add Filters if required
        filter1=s3.NotificationKeyFilter(prefix="home/")

        #sns Topic
        my_sns = sns.Topic(self,id="my-sns-topic",display_name="my-sns-topic")

        #Create the s3 notification objects which points to Lambda
        notification = notifications.SnsDestination(my_sns)

        #link s3 and sns
        my_bucket.add_event_notification(s3.EventType.OBJECT_CREATED,notification,filter1)

        #create sqs queue
        my_sqs = sqs.Queue(self,id="my-queue")

        #create sqs / sns subcription
        subscription = aws_sns_subscriptions.SqsSubscription(my_sqs)

        #add subscription to sns.
        my_sns.add_subscription(subscription)

        #create lambda function
        my_lambda = _lambda.Function(self,"HelloHandler",
                            runtime=_lambda.Runtime.PYTHON_3_7,
                            handler="hello.handler",
                            code=_lambda.Code.asset('lambda'))
        
        #create sns/lambda subscription
        subscription = aws_sns_subscriptions.LambdaSubscription(my_lambda)

        #add lambda subscription to sns
        my_sns.add_subscription(subscription)





          