def test_substring(full_string, substring):
    assert substring in full_string, f"expected {substring!r} to be substring of {full_string!r}"

# !r - автовыделение в кавычки