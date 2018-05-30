from polyglot.text import Text

t = ("New York is a state in the northeastern United States. "
     "New York is bordered by New Jersey and Pennsylvania to the south and Connecticut, Massachusetts, and Vermont to the east. "
     "The state has a maritime border in the Atlantic Ocean with Rhode Island, east of Long Island, "
     "as well as an international border with the Canadian provinces of Quebec to the north and Ontario to the northwest. "
     "New York was one of the original Thirteen Colonies that formed the United States. "
     "The state of New York, with an estimated 19.8 million residents in 2015,[9] is also referred to as New York State to distinguish it from New York City, "
     "the state's most populous city and its economic hub.")

tokens = Text(t)
for entity in tokens.entities:
    print(entity.tag, entity)