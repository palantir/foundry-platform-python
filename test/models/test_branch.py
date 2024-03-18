from pydantic import ValidationError
import pytest
from foundry.models import Branch


def test_from_dict():
    r = Branch.from_dict(
        {
            "branchId": "123",
            "transactionRid": "ri.a.b.c.d",
        }
    )
    assert r.branch_id == "123"
    assert r.transaction_rid == "ri.a.b.c.d"


def test_from_dict_extra():
    with pytest.raises(ValidationError) as error:
        # Expect extra property to be forbidden to be default
        r = Branch.from_dict(
            {
                "branchId": "123",
                "DOES_NOT_EXIST": "FOO",
            },
        )

    r = Branch.from_dict(
        {
            "branchId": "123",
            "DOES_NOT_EXIST": "FOO",
        },
        allow_extra=True,
    )

    assert r.branch_id == "123"
