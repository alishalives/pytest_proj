from utils import dicts

data = {"vcs": "mercurial"}


def test_get_vall():
    assert dicts.get_val(data, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"
    assert dicts.get_val("", "vcs", "git") == "git"

