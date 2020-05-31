# Run tests:

```
python setup.py install
pytest mokarakaya_ml_notes/pytest/test/

```

# Mocking
- `mocker.patch.object(manager, 'sub_method')`: mocking methods or classes.
- `manager.sub_method.return_value = 120`: setting a return value.
- `@pytest.mark.parametrize`: setting parameters to run the same test with different parameters.
- `@pytest.mark.xfail(raises=Exception)`: verify that test raises `Exception.`
- `@pytest.fixture(scope="module")`: creating mocks for all tests.

# Build and publish package to Pypi

- `python -m pip install --user --upgrade setuptools wheel`
- `python setup.py sdist bdist_wheel`
- `python -m pip install --user --upgrade twine`
- `python -m twine upload --repository uploadpypi dist/*`
- Make sure `uploadpypi` is defined in `.pypirc` as follows before uploading;

```
[distutils]
   index-servers=
       uploadpypi

   [uploadpypi]
   repository: https://upload.pypi.org/legacy/
   username: mokarakaya
   password: password_or_token_here


```

# References
- `https://medium.com/@bfortuner/python-unit-testing-with-pytest-and-mock-197499c4623c`
- `https://packaging.python.org/tutorials/packaging-projects/`
