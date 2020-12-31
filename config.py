#!/usr/bin/env python
"""
Configuration Script for Contactless App

Usage:
config.py -p PROFILE -r REGION CMD {opts}
where CMD is
  init  reset/inital setup
  save export
  load import
  set --key --value
  get [--key]

requires:
  boto3



    'branch': {
      'stack_name': XXX,
      'domain_name': XXX,
      'api_name': XXX,
      'cert_arn': XXXX
    }


"""
import json
import argparse


import boto3


class ConfigTool(object):
    """ Tool object """

    def __init__(self, profile, region):
        """ sets up tool aws connection """
        self.session = boto3.Session(profile_name=profile, region_name=region)
        self.account_name = self.session.client('ssm').get_parameter_value(ParameterName='/foundation/account/name')['Paramater']['Value']

    def setup(self, branch: str, stack=None: str):
        """
        runs the initialization setup

        sets the */contactless/build/{branch}/config* as
        {
          'stack_name': XXX,
          'domain_name': XXX,
          'api_name': XXX,
          'cert_arn': XXXX
        }

        """
        result = {
          'stack_name': 'XXX', #{/foundation/account/name}-
          'domain_name': 'XXX',
          'api_name': 'XXX',
          'cert_arn': 'XXXX'
        }



        return result


if __name__ == '__main__':

    def parse():
        """ return CLI args """
        parser = argparse.ArgumentParser()
        parser.add_argument('-r', '--region', action='store', dest='region', help='AWS Region to select [us-west-2]', default='us-west-2') # pylint: disable=C0301
        parser.add_argument('-p', '--profile', action='store', dest='profile', required=True, help='AWS Profile to use') # pylint: disable=C0301
        #parser.add_argument('--login', action='store_true', dest='login', help='Logs into SSO')
        #parser.add_argument('-l', '--list', action='store_true', dest='list', help='Lists Accounts in SSO')
        try:
            arguments = parser.parse_args()
        except:
            parser.print_help()
            print('\nRequirements:')
            print('  - AWS CLI version 2')
            print('  - boto3')
            exit(1)
        return arguments

    ARGS = parse()
    TOOL = ConfigTool(ARGS.profile, ARGS.region)

    print(json.dumps(TOOL.setup()))
