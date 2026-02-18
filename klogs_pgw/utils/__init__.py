"""Klogs Payment Gateway - Authentication and Utility Functions"""

import hmac
import hashlib
import secrets
import string
import time
from datetime import datetime


# Constants
def create_random_string(length: int = 32) -> str:
    """
    Generate a URL-friendly random string.
    
    Args:
        length: Length of the random string (default: 32)
        
    Returns:
        Random string containing alphanumeric characters
    """
    allowed_chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(allowed_chars) for _ in range(length))


def utc_ticks() -> int:
    """
    Get current UTC time in .NET ticks format.
    
    Returns:
        Current UTC time as .NET ticks
    """
    # Get current unix time in milliseconds
    return int(time.time() * 1000)


def create_hmac_signature(cipher_text: str, secret_key: str) -> str:
    """
    Create HMAC-SHA256 signature.
    
    Args:
        cipher_text: Text to sign
        secret_key: Secret key for HMAC
        
    Returns:
        Hex-encoded HMAC-SHA256 signature
    """
    mac = hmac.new(
        secret_key.encode('utf-8'),
        cipher_text.encode('utf-8'),
        hashlib.sha256
    )
    return mac.hexdigest()


def create_auth_headers(api_key: str, secret_key: str) -> dict:
    """
    Create authentication headers for Klogs API requests.
    
    Args:
        api_key: API key
        secret_key: Secret key
        
    Returns:
        Dictionary containing authentication headers
    """
    random_string = create_random_string(32)
    timestamp = str(utc_ticks())
    
    # Create signature: HMAC-SHA256(apiKey + randomString + timestamp, secretKey)
    cipher_text = f"{api_key}{random_string}{timestamp}"
    signature = create_hmac_signature(cipher_text, secret_key)
    
    return {
        "X-Api-Key": api_key,
        "X-Klogs-Rnd": random_string,
        "X-Klogs-Timestamp": timestamp,
        "X-Klogs-Signature": signature,
        "Content-Type": "application/json"
    }


def is_success_status_code(status_code: int) -> bool:
    """
    Check if HTTP status code indicates success.
    
    Args:
        status_code: HTTP status code
        
    Returns:
        True if status code is in the 2xx range
    """
    return 200 <= status_code <= 299
