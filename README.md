# About

This repository contains new overture analysis schemas for the clin project.

There is also an image to seamlessly apply them.

# Usage

Build a docker image from this project's **Dockerfile**.

Run the following scripts in the image:
- **applyClinReadAlignment.py**

The scripts are idempotent and can be composed with the following environment variables:
- KEYCLOAK_URL: Full base url to access keycloak (ex: https://mykeycloack:8443)
- KEYCLOAK_REALM: Keycloak realm to use
- KEYCLOAK_CLIENT: Keycloak client to use
- KEYCLOAK_CLIENT_SECRET: Symmetric key to use to encrypt keycloak login
- KEYCLOAK_USER: Keycloak user to login as
- KEYCLOAK_USER_PASSWORD: Password of the provided keycloak user
- SONG_URL: Full base url to access SONG (ex: https://mysong:8443)