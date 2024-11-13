from dataclasses import dataclass

@dataclass
class SupportRequestEmailValueObject:
    topic: str
    message: str
    receiver: str