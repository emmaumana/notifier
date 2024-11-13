from dataclasses import dataclass
from enums.support_requests import Channel, Topic

@dataclass(frozen=True)
class SupportRequestDto:
    topic: Topic
    description: str
    receiver: str

    def get_channel(self) -> Channel:
        if self.topic == Topic.SALES:
            return Channel.SLACK
        elif self.topic == Topic.PRICING:
            return Channel.EMAIL
        else:
            raise ValueError("Invalid topic")