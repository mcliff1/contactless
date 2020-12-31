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
        self.account_name = self.session.client('ssm').get_parameter(Name='/foundation/account/name')['Parameter']['Value']

    def setup(self, branch: str, stack: str = None, api_name: str = None):
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
        ssm_client = self.session.client('ssm')
        ssm_param = lambda x: ssm_client.get_parameter(Name=x)['Parameter']['Value']

        print(f'account name is {self.account_name}')
        result = {
          'stack_name': stack if stack else f'{self.account_name}-contactless',
          'domain_name': ssm_param('/foundation/dns/mattcliffnet'),
          'api_name': api_name if api_name else 'contactless', #/ contactless (for now)
          'cert_arn': ssm_param('/foundation/cert/mattcliff.net')
        }
        ssm_client.put_parameter(
            Name=f'/contactless/build/{branch}/config',
            Value=json.dumps(result),
            Type='String',
            Description=f'Contactless Configuration for Branch: {branch}'
        )



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

    print(json.dumps(TOOL.setup('feature-init')))
