#   -------------------------------------------------------------
#   Copyright (c) Felix Kotschenreuther. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   -------------------------------------------------------------
"""Here are all the exceptions defined that can be raised by the church_tools_api package."""

from __future__ import annotations

from ChurchToolsApi import ChurchToolsApi

from unittest.mock import patch


def test_churchtools_api_init():
    with patch.object(ChurchToolsApi, "authenticate") as mock_authenticate:
        api = ChurchToolsApi("https://demo.church.tools", "token")
        assert api.url == "https://demo.church.tools"
        assert api.token == "token"
        assert api.session is not None
        mock_authenticate.assert_called_once()
