#!/usr/bin/env python3
"""The main app. Contains all the stacks."""


# Third party imports
import jsii

# Local application/library specific imports
from aws_cdk import (
    core as cdk,
    aws_s3 as s3,
)
from monitor_events_from_multiple_s3_buckets_with_eventbridge.monitor_events_from_multiple_s3_buckets_with_eventbridge_stack import (
    MonitorEventsFromMultipleS3BucketsWithEventbridgeStack,
)


@jsii.implements(cdk.IAspect)
class EventBridgeNotificationAdder:  # pylint: disable=too-few-public-methods
    """CDK Aspect to set EventBridgeEnabled on every CfnBucket."""

    def visit(self, node):
        """Visit every node, check if it is a Bucket, update if it is."""
        if isinstance(node, s3.CfnBucket):
            node.add_property_override(
                "NotificationConfiguration.EventBridgeConfiguration",
                {"EventBridgeEnabled": True},
            )


app = cdk.App()
MonitorEventsFromMultipleS3BucketsWithEventbridgeStack(
    scope=app,
    construct_id="MonitorEventsFromMultipleS3BucketsWithEventbridgeStack",
)
cdk.Aspects.of(app).add(EventBridgeNotificationAdder())

app.synth()
