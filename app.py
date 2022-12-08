#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_pipeline_lab.cdk_pipeline_lab_stack import CdkPipelineLabStack


app = cdk.App()
CdkPipelineLabStack(app, "CdkPipelineLabStack",
    env=cdk.Environment(account="915879673089", region="us-east-1")
    )

app.synth()
