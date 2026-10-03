"""Tiny artifact used by the RepoRogue generated test repository."""


def room_signal(name: str) -> str:
    return f"RepoRogue sees artifact: {name}"


if __name__ == "__main__":
    print(room_signal("src/demo.py"))