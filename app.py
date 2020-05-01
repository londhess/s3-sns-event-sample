#!/usr/bin/env python3

from aws_cdk import core

from s3_sns_event_sample.s3_sns_event_sample_stack import S3SnsEventSampleStack


app = core.App()
S3SnsEventSampleStack(app, "s3-sns-event-sample",  env={'region': 'ap-south-1'})

app.synth()
