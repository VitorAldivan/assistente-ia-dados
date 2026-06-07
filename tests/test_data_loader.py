from pathlib import Path


def test_estrutura_projeto():
    assert Path("src").exists()