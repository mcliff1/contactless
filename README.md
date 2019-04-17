# contactless
Serverless Contact Us page


April 14, 2019; refactor this to no longer use *AWS CodeBuild*, rather use *TravisCI*

[travis ci](https://dev.to/codevbus/deploy-aws-lambda-functions-with-aws-sam-cli-and-travis-ci-part-2-2goh)
[travis ci](https://sysengcooking.com/blog/aws-lambda-with-travis-2/)


1. make a policy/role to execute this under; add those keys to the Travis CI config secrets  (I can use the CodeBuild Role) - TODO later I can make this work as a NIU type of account
2. update the .travis.yaml



[aws tools](https://dev.to/sagar/implement-a-serverless-cicd-pipeline-with-aws-amazon-web-services-438f)

## Install notes

This repo is designed to be able to be pushed to a Stack with key environment parameters provided, and the rest runs through a CI stack using the *buildspec.yml* file.

1. create the base stack from *contactless-cfn-base.json*
2. The *template.yml* uses the SAM framework from there
2. the *serverless.yml* builds from there (no longer used)


## Build Steps


4/14/19 - remove Code Pipeline, removed old serverless.yml.
running in AWS account throught Code Pipeline (on *init* and *dev* branches)

Build as of 12/22 failed *init*;  the `sam validate` step failed


## TODO

Once I get this SAM stack up and running would like to add Cognito Authentication to the stack
