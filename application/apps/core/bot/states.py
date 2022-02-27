from aiogram.dispatcher.filters.state import State, StatesGroup

class TherapistRegistration(StatesGroup):
    name = State()
    sex = State()
    themes = State()
    contact = State()
    other_data = State()

class TherapistSelection(StatesGroup):
    view_request = State()
    take_request = State()


class TherapistClosure(StatesGroup):
    view_requests = State()
    close_request = State()
    rejection_procesing = State()
    failure_processing = State()
    success_processing = State()
    additional_consultation = State()

class ClientRequest(StatesGroup):
    issue_type_selection = State()
    situation_description = State()
    specialist_sex_selection = State()
    specialist_quality_selection = State()
    name_set = State()
    age_set = State()
    sex_set = State()
    contact_set = State()
