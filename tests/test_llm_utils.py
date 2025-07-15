import pytest
import app.llm_utils as llm_utils


def test_generate_json():
    result = llm_utils.generate_json("given_name: John family_name: Doeeyes:brown")
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


@pytest.mark.parametrize("text", [(None), ("")])
def test_generate_json_none(text: str):
    with pytest.raises(ValueError):
        llm_utils.generate_json(text)
