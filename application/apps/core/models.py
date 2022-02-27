
from django.utils import timezone
from django.db.models import fields as django_fields
from django.db import models as django_models
from enum import Enum
from orm_converter.tortoise_to_django import ConvertedModel, RedefinedAttributes
from tortoise import Tortoise, fields
from tortoise.models import Model


class TherapistType(Enum):
    UNEXPERIENCED = "Початківець"
    EXPERIENCED = "Спеціаліст"
    UNVERIFIED = "Неверифіковано як спеціаліста"
    
class UserSex(Enum):
    MALE = "Чоловіча"
    FEMALE = "Жіноча"
    OTHER = "Жоден з варіантів (інше)"
    NO_DATA = "Не бажаю вказувати"

class TherapistPreferredSex(Enum):
    MALE = "Чоловіча"
    FEMALE = "Жіноча"
    OTHER = "Жоден з варіантів (інше)"
    NO_DATA = "Не має значення"

class TherapistPreferredType(Enum):
    UNEXPERIENCED = "Початківець"
    EXPERIENCED = "Спеціаліст"

class ClosureReason(Enum):
    REJECTION = "Відмова"
    FAILURE = "Неуспішне закриття"
    SUCCESS = "Успішне закриття"


class TelegramUser(Model, ConvertedModel):
    tg_id = fields.BigIntField(unique=True, description="Telegram - User ID")
    chat_id = fields.BigIntField(unique=False, description="Telegram - Chat ID")
    first_name = fields.CharField(max_length=64, description="Telegram - ім'я профілю")
    therapist_type = fields.CharEnumField(enum_type=TherapistType, default=TherapistType.UNVERIFIED, description="Статус спеціаліста")
    user_sex = fields.CharEnumField(enum_type=UserSex, default=UserSex.NO_DATA, description="Стать")
    user_age = fields.SmallIntField(description="Вік", null=True, blank=True)
    user_preferred_name = fields.CharField(max_length=64, description="Як звертатися", null=True, blank=True)
    user_contact_data = fields.CharField(max_length=64, description="Контактні дані", null=True, blank=True)

    is_therapist = fields.BooleanField(description="Спеціаліст?", null=True, blank=True)
    is_ready_for_clients = fields.BooleanField(description="Готові до кліентів?", null=True, blank=True)
    therapist_themes = fields.TextField(description="Теми спеціаліста", null=True, blank=True)
    therapist_other_data = fields.TextField(description="Спеціаліст - інше", null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.first_name} - {self.tg_id}"

    class Meta:
        table = "user"

    class RedefinedAttributes(RedefinedAttributes):
        class DjangoTherapistType(django_models.TextChoices):
            UNEXPERIENCED = "Початківець"
            EXPERIENCED = "Спеціаліст"
            UNVERIFIED = "Неверифіковано як спеціаліста"

        class DjangoUserSex(django_models.TextChoices):
            MALE = "Чоловіча"
            FEMALE = "Жіноча"
            OTHER = "Жоден з варіантів (інше)"
            NO_DATA = "Не бажаю вказувати"

        therapist_type = django_fields.CharField(choices=DjangoTherapistType.choices, default=DjangoTherapistType.UNVERIFIED, max_length=150)
        user_sex = django_fields.CharField(choices=DjangoUserSex.choices, default=DjangoUserSex.NO_DATA, max_length=150)

class HelpRequest(Model, ConvertedModel):
    user = fields.ForeignKeyField(model_name='core.TelegramUser', related_name="requests")
    therapist = fields.ForeignKeyField(model_name='core.TelegramUser', related_name="therapist_requests", null=True)
    is_open = fields.BooleanField(default=True)
    date_created = fields.DatetimeField(default=timezone.now)
    status_description = fields.TextField(description="Опис ситуації", null=True, blank=True)
    therapist_preferred_sex = fields.CharEnumField(enum_type=TherapistPreferredSex, default=TherapistPreferredSex.NO_DATA, description="Бажана стать терапевта")
    therapist_preferred_type = fields.CharEnumField(enum_type=TherapistPreferredType, default=TherapistPreferredType.UNEXPERIENCED, description="Стать")
    request_type = fields.CharField(null=True, blank=True, max_length=512)
    closure_status = fields.CharEnumField(enum_type=ClosureReason, null=True, blank=True, max_length=150)
    failure_closure_reason = fields.TextField(description="Спеціаліст - причина закриття заявки", null=True, blank=True)
    therapist_feedback = fields.TextField(description="Спеціаліст - фідбек на заявку", null=True, blank=True)

    class RedefinedAttributes(RedefinedAttributes):
        class DjangoTherapistPreferredSex(django_models.TextChoices):
            MALE = "Чоловіча"
            FEMALE = "Жіноча"
            OTHER = "Жоден з варіантів (інше)"
            NO_DATA = "Не має значення"

        class DjangoTherapistPreferredType(django_models.TextChoices):
            UNEXPERIENCED = "Початківець"
            EXPERIENCED = "Спеціаліст"

        class DjangoClosureReason(django_models.TextChoices):
            REJECTION = "Відмова"
            FAILURE = "Неуспішне закриття"
            SUCCESS = "Успішне закриття"

        therapist_preferred_sex = django_fields.CharField(choices=DjangoTherapistPreferredSex.choices, default=DjangoTherapistPreferredSex.NO_DATA, max_length=150)
        therapist_preferred_type = django_fields.CharField(choices=DjangoTherapistPreferredType.choices, default=DjangoTherapistPreferredType.UNEXPERIENCED, max_length=150)
        closure_status = django_fields.CharField(choices=DjangoClosureReason.choices, null=True, blank=True, max_length=150)

    def __str__(self) -> str:
        return f"{self.date_created} - {self.tg_id}"

    class Meta:
        table = "help_request"


def register_models() -> None:
    Tortoise.init_models(
        models_paths=["apps.core.models"],
        app_label="core",
        _init_relations=False,
    )
