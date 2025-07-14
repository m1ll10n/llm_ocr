import pytest
import app.ocr_utils as ocr_utils


def test_extract_text():
    result = ocr_utils.extract_text("license.png")
    assert isinstance(result, str)
