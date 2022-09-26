from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MainPageTemplateView(TemplateView):
    template_name = "main/main.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageTemplateView, self).get_context_data(**kwargs)
        context["name"] = "Песчанский Дмитрий"
        context["age"] = "16 лет"
        context["education"] = "Школа(11 класс)"
        context["town"] = "Одинцово"
        context["github_link"] = "https://github.com/M1steryO?tab=repositories"
        context["telegram_link"] = "https://t.me/m1stery0"
        context["discord_link"] = "https://discordapp.com/users/%D0%9C%D0%B8%D1%81%D1%82%D0%B5%D1%80%D0%B8#4134"
        context["about_me"] = "Здравствуйте, меня зовут Дима. Я из прекрасного города – Одинцово. Сейчас я учусь в 11 " \
                              "классе и упорно готовлюсь к ЕГЭ. Кроме занятий по разработке, активно занимаюсь " \
                              "изучением английского языка, а также хожу в тренажерный зал. "
        context["experience_text"] = "Занимаюсь разработкой на Python с конца 2020 года. Прошел много курсов на площадках " \
                                 "Coursera и Stepik. Делал небольшие проекты на Flask, также писал Telegram-ботов. " \
                                 "Пробовал работать с docker и размещать проекты на Heroku. Также с 21-22 год " \
                                 "обучался в IT школе Samsung, изучал Java для разработки мобильных приложений, " \
                                 "стал победителем в региональном туре (на площадке), но финал пройти не удалось. " \
                                 "Очень хочу связать свою будущую жизнь с IT, так как весь процесс разработки, " \
                                 "с этапа задумки до деплоя его на сервер, невероятно интересен для меня. "
        context["experience_num"] = "1,5 года"
        return context
