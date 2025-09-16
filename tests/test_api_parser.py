import pytest

from src.api_parser import HeadHunterAPI


@pytest.fixture
def vacancy1():
    return [
        {
            "id": "125316609",
            "premium": False,
            "name": "Преподаватель по Frontend-программированию",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "2778", "name": "Самарканд", "url": "https://api.hh.ru/areas/2778"},
            "salary": {"from": 5000000, "to": 10000000, "currency": "UZS", "gross": False},
            "salary_range": {
                "from": 5000000,
                "to": 10000000,
                "currency": "UZS",
                "gross": False,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": {"id": "MONTHLY", "name": "Раз в\xa0месяц"},
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Самаркандский район",
                "street": "махаллинский сход граждан Хожа Ахрор Валий," " улица Зарафшон",
                "building": "519",
                "lat": 39.614882,
                "lng": 66.959855,
                "description": None,
                "raw": "Самаркандский район,"
                " махаллинский "
                "сход граждан Хожа"
                " Ахрор Валий, улица"
                " Зарафшон, 519",
                "metro": None,
                "metro_stations": [],
                "id": "19514743",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-09-15T10:21:44+0300",
            "created_at": "2025-09-15T10:21:44+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125316609",
            "show_logo_in_search": None,
            "show_contacts": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/125316609?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/125316609",
            "relations": [],
            "employer": {
                "id": "10483250",
                "name": "НОУ BUYUK AVLOD AKADEMIYASI",
                "url": "https://api.hh.ru/employers/10483250",
                "alternate_url": "https://hh.ru/employer/10483250",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1270716.png",
                    "90": "https://img.hhcdn.ru/employer-logo/6703174.png",
                    "240": "https://img.hhcdn.ru/employer-logo/6703175.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10483250",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Опыт работы во Frontend-разработке от 1–2 лет. Знание HTML5, CSS3,"
                " JavaScript (ES6+), желательно знание...",
                "responsibility": "Преподавание курсов по Frontend-разработке (HTML, CSS, JavaScript,"
                " базовые фреймворки). Подготовка учебных материалов и практических"
                " заданий для учеников. ",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [
                {"id": "from_four_to_six_hours_in_a_day", "name": "Можно сменами по\xa04-6\xa0часов в\xa0день"}
            ],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [
                {"id": "HOURS_2", "name": "2\xa0часа"},
                {"id": "HOURS_4", "name": "4\xa0часа"},
                {"id": "HOURS_6", "name": "6\xa0часов"},
                {"id": "HOURS_8", "name": "8\xa0часов"},
                {"id": "HOURS_10", "name": "10\xa0часов"},
            ],
            "work_schedule_by_days": [{"id": "THREE_ON_THREE_OFF", "name": "3/3"}, {"id": "OTHER", "name": "Другое"}],
            "night_shifts": False,
            "professional_roles": [{"id": "132", "name": "Учитель, преподаватель, педагог"}],
            "accept_incomplete_resumes": True,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "part", "name": "Частичная занятость"},
            "employment_form": {"id": "PART", "name": "Частичная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]


def test_hh_api(vacancy1) -> None:
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python")
    assert hh_vacancies == vacancy1
