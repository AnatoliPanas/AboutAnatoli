from django.shortcuts import render
from django.http import HttpResponse

from api.users.models import Profile


def index(request):
    # Рендерим главный шаблон, указывая путь с учетом подпапки

    profile = Profile.objects.first()

    if not profile:
        profile = Profile(
            headline='Software Developer',
            description='Willkommen auf meiner Web-Visitenkarte. Ich spezialisiere mich auf Entwicklung, saubere Architektur (Clean Code) und das Design effizienter APIs.'
        )
        profile.owner_first_name = 'Anatoli'
        profile.owner_last_name = ''
    else:
        # Если профиль из базы найден и у него есть владелец, пробрасываем его имена
        if profile.owner:
            profile.owner_first_name = profile.owner.first_name
            profile.owner_last_name = profile.owner.last_name
        else:
            profile.owner_first_name = "Anatoli"
            profile.owner_last_name = ""

    return render(request, 'website/index.html', {'profile': profile})

def get_info(request):
    # Этот кусочек вернется асинхронно и заменит собой кнопку
    html = """
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 transition-all duration-300">
        <div class="flex items-center space-x-2 text-slate-300">⚡ Python / Django</div>
        <div class="flex items-center space-x-2 text-slate-300">🛡️ SOLID / Clean Code</div>
        <div class="flex items-center space-x-2 text-slate-300">🗄️ PostgreSQL / SQL</div>
        <div class="flex items-center space-x-2 text-slate-300">🐳 Docker</div>
        <div class="flex items-center space-x-2 text-slate-300">🤝 Project Leadership</div>
        <div class="flex items-center space-x-2 text-slate-300">📈 REST API Architecture</div>
    </div>
    """
    return HttpResponse(html)