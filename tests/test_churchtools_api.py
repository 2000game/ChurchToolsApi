#   -------------------------------------------------------------
#   Copyright (c) Felix Kotschenreuther. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   -------------------------------------------------------------
"""Here are all the exceptions defined that can be raised by the church_tools_api package."""

from __future__ import annotations

from unittest.mock import patch

import requests
import pytest

from ChurchToolsApi.churchtools_api import ChurchToolsApi
from ChurchToolsApi.exceptions import ChurchToolsApiConnectionException


def test_churchtools_api_init(class_constructor):
    with patch.object(ChurchToolsApi, "authenticate") as mock_authenticate:
        api = class_constructor()
        assert api.url == "https://demo.church.tools"
        assert api.token == "token"
        assert api.session is None
        mock_authenticate.assert_called_once()


def test_churchtools_api_1(class_constructor):
    api = class_constructor()


@patch.object(ChurchToolsApi, "authenticate")
def test_churchtools_api_authenticate_wrong_url(mock_authenticate):
    mock_authenticate
    api = ChurchToolsApi("https://demo.church.tools", "token")
    with patch.object(api.session, "get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError
        try:
            api.authenticate()
        except Exception as exc:
            assert isinstance(exc, ChurchToolsApiConnectionException)
            assert str(exc) == "Could not connect to the church tools instance."
        else:
            AssertionError("Expected exception was not raised.")
