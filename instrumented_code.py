# Initialize coverage tracking
branch_coverage = {
    "contains_if_cache_complete": False,
    "contains_for_loop": False,
    "contains_if_item_equals": False,
    "contains_elif_item_greater": False,
    "parse_hms_if_none": False,
    "parse_hms_elif_greater": False,
    "parse_hms_else": False
}

class YourClass:
    def __init__(self):
        self._cache_complete = False
        self._cache = []

    def __contains__(self, item): 
        global branch_coverage

        if self._cache_complete:
            branch_coverage["contains_if_cache_complete"] = True
            return item in self._cache 

        else: 
            branch_coverage["contains_for_loop"] = True
            for i in self:
                if i == item: 
                    branch_coverage["contains_if_item_equals"] = True
                    return True 
                elif i > item: 
                    branch_coverage["contains_elif_item_greater"] = True
                    return False 
        return False

    def _parse_hms(self, idx, tokens, info, hms_idx):
        global branch_coverage
        
        if hms_idx is None:
            branch_coverage["parse_hms_if_none"] = True
            hms = None
            new_idx = idx
        elif hms_idx > idx:
            branch_coverage["parse_hms_elif_greater"] = True
            hms = info.hms(tokens[hms_idx])
            new_idx = hms_idx
        else:
            branch_coverage["parse_hms_else"] = True
            # Looking backwards, increment one.
            hms = info.hms(tokens[hms_idx]) + 1
            new_idx = idx
        return (new_idx, hms)

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch}: {'Hit' if hit else 'Missed'}")
