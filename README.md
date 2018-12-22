# contactless
Serverless Contact Us page


## Install notes

This repo is designed to be able to be pushed to a Stack with key environment parameters provided, and the rest runs through a CI stack using the *buildspec.yml* file.

1. create the base stack from *contactless-cfn-base.json*
2. The *template.yml* uses the SAM framework from there
2. the *serverless.yml* builds from there


## Build Steps



running in AWS account throught Code Pipeline (on *init* and *dev* branches)

Build as of 12/22 failed *init*;  the `sam validate` step failed
