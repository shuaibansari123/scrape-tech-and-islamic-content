from django.core.management.base import BaseCommand
from ImfeelingApp.models import ImFeeling

class Command(BaseCommand):
    help = 'Populate the ImFeeling model with predefined feelings'

    def handle(self, *args, **kwargs):
        feelings_data = [
            {"feeling_name": "Angry", "description": "Feeling of anger."},
            {"feeling_name": "Anxious", "description": "Feeling of anxiety."},
            {"feeling_name": "Bored", "description": "Feeling of boredom."},
            {"feeling_name": "Confident", "description": "Feeling of confidence."},
            {"feeling_name": "Confused", "description": "Feeling of confusion."},
            {"feeling_name": "Content", "description": "Feeling of contentment."},
            {"feeling_name": "Depressed", "description": "Feeling of depression."},
            {"feeling_name": "Doubtful", "description": "Feeling of doubt."},
            {"feeling_name": "Grateful", "description": "Feeling of gratitude."},
            {"feeling_name": "Greedy", "description": "Feeling of greed."},
            {"feeling_name": "Guilty", "description": "Feeling of guilt."},
            {"feeling_name": "Happy", "description": "Feeling of happiness."},
            {"feeling_name": "Hurt", "description": "Feeling of hurt."},
            {"feeling_name": "Hypocritical", "description": "Feeling of hypocrisy."},
            {"feeling_name": "Indecisive", "description": "Feeling of indecision."},
            {"feeling_name": "Jealous", "description": "Feeling of jealousy."},
            {"feeling_name": "Lazy", "description": "Feeling of laziness."},
            {"feeling_name": "Lonely", "description": "Feeling of loneliness."},
            {"feeling_name": "Lost", "description": "Feeling of being lost."},
            {"feeling_name": "Nervous", "description": "Feeling of nervousness."},
            {"feeling_name": "Overwhelmed", "description": "Feeling of being overwhelmed."},
            {"feeling_name": "Regret", "description": "Feeling of regret."},
            {"feeling_name": "Sad", "description": "Feeling of sadness."},
            {"feeling_name": "Scared", "description": "Feeling of fear."},
            {"feeling_name": "Suicidal", "description": "Feeling of suicidal thoughts."},
            {"feeling_name": "Tired", "description": "Feeling of tiredness."},
            {"feeling_name": "Unloved", "description": "Feeling of being unloved."},
            {"feeling_name": "Weak", "description": "Feeling of weakness."},
            {"feeling_name": "Anticipation", "description": "Feeling of anticipation."},
            {"feeling_name": "Aroused", "description": "Feeling of arousal."},
            {"feeling_name": "Curious", "description": "Feeling of curiosity."},
            {"feeling_name": "Defeated", "description": "Feeling of defeat."},
            {"feeling_name": "Desire", "description": "Feeling of desire."},
            {"feeling_name": "Desperate", "description": "Feeling of desperation."},
            {"feeling_name": "Determined", "description": "Feeling of determination."},
            {"feeling_name": "Disbelief", "description": "Feeling of disbelief."},
            {"feeling_name": "Envious", "description": "Feeling of envy."},
            {"feeling_name": "Hatred", "description": "Feeling of hatred."},
            {"feeling_name": "Humiliated", "description": "Feeling of humiliation."},
            {"feeling_name": "Impatient", "description": "Feeling of impatience."},
            {"feeling_name": "Insecure", "description": "Feeling of insecurity."},
            {"feeling_name": "Irritated", "description": "Feeling of irritation."},
            {"feeling_name": "Love", "description": "Feeling of love."},
            {"feeling_name": "Nostalgic", "description": "Feeling of nostalgia."},
            {"feeling_name": "Offended", "description": "Feeling of being offended."},
            {"feeling_name": "Peaceful", "description": "Feeling of peace."},
            {"feeling_name": "Rage", "description": "Feeling of rage."},
            {"feeling_name": "Satisfied", "description": "Feeling of satisfaction."},
            {"feeling_name": "Uncertain", "description": "Feeling of uncertainty."},
            {"feeling_name": "Uneasy", "description": "Feeling of unease."},
        ]

        for feeling in feelings_data:
            ImFeeling.objects.create(
                title=feeling["feeling_name"],
                body="",  # You can add default content or leave it empty
                feeling_name=feeling["feeling_name"],
                description=feeling["description"]
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated feelings!'))