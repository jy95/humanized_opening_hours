from lark.lark import Tree
from lark.lexer import Token

# This dict contains Lark trees for the 50 most frequent fields in OSM
# (on 10 june 2018), so we don't have to parse them.
# They represent about 30% of all fields!

# flake8: noqa

FREQUENT_FIELDS = {
    "24/7": Tree("time_domain", [Tree("rule_sequence", [Tree("always_open", [Token("ALWAYS_OPEN", '24/7')])])]),
    "Mo-Su 09:00-21:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '21'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 08:00-18:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '18'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 10:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 09:00-17:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '17'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 08:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 08:00-17:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '17'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 08:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 09:00-18:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '18'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 09:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 08:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 10:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 10:00-21:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '21'), Token("TWO_DIGITS", '00')])])])])])])]),
    "sunrise-sunset": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("variable_time", [Token("EVENT", 'sunrise')])]), Tree("time", [Tree("variable_time", [Token("EVENT", 'sunset')])])])])])])]),
    "Mo-Su 09:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 09:00-18:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '18'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 08:00-23:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '23'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 09:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "09:00-21:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '21'), Token("TWO_DIGITS", '00')])])])])])])]),
    "08:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 07:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '07'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "10:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 09:00-18:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '18'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 08:00-21:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '21'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 06:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '06'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 07:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '07'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 09:00-23:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '23'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 08:00-18:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '18'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 07:00-23:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '07'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '23'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 11:00-23:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '11'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '23'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 10:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 08:30-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '30')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 22:00-05:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '05'), Token("TWO_DIGITS", '00')])])])])])])]),
    "08:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 09:00-17:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '17'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 06:00-23:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '06'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '23'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 09:00-17:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '17'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 09:00-19:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '19'), Token("TWO_DIGITS", '00')])])])])])])]),
    "09:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '09'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "10:00-21:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '21'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 10:00-23:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '23'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 08:00-16:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '16'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Fr 10:00-18:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Fr')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '18'), Token("TWO_DIGITS", '00')])])])])])])]),
    "10:00-20:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '20'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 11:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '11'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 10:00-19:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '19'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 07:00-21:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '07'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '21'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 08:00-21:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '08'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '21'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Sa 07:00-22:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Sa')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '07'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '22'), Token("TWO_DIGITS", '00')])])])])])])]),
    "Mo-Su 10:00-19:00": Tree("time_domain", [Tree("rule_sequence", [Tree("selector_sequence", [Tree("range_selectors", [Tree("weekday_or_holiday_sequence_selector", [Tree("weekday_sequence", [Tree("weekday_range", [Token("WDAY", 'Mo'), Token("WDAY", 'Su')])])])]), Tree("time_selector", [Tree("timespan", [Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '10'), Token("TWO_DIGITS", '00')])]), Tree("time", [Tree("hour_minutes", [Token("TWO_DIGITS", '19'), Token("TWO_DIGITS", '00')])])])])])])])
}
