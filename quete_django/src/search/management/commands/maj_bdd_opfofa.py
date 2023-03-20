from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Je ne peux pas t'aider désolé !"

    def handle(self, *args, **options):
        # Votre code pour la commande ici
        self.stdout.write(self.style.SUCCESS('Commande réussie'))