from PyPoE.poe.file.translations import get_custom_translation_file
from RePoE.util import write_json, call_with_default_args


def _convert_tags(n_ids, tags, tags_types):
    f = ["ignore" for _ in range(n_ids)]
    for tag, tag_type in zip(tags, tags_types):
        if tag_type == '%':
            f[tag] = "#"
        elif tag_type == 'd%':
            f[tag] = "#%"
        elif tag_type.startswith('$') and 'd' in tag_type:
            f[tag] = tag_type[1:].replace('d', "#")
        else:
            print("Unknown tag type:", tag_type)
    return f


def _convert_range(translation_range):
    rs = []
    for r in translation_range:
        if r.min is None and r.max is None:
            rs.append({})
        elif r.min is None:
            rs.append({
                'max': r.max
            })
        elif r.max is None:
            rs.append({
                'min': r.min
            })
        else:
            rs.append({
                'min': r.min,
                'max': r.max
            })
    return rs


def _convert_handlers(n_ids, index_handlers):
    hs = [[] for _ in range(n_ids)]
    for handler_name, ids in index_handlers.items():
        for i in ids:
            # Indices in the handler dict are 1-based
            hs[i - 1].append(handler_name)
    return hs


def _convert(tr, tag_set):
    ids = tr.ids
    n_ids = len(ids)
    english = []
    for s in tr.get_language('English').strings:
        tags = _convert_tags(n_ids, s.tags, s.tags_types)
        tag_set.update(tags)
        english.append({
            'condition': _convert_range(s.range),
            'string': s.as_format_string,
            'format': tags,
            'index_handlers': _convert_handlers(n_ids, s.quantifier.index_handlers)
        })
    return {
        'ids': ids,
        'English': english
    }


def _get_stat_translations(tag_set, translations, custom_translations):
    previous = set()
    root = []
    for tr in translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            print("Duplicate id", tr.ids)
            continue
        previous.add(id_str)
        root.append(_convert(tr, tag_set))
    for tr in custom_translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            print("Duplicate custom id", tr.ids)
            continue
        previous.add(id_str)
        result = _convert(tr, tag_set)
        result['hidden'] = True
        root.append(result)
    return root


def write_stat_translations(data_path, translation_file_cache, **kwargs):
    tag_set = set()
    for in_file, out_file in WRITTEN_FILES:
        translations = translation_file_cache[in_file].translations
        result = _get_stat_translations(tag_set, translations,
                                        get_custom_translation_file().translations)
        write_json(result, data_path, out_file)
    print("Possible format tags: {}".format(tag_set))


WRITTEN_FILES = {
    ('stat_descriptions.txt', 'stat_translations'),
    ('map_stat_descriptions.txt', 'stat_translations_areas'),
    ('atlas_stat_descriptions.txt', 'stat_translations_atlas'),
}


# The stat description files can include each other and can override stats from included files. E.g. the same stat
# may have different translations on active and support gems. Because of that, they can't simply be merged together
# This module only covers the files in WRITTEN_FILES. I can add more on request.

# 'stat_descriptions.txt' tree
# (use stat_descriptions.txt for everything but chest, gem, area, atlas, passive skill tree,
#  leaguestone and monster stats)
# - chest (strongboxes)
# - gem (support gems)
#   - active_skill_gem
#     - skill (skills/active gems not covered by a child file,
#              use 'skillpopup_stat_filters.txt' to get the matching child file)
#       - aura_skill
#       - beam_skill
#       - curse_skill
#       - debuff_skill
#       - minion_skill
#         - minion_attack_skill
#         - minion_spell_skill
#       - offering_skill
# - map (areas, not the map items themselves)
#   - atlas (sextants)
# - passive_skill (passive skill tree)
#   - passive_skill_aura (aura effects granted by passive skill tree stats?)
# - leaguestone
# 'monster_stat_descriptions.txt' tree


if __name__ == '__main__':
    call_with_default_args(write_stat_translations)
