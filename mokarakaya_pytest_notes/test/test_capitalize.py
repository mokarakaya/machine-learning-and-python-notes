from mokarakaya_pytest_notes.source import capitalize



def test_capital_case():
    assert capitalize.capital_case('semaphore') == 'Semaphore'