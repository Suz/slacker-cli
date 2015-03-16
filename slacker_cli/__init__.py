#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Send message to Slack from command line
"""

from slacker import Slacker
import argparse
import sys
import os

def to_bin(ascii_msg):
    return ' '.join(bin(ord(c))[2:].zfill(8) for c in ascii_msg.encode('UTF-8'))


def id_from_list_dict(list_dict, key_name):
    for d in list_dict:
        if d['name'] == key_name:
            return d['id']


def post_message(token, channel, message):
    slack = Slacker(token)
    slack.chat.post_message(channel, message)


def post_message_binary(token, channel, message):
    """ post a message to real_engineering and echo it to channel in binary """
    slack = Slacker(token)
    slack.chat.post_message(channel, to_bin(message))
    slack.chat.post_message('#real_engineering', message)


def get_channel_id(token, channel_name):
    slack = Slacker(token)
    channels = slack.channels.list().body['channels']
    return id_from_list_dict(channels, channel_name)


def get_user_id(token, user_name):
    slack = Slacker(token)
    members = slack.users.list().body['members']
    return id_from_list_dict(members, user_name)


def upload_file(token, channel, file_name):
    """ upload file to a channel """

    slack = Slacker(token)
    channel_id = get_channel_id(token, channel)

    slack.files.upload(file_name, channels=channel_id)


def args_priority(args, environ):
    '''
        priority of token
        1) as argumment: -t
        2) as environ variable
    '''

    arg_token = args.token

    slack_token_var_name = 'SLACK_TOKEN'
    if slack_token_var_name in environ.keys():
        token = environ[slack_token_var_name]
    else:
        token = None

    if arg_token:
        token = arg_token

    return token, args.channel


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--channel", help="Slack channel")
    parser.add_argument("-u", "--user", help="Slack user")
    parser.add_argument("-b", "--binary", action="store_true", default=False, help="Convert message to binary")
    parser.add_argument("-t", "--token", help="Slack token")
    parser.add_argument("-f", "--file", help="File to upload")

    args = parser.parse_args()

    token, channel = args_priority(args, os.environ)
    user = args.user
    binary = args.binary 
    message = sys.stdin.read()
    file_name = args.file

    if token and channel and message:
        if binary:
            post_message_binary(token, '#' + channel, message)
        else:
            post_message(token, '#' + channel, message)


    if token and user and message:
        post_message(token, get_user_id(token, user), message)

    if token and channel and file_name:
        upload_file(token, channel, file_name)


if __name__ == '__main__':
    main()
