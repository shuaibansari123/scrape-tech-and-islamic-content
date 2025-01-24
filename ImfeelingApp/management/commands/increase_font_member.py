
from django.core.management.base import BaseCommand
from ImfeelingApp.models import FamilyMember  # Adjust the import based on your model
from django.utils.html import format_html

class Command(BaseCommand):
    help = 'Increase font size of content field in CKEditor'

    def handle(self, *args, **kwargs):
        members = FamilyMember.objects.all()  # Fetch all members
        for member in members:
            new_content  = f"""
                    <div style="padding: 20px; border-radius: 8px; font-family: 'Noto Nastaliq Urdu', serif; font-size: 20px; color: #333;">
                        {member.content}
                    </div>
                    """
            member.content = new_content
            member.save()  # Save the updated member
            self.stdout.write(self.style.SUCCESS(f'Updated member: {member.id}'))

        self.stdout.write(self.style.SUCCESS('Font size updated for all members.'))