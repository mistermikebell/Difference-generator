REMOVED = 'removed'
ADDED = 'added'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
NESTED = 'nested'


def build(before_dict, after_dict):
    added_items = {key: (ADDED, after_dict[key])
                   for key in after_dict.keys() - before_dict.keys()}
    removed_items = {key: (REMOVED, before_dict[key])
                     for key in before_dict.keys() - after_dict.keys()}
    intersec = {}
    for key in before_dict.keys() & after_dict.keys():
        if isinstance(before_dict[key], dict) and isinstance(after_dict[key], dict):  # noqa: E501
            adjusted_value = build(before_dict[key], after_dict[key])
            intersec[key] = (NESTED, adjusted_value)
        elif before_dict[key] == after_dict[key]:
            intersec[key] = (UNCHANGED, before_dict[key])
        else:
            intersec[key] = (CHANGED, [before_dict[key], after_dict[key]])
    return dict(sorted({**added_items, **removed_items, **intersec}.items()))
