# contactless
Serverless Contact Us page

## About

This is an example application which makes a servless contact page using only Lambda functions (no static content)

## History

May 22, 2020

refactor to clear the seperation of base account setup with app stack.

Assumes the following exist for auto-deploy.
- Travis CI environ configured with AWS credentials
- Travis yaml file indicates which branches to build on
- Each branch build expects to find corresponding build properties in */foundation/travsci/contactless* SSM key



Structure of SSM config:
```
{
  'build_bucket': XXX,
  'branches': {
    'branch': {
      'stack_name': XXX,
      'domain_name': XXX,
      'api_name': XXX,
      'cert_arn': XXXX
    }
  }
}
```

The CI process is configured to assume a role in an AWS account/region; this region is expected to have a SSM parameter */contactless/build/{branch}/config* where branch corresponds to the **TRAVIS_BRANCH** environment variable in the build shell.

The script *config.py* can be used with *--init*, *--save*, *--load* options to set the values from command line.





May 5, 2019

 This is publicly hosted on GitHub;   To automate a build process within an AWS environment, you can use Travis CI plug-in

We expect the *contactless-cfn-base.json* template to be used to create an initial stack in the target AWS environment (this creates the */travisci/contactless* **SSM** property); and the create another **SSM** config property with the name */travisci/contactless/BRANCH* for each branch you which to have an automated build on.


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


## Build Steps


4/14/19 - remove Code Pipeline, removed old serverless.yml.
running in AWS account throught Code Pipeline (on *init* and *dev* branches)

Build as of 12/22 failed *init*;  the `sam validate` step failed


## TODO

Once I get this SAM stack up and running would like to add Cognito Authentication to the stack
