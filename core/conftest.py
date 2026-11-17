import pytest
from core import json_format as jf


# Every test gets its own empty log, so the real memory/chat.log is never touched
@pytest.fixture(autouse=True)
def temp_log(tmp_path, monkeypatch):
    monkeypatch.setattr(jf, "LOG_PATH", tmp_path / "chat.log")
    jf._log.cache_clear()  # _log() is @cache'd; forget any log opened at the old path
    yield
    jf._log.cache_clear()
