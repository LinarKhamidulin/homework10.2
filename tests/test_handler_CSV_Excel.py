import pytest
from unittest.mock import Mock, mock_open
from unittest.mock import patch



@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_reading_a_file_csv(mock_file):
    assert open("path/to/open").read() == "data"
    mock_file.assert_called_with("path/to/open")


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_read_excel_file(mock_file):
    assert open("path/to/open").read() == "data"
    mock_file.assert_called_with("path/to/open")