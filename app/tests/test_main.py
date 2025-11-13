from unittest.mock import patch

from app.main import main


def test_main():
    with patch("lib.module1.foo") as mock:
        main()
        mock.assert_called_once()
