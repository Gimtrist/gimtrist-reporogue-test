from src.demo import room_signal


def test_room_signal():
    assert "RepoRogue" in room_signal("test")