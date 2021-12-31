#!/usr/bin/env python3
"""The main app. Contains all the stacks."""

# Standard library imports
# -

# Third party imports
# -

# Local application/library specific imports
from aws_cdk import core as cdk
from monitor_events_from_multiple_s3_buckets_with_eventbridge.monitor_events_from_multiple_s3_buckets_with_eventbridge_stack import (
    MonitorEventsFromMultipleS3BucketsWithEventbridgeStack,
)

app = cdk.App()
MonitorEventsFromMultipleS3BucketsWithEventbridgeStack(
    scope=app,
    construct_id="MonitorEventsFromMultipleS3BucketsWithEventbridgeStack",
)

app.synth()
