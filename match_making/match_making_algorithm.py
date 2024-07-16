from schemas import MatchEntity
def is_match_wrapper(match_entity_prim: MatchEntity):
    def is_match(match_entity_second: MatchEntity) -> bool:
        result = match_entity_prim.field_id == match_entity_second.field_id
        result = result and (match_entity_second.id not in match_entity_prim.likes)
        result = result and (match_entity_second.id not in match_entity_prim.dislikes)
        return result
    return is_match