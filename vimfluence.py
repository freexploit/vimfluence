#!/usr/bin/env python

import base64
import argparse


class Vimfluence(object):

    """Docstring for Vimfluence. """


    def __init__(self, resource=None, url=None, auth_string=None):

        self.resource = resource
        self.url = url
        try:
            self.auth_string = base64.b64encode(auth_string)

        except Exception as e:
            raise e


def main():
    parser = argparse.ArgumentParser(description='Manage Confluence over CLI')
    parser.add_argument('echo')
    args = parser.parse_args()
    print(args.echo)

if __name__ == "__main__":
    main()

