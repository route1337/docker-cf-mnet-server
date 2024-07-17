Cloudflare Zero Trust Access Managed Network Server
===================================================
This is a simple docker container that allows you to run a [Cloudflare managed network location](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/configure-warp/managed-networks)
with ease. Deploy it on any network where you intend to take advantage of Cloudflare WARP client settings based on network location.

Docker -> GHCR
--------------
Route 1337 LLC is moving to ghcr.io and away from Docker Hub.  
This does mean that anything in the `route1337` namespace on Docker Hub should no longer be trusted, as it could be run by an attacker paying for the namespace.

Running The Server
---------------
You can either mount your own volume containing the SSL cert and key, or let the container generate its own.  
Mounting your own is the recommended course of action as you should always use your own certs.

We offer a helm chart called `cloudflare-mnet` in our public [helm charts](https://helm-charts.route1337.com/) repo.

Running Without Docker
----------------------
This Python3 code is fairly simple, and can be run directly on a host. It does rely on the hard coded folder of `/cert/`
for the SSL `server.crt` and `server.key` files, but otherwise you can ignore Docker.

Cloudflare Requirements
-----------------------
According to Cloudflare the following constraints are in place:

1. "The WARP client requires certificates to include `CN` and `subjectAltName` metadata. You can use `example.com` **or any other domain**."
   1. For security reasons, we recommend domains that you actually control despite this server serving a dummy page.

Web Page
--------
For configuration ease, the web page presented by this server will display the following information:

1. The name of the network you should put in the ZTA console (If specified with the `NETWORK_NAME` env var)
2. The SHA-256 fingerprint of the TLS certificate for use in the ZTA console

Donate To Support This Container
--------------------------------
Route 1337 LLC's open source code heavily relies on donations. If you find this container useful, please consider using the GitHub Sponsors button to show your continued support.

Thank you for your support!
