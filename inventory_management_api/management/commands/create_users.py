from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create initial users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
            self.stdout.write("Test user created.")
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin', password='adminpass', email='admin@example.com')
            self.stdout.write("Admin user created.")
