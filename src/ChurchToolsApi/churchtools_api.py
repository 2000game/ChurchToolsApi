#   -------------------------------------------------------------
#   Copyright (c) Felix Kotschenreuther. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   -------------------------------------------------------------
"""This module contains the ChurchToolsApi class."""

from __future__ import annotations

import requests
from ChurchToolsApi.exceptions import (
    ChurchToolsApiConnectionException,
    ChurchToolsApiNotFoundException,
    ChurchToolsApiAuthenticationException,
)


class ExternalCommunicator:
    def __init__(self) -> None:
        pass

    def external_authenticate(self) -> str:
        return "Authenticated via authenticate function"


class ChurchToolsApi:
    """
    This class represents the ChurchToolsApi object.
    """

    def __init__(self, url, token):
        """
        Initialize the ChurchToolsApi object either with a token.
        :param url: URL of the church tools instance
        :param token: Token for authentication
        """
        self.url = url
        self.token = token
        self.session = None
        self.authenticate()

    def authenticate(self) -> None:
        """
        Authenticate with the given credentials.
        """
        if self.session is None:
            self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Login {self.token}"})

        # Check if the inputs are valid

        try:
            response = self.session.get(f"{self.url}/api/whoami")
        except requests.exceptions.ConnectionError as exc:
            raise ChurchToolsApiNotFoundException("Could not connect to the church tools instance.") from exc

        if response.status_code == 401:
            raise ChurchToolsApiAuthenticationException("Could not authenticate with the given token.")

        if response.status_code != 200:
            raise ChurchToolsApiConnectionException("Could not connect to the church tools instance.")

        if response.url != f"{self.url}/api/whoami":
            # This happens when the prefix of the church.tools url is wrong
            raise ChurchToolsApiNotFoundException("Could not connect to the church tools instance.")
