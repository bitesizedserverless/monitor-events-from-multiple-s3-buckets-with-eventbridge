"""Module for the main MonitorEventsFromMultipleS3BucketsWithEventbridge Stack."""

# Standard library imports
# -

# Third party imports
# -

# Local application/library specific imports
from aws_cdk import core as cdk


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

        # The code that defines your stack goes here
