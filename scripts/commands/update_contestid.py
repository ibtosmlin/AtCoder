from ..config.config_loader import (
    KEY_CONTESTID,
    PATHS,
    load_config_tomlkit,
    save_config_tomlkit,
)


def main(new_id: str) -> str:
    # tomlkit の TOMLDocument を取得
    data = load_config_tomlkit()

    # セクションが存在しない場合は作成
    if KEY_CONTESTID not in data:
        data[KEY_CONTESTID] = {}

    # 値を更新
    data[KEY_CONTESTID] = new_id

    # 保存
    save_config_tomlkit(data)

    return f"✅ Updated {PATHS.CONFIG_TOML} {KEY_CONTESTID} to: {new_id}"


if __name__ == "__main__":
    import sys

    print(main(sys.argv[1]))
