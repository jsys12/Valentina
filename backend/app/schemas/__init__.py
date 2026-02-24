# === TypedDict ===
from .dicts import (
    ActivateQrCodeResult,
    EventCreatedResult,
    LoginUserResult,
    UserRegistrationResult,
)

# === Protocol ===
from .protocols.protocol_event import ManagementEventsProtocol

# === Pydantic ===
from .pydantics.routers.event import (
    AllElementsResponseDTO,
    CreateEventDTO,
    CreateEventResponseDTO,
    EditEventDTO,
    EditEventResponseDTO,
)


# === NewType ===
from .types.types_event import (
    IntEventCreatorId,
    StrEventAddress,
    StrEventDescription,
    StrEventTitle,
)
from .types.types_user import IntUserId, StrUserLogin, StrUserName, StrUserPassword

__all__ = [
    "UserRegistrationResult",
    "EventCreatedResult",
    "LoginUserResult",
    "LoginUserDTO",
    "CreateUserDTO",
    "CreateEventDTO",
    "EditEventDTO",
    "IntUserId",
    "StrUserName",
    "StrUserLogin",
    "StrUserPassword",
    "IntEventCreatorId",
    "StrEventAddress",
    "StrEventDescription",
    "StrEventTitle",
    "ManagementEventsProtocol",
    "ManagementUsersProtocol",
    "ManagementTicketTypeProtocol",
    "CreateTicketTypeDTO",
    "EditTicketTypeDTO",
    "CreateTicketTypeResponseDTO",
    "EditTicketTypeResponseDTO",
    "TicketCreateDTO",
    "TicketCreateResponseDTO",
    "ManagementTicketsProtocol",
    "GetUserInfoResponseDTO",
    "LoginUserResponseDTO",
    "CreateUserResponseDTO",
    "AllElementsResponseDTO",
    "CreateEventResponseDTO",
    "EditEventResponseDTO",
    "GetTicketTypesResponseDTO",
    "AllTicketsEventResponseDTO",
    "AllActiveTicketsEventResponseDTO",
    "ActivateQrCodeResult",
    "ActivateQrCodeResponseDTO",
]
