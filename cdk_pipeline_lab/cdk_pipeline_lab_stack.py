from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines
# from aws_cdk import codepipelines
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, ManualApprovalStep
from cdk_pipeline_lab.my_pipeline_app_stage import MyPipelineAppStage

class CdkPipelineLabStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("germaine5/CdkPipelineLab", "main",
                                connection_arn='arn:aws:codestar-connections:us-east-1:915879673089:connection/2cde4b6a-c128-49aa-8f90-b7181191c383'
                            ),
                            
                            
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
                    )
                    
        pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account="915879673089", region="us-east-1")))
            
        testing_stage = pipeline.add_stage(MyPipelineAppStage(self, "testing",
            env=cdk.Environment(account="915879673089", region="us-east-1")))

        testing_stage.add_post(ManualApprovalStep('approval'))
