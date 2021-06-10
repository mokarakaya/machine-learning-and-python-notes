# Named Entities in SpaCy

PERSON:      People, including fictional.

NORP:        Nationalities or religious or political groups.

FAC:         Buildings, airports, highways, bridges, etc.

ORG:         Companies, agencies, institutions, etc.

GPE:         Countries, cities, states.

LOC:         Non-GPE locations, mountain ranges, bodies of water.

PRODUCT:     Objects, vehicles, foods, etc. (Not services.)

EVENT:       Named hurricanes, battles, wars, sports events, etc.

WORK_OF_ART: Titles of books, songs, etc.

LAW:         Named documents made into laws.

LANGUAGE:    Any named language.

DATE:        Absolute or relative dates or periods.

TIME:        Times smaller than a day.

PERCENT:     Percentage, including ”%“.

MONEY:       Monetary values, including unit.

QUANTITY:    Measurements, as of weight or distance.

ORDINAL:     “first”, “second”, etc.

CARDINAL:    Numerals that do not fall under another type.

# IOB scheme (Inside–outside–beginning)
- I: Inside (Los B-LOC Angeles I-LOC)
- O: Outside (going O)
- B: Beginning (Alex B-PER)

# BILUO scheme (Begin, In , Last, Unit, Out)

- [ Ratinov and Roth ](https://www.aclweb.org/anthology/W09-1119/) shows that ML algorithms learn BILUO scheme better than IOB.
- Begin: The first token of a multi-token entity.
- In: An inner token of a multi-token entity.
- Last: The final token of a multi-token entity.
- Unit: A single token entity.
- Out: A non-entity token.
