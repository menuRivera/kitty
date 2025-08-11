#!/usr/bin/env python3

def get_tab_title_template(is_active):
    bg = "{fmt.bg.default}"

    property = "active_tab_title_template" if is_active \
        else "tab_title_template"

    title = "{title if title == '~' else tab.active_wd.split('/')[-1]}"

    return f'{property} "{bg}<{title}> "' if is_active \
        else f'{property} "{bg} {title}  "'


if __name__ == "__main__":
    print(get_tab_title_template(is_active=True))
    print(get_tab_title_template(is_active=False))
