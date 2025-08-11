#!/usr/bin/env python3

def get_tab_title_template():
    bg = "{fmt.bg.default}"
    property = "tab_title_template"
    title = "{title if title == '~' else tab.active_wd.split('/')[-1]}"

    return f'{property} "{bg} {title}  "'


def get_active_tab_title_template():
    bg = "{fmt.bg.default}"
    property = "active_tab_title_template"
    title = "{title if title == '~' else tab.active_wd.split('/')[-1]}"

    return f'{property} "{bg}<{title}> "'


if __name__ == "__main__":
    print(get_tab_title_template())
    print(get_active_tab_title_template())
