"""Klogs Payment Gateway Python Client"""

import requests
import json
from typing import Optional, Dict, Any
from urllib.parse import urljoin, urlencode

from .utils import create_auth_headers, is_success_status_code
from .models import Response


class KlogsHttpClient:
    """Base HTTP client for Klogs API"""
    
    def __init__(self, base_url: str, api_key: str, secret_key: str, 
                 additional_headers: Optional[Dict[str, str]] = None):
        """
        Initialize HTTP client.
        
        Args:
            base_url: Base URL for the API
            api_key: API key for authentication
            secret_key: Secret key for authentication
            additional_headers: Additional headers to include in requests
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.secret_key = secret_key
        self.additional_headers = additional_headers or {}
        self.session = requests.Session()
    
    def _get_headers(self) -> Dict[str, str]:
        """
        Get headers for API request including authentication.
        
        Returns:
            Dictionary of headers
        """
        headers = create_auth_headers(self.api_key, self.secret_key)
        headers.update(self.additional_headers)
        return headers
    
    def _build_url(self, resource_uri: str) -> str:
        """
        Build full URL from resource URI.
        
        Args:
            resource_uri: Resource URI (relative path)
            
        Returns:
            Full URL
        """
        if not resource_uri.startswith('/'):
            resource_uri = '/' + resource_uri
        return urljoin(self.base_url, resource_uri)
    
    def _handle_response(self, response: requests.Response, response_class=None) -> Any:
        """
        Handle HTTP response.
        
        Args:
            response: HTTP response object
            response_class: Class to deserialize response to
            
        Returns:
            Deserialized response object
            
        Raises:
            Exception: If response indicates an error
        """
        try:
            data = response.json()
        except json.JSONDecodeError:
            raise Exception(f"Failed to parse response: {response.text}")
        
        if not is_success_status_code(response.status_code):
            error_msg = data.get('error', {}).get('summary', 'Unknown error')
            raise Exception(f"API Error: {error_msg}")
        
        if response_class:
            return response_class.from_dict(data)
        return data
    
    def get(self, resource_uri: str, params: Optional[Dict] = None, 
            response_class=None) -> Any:
        """
        Send GET request.
        
        Args:
            resource_uri: Resource URI
            params: Query parameters
            response_class: Class to deserialize response to
            
        Returns:
            Response object
        """
        url = self._build_url(resource_uri)
        headers = self._get_headers()
        
        response = self.session.get(url, headers=headers, params=params)
        return self._handle_response(response, response_class)
    
    def post(self, resource_uri: str, body: Any = None, 
             response_class=None) -> Any:
        """
        Send POST request.
        
        Args:
            resource_uri: Resource URI
            body: Request body (will be JSON serialized)
            response_class: Class to deserialize response to
            
        Returns:
            Response object
        """
        url = self._build_url(resource_uri)
        headers = self._get_headers()
        
        json_data = None
        if body is not None:
            if hasattr(body, 'to_dict'):
                json_data = body.to_dict()
            else:
                json_data = body
        
        response = self.session.post(url, headers=headers, json=json_data)
        return self._handle_response(response, response_class)
    
    def put(self, resource_uri: str, body: Any = None, 
            response_class=None) -> Any:
        """
        Send PUT request.
        
        Args:
            resource_uri: Resource URI
            body: Request body (will be JSON serialized)
            response_class: Class to deserialize response to
            
        Returns:
            Response object
        """
        url = self._build_url(resource_uri)
        headers = self._get_headers()
        
        json_data = None
        if body is not None:
            if hasattr(body, 'to_dict'):
                json_data = body.to_dict()
            else:
                json_data = body
        
        response = self.session.put(url, headers=headers, json=json_data)
        return self._handle_response(response, response_class)
    
    def delete(self, resource_uri: str, response_class=None) -> Any:
        """
        Send DELETE request.
        
        Args:
            resource_uri: Resource URI
            response_class: Class to deserialize response to
            
        Returns:
            Response object
        """
        url = self._build_url(resource_uri)
        headers = self._get_headers()
        
        response = self.session.delete(url, headers=headers)
        return self._handle_response(response, response_class)
