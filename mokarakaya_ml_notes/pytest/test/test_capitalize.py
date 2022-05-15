from mokarakaya_ml_notes.pytest.source import capitalize


def test_capital_case():
    assert capitalize.capital_case("semaphore") == "Semaphore"
