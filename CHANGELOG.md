Cloudflare Zero Trust Access Managed Network Server: Changelog
==============================================================
A list of all the changes made to this repo, and the container service it contains

Version 1.0.0
-------------

1. Breaking Change: Moving away from Docker Hub for GitHub Container Registry

Version 0.1.1
-------------

1. Fixed some typos
2. Added `test-compose.yml` and updated `docker-compose.yml` to reflect specific environments
3. Changed Flask port to `8443` to better reflect that it's SSL
4. Added empty `test-config` folder for use as a compose file volume mount to store the cert
5. Remove colons from SHA-256 output as Cloudflare console doesn't expect them

Version 0.1.0
-------------

1. Initial Pre-release of repository

Return to [README](README.md)
