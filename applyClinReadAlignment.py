import os
import logging
logging.basicConfig(level=logging.DEBUG)

from keycloak import KeyCloakClient
from song import SongClient

logger = logging.getLogger(__name__)

KEYCLOAK_URL = os.environ.get('KEYCLOAK_URL')
KEYCLOAK_REALM = os.environ.get('KEYCLOAK_REALM')
KEYCLOAK_CLIENT = os.environ.get('KEYCLOAK_CLIENT')
KEYCLOAK_CLIENT_SECRET = os.environ.get('KEYCLOAK_CLIENT_SECRET')
KEYCLOAK_USER = os.environ.get('KEYCLOAK_USER')
KEYCLOAK_USER_PASSWORD = os.environ.get('KEYCLOAK_USER_PASSWORD')

SONG_URL = os.environ.get('SONG_URL')

if __name__ == '__main__':
    token = KeyCloakClient(
        '{keycloak_url}/auth/realms/{keycloak_realm}'.format(
            keycloak_url=KEYCLOAK_URL,
            keycloak_realm=KEYCLOAK_REALM
        ),
        KEYCLOAK_CLIENT,
        KEYCLOAK_CLIENT_SECRET
    ).login(
        KEYCLOAK_USER, 
        KEYCLOAK_USER_PASSWORD
    )
    logger.info("Login token: {token}".format(token=token))
    song_client = SongClient(
        SONG_URL,
        token
    )
    
    schemas = song_client.get_schemas()
    if not 'clinReadAlignment' in [result.name for result in schemas.resultSet]:
        logger.info('clinReadAlignment schema missing. Creating it...')
        with open('/opt/clinReadAlignment_schema.json' , 'r') as schema_file:
            schema = schema_file.read()
            song_client.create_schema(schema)
    else:
        logger.info('clinReadAlignment schema already present. Skipping creation.')