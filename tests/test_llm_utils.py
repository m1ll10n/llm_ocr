import pytest
import app.llm_utils as llm_utils


def test_generate_json():
    result = llm_utils.generate_json("")
    assert isinstance(result, dict)
    assert "dln" in result
    assert "exp" in result
    assert "family_name" in result
    assert "given_name" in result
    assert "address" in result
    assert "sex" in result
    assert "height" in result
    assert "weight" in result
    assert "eyes" in result
    assert "dob" in result
    assert "class" in result
    assert "iss" in result
    assert "endorsements" in result
    assert "restrictions" in result
