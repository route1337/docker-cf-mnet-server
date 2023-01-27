#!/usr/bin/env python3
"""SSL certificate generation code"""
import OpenSSL.crypto
#
# Python Script:: generate.py
#
# Linter:: pylint
#
# Copyright 2023, Route 1337 LLC, All Rights Reserved.
#
# Maintainers:
# - Matthew Ahrenstein: @ahrenstein
#
# See LICENSE
#


import os


def generate_cert(host_name: str):
    """
    Generate a self-signed OpenSSL certificate for long term use

    Args:
    host_name: The host name for the SSL certificate
    """
    # This is a quick and dirty way to accomplish this and will be made proper later
    generation_command = f"openssl req -x509 -newkey rsa:4096 -sha256 -days 36500 " \
                         f"-nodes -keyout /cert/server.key -out /cert/server.crt -subj" \
                         f" \"/CN={host_name}\" -addext \"subjectAltName=DNS:{host_name}\""
    os.system(generation_command)
