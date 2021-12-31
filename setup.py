"""Project setup."""

import setuptools

with open(file="README.md", encoding="utf-8") as fp:
    long_description = fp.read()

setuptools.setup(
    name="Monitor Events from Multiple S3 Buckets with EventBridge",
    version="0.0.1",
    description="Bite-Sized Serverless: Monitor Events from Multiple S3 Buckets with EventBridge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bite-Sized Serverless",
    package_dir={"": "monitor_events_from_multiple_s3_buckets_with_eventbridge"},
    packages=setuptools.find_packages(
        where="monitor_events_from_multiple_s3_buckets_with_eventbridge"
    ),
    install_requires=[
        "aws-cdk.core==1.137.0",
        "aws-cdk.aws_events==1.137.0",
        "aws-cdk.aws_events_targets==1.137.0",
        "aws-cdk.aws_lambda==1.137.0",
        "aws-cdk.aws_s3==1.137.0",
        "black==21.6b0",
        "pylint==2.10.2",
        "python-dotenv==0.17.0",
        "stringcase==1.2.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
