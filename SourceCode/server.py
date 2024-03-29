#!/usr/bin/env python3
"""A simple webserver that serves some basic data for Cloudflare ZTA Managed Network usage"""
#
# Python Script:: server.py
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

import logging
import os
import OpenSSL.crypto
from flask import Flask
from cheroot.wsgi import Server as WSGIServer
from cheroot.ssl.builtin import BuiltinSSLAdapter
import generate


flask_app = Flask(__name__)


@flask_app.route("/")
def server_index():
    """
    Display content to a Flask server
    """
    # Get the server's name from the environment or use the hostname as a default
    server_name = os.getenv("NETWORK_NAME", default="ZTA-" + os.uname()[1])
    # Obtain the SHA-256 certificate fingerprint
    with open('/cert/server.crt', encoding='utf-8') as cert_file:
        server_cert = OpenSSL.crypto.load_certificate(
            OpenSSL.crypto.FILETYPE_PEM, cert_file.read())
    cert_digest = server_cert.digest("sha256").decode("utf-8").replace(":", "")
    server_output = "<h1>Cloudflare Zero Trust Managed Network Server</h1><br/>" \
                    f"<b>Server Name:</b> {server_name}<br/>" \
                    f"<b>TLS Cert SHA-256:</b> {cert_digest}"
    return server_output


def main(use_existing_cert: bool):
    """
    The main function that triggers and runs the server functions

    Args:
    use_existing_cert: Do we generate a cert or load one?
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        datefmt='%m/%d/%G %H:%M:%S', format='%(asctime)s %(message)s')
    if use_existing_cert:
        logging.info("An existing cert has been found and will be used.")
    else:
        logging.info("No cert found, generating one.")
        logging.warning("If you are not mounting a volume,"
                        " it's possible the generated cert will be lost!")
        generate.generate_cert(os.uname()[1])

    # Configure SSL
    ssl_config = BuiltinSSLAdapter(certificate='/cert/server.crt', private_key='/cert/server.key',
                                   certificate_chain=None)
    # Configure CherryPy on 0.0.0.0:8443
    server = WSGIServer(
        ('0.0.0.0', 8443), flask_app,
        server_name=os.getenv("NETWORK_NAME", default="ZTA-" + os.uname()[1]))
    # Configure CherryPy to use SSL
    server.ssl_adapter = ssl_config
    logging.info("Starting the server")
    server.start()


if __name__ == '__main__':
    cert_exists = os.path.isfile("/cert/server.crt")
    main(cert_exists)
