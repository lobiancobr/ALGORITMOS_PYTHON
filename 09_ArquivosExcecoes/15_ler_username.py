if Path("username.json").exists():
    print(Path("username.json").read_text(encoding="utf-8"))