from core import json_format as jf


def test_delete_hides_only_that_session():
    jf.add_turn("hi", "hello", "a")
    jf.add_turn("bye", "goodbye", "b")
    jf.delete_session("a")
    assert [m["text"] for m in jf.read_history()] == ["bye", "goodbye"]


def test_delete_imported_messages():
    jf._log().append([{"role": "user", "text": "pre-session message"}])  # no session id
    jf.delete_session("imported")
    assert jf.read_history() == []
