import logging
import os
from contextvars import ContextVar
from typing import Optional
from dotenv import load_dotenv

# Configure logging
logger = logging.getLogger(__name__)

load_dotenv()

# Context variable to store the access token for each request
auth_token_context: ContextVar[str] = ContextVar('auth_token')

def get_auth_token() -> str:
    """Get the authentication token from context."""
    try:
        token = auth_token_context.get()
        if not token:
            # Fallback to environment variable if no token in context
            token = os.getenv("METABASE_SESSION_TOKEN")
            print(f"---Token: {token}")
            if not token:
                raise RuntimeError("No authentication token available")
        return token
    except LookupError:
        token = os.getenv("METABASE_SESSION_TOKEN")
        if not token:
            raise RuntimeError("Authentication token not found in request context or environment")
        return token

def get_metabase_client() :
    """Get HubSpot client with auth token from context."""
    try:
        auth_token = get_auth_token()
        client =  {
            'auth_token': auth_token,
            'url': os.getenv("METABASE_URL")
        }

        return client
    except RuntimeError as e:
        logger.warning(f"Failed to get auth token: {e}")
        return None
    except Exception as e:
        logger.error(f"Failed to initialize HubSpot client: {e}")
        return None
