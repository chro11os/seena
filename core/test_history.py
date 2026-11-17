"""Session delete check. Run: uv run python core/test_history.py"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import json_format as jf

jf.LOG_PATH = Path(tempfile.mkdtemp()) / "chat.log"  # never touch the real memory/chat.log

jf._log().append([{"role": "user", "text": "pre-session message"}])  # no id -> "imported"
jf.add_turn("hi", "hello", "a")
jf.add_turn("bye", "goodbye", "b")

jf.delete_session("a")
assert {m["session"] for m in jf.read_history() if "session" in m} == {"b"}
assert not any(m["role"] == "deleted" for m in jf.read_history())

jf.delete_session("imported")
assert [m["text"] for m in jf.read_history()] == ["bye", "goodbye"]
print("ok")
