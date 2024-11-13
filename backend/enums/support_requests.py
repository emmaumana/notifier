from enum import Enum

class Topic(Enum):
    SALES = 'sales'
    PRICING = 'pricing'

class Channel(Enum):
    SLACK = 'slack'
    EMAIL = 'email'
