import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Cria ou atualiza um superusuário usando variáveis de ambiente."

    def handle(self, *args, **options):
        username = os.getenv("ADMIN_USERNAME", "").strip()
        email = os.getenv("ADMIN_EMAIL", "").strip()
        password = os.getenv("ADMIN_PASSWORD", "").strip()

        if not username or not password:
            self.stdout.write(self.style.WARNING(
                "ADMIN_USERNAME e ADMIN_PASSWORD não definidos. Pulando bootstrap do admin."
            ))
            return

        User = get_user_model()
        user = User.objects.filter(username=username).first()

        if user:
            if email:
                user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superusuário '{username}' atualizado com sucesso."))
            return

        User.objects.create_superuser(
            username=username,
            email=email or "",
            password=password,
        )
        self.stdout.write(self.style.SUCCESS(f"Superusuário '{username}' criado com sucesso."))
