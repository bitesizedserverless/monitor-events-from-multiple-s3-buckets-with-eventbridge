"""Module for the main MonitorEventsFromMultipleS3BucketsWithEventbridge Stack."""

# Standard library imports
# -

# Third party imports
from aws_cdk import (
    core as cdk,
    aws_s3 as s3,
    aws_events as events,
    aws_events_targets as targets,
    aws_lambda as lambda_,
)

# Local application/library specific imports
from monitor_events_from_multiple_s3_buckets_with_eventbridge.lambda_function import (
    LambdaFunction,
)


class MonitorEventsFromMultipleS3BucketsWithEventbridgeStack(cdk.Stack):
    """The MonitorEventsFromMultipleS3BucketsWithEventbridge Stack."""

    def __init__(
        self,
        scope: cdk.Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        """Construct a new MonitorEventsFromMultipleS3BucketsWithEventbridgeStack."""
        super().__init__(scope, construct_id, **kwargs)

        # Create a few S3 buckets
        s3.CfnBucket(
            scope=self,
            id="Bucket1",
            notification_configuration=s3.CfnBucket.NotificationConfigurationProperty(
                event_bridge_configuration=s3.CfnBucket.EventBridgeConfigurationProperty(
                    event_bridge_enabled=True
                )
            ),
        )
        s3.CfnBucket(
            scope=self,
            id="Bucket2",
            notification_configuration=s3.CfnBucket.NotificationConfigurationProperty(
                # notification_configuration set through Aspect in app.py
            ),
        )
        s3.CfnBucket(
            scope=self,
            id="Bucket3",
            # notification_configuration set through Aspect in app.py
        )

        # Create an EventBridge Rule to match new objects in any bucket
        put_object_processor = LambdaFunction(
            scope=self,
            construct_id="PutObjectProcessor",
            code=lambda_.Code.from_asset("lambda_functions/s3_event_processor"),
        )

        events.Rule(
            self,
            "PutObjectRule",
            event_pattern=events.EventPattern(
                source=["aws.s3"], detail_type=["Object Created"]
            ),
        ).add_target(
            targets.LambdaFunction(
                put_object_processor.function,
            )
        )

        # Create an EventBridge Rule to match updated ACLs
        change_acl_processor = LambdaFunction(
            scope=self,
            construct_id="ChangeAclFunction",
            code=lambda_.Code.from_asset("lambda_functions/s3_event_processor"),
        )

        events.Rule(
            self,
            "ChangeAclRule",
            event_pattern=events.EventPattern(
                source=["aws.s3"], detail_type=["Object ACL Updated"]
            ),
        ).add_target(
            targets.LambdaFunction(
                change_acl_processor.function,
            )
        )

        # Create an EventBridge Rule to match new objects larger than 1MB
        large_objects_processor = LambdaFunction(
            scope=self,
            construct_id="LargeObjectsFunction",
            code=lambda_.Code.from_asset("lambda_functions/s3_event_processor"),
        )

        events.Rule(
            self,
            "LargeObjectsRule",
            event_pattern=events.EventPattern(
                source=["aws.s3"],
                detail_type=["Object Created"],
                detail={
                    "object": {
                        "size": [{"numeric": [">", 1048576]}]  # 1024 * 1024 bytes
                    }
                },
            ),
        ).add_target(
            targets.LambdaFunction(
                large_objects_processor.function,
            )
        )
