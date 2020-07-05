from django.core.management.base import BaseCommand
import feedparser
from ...models import News
from datetime import datetime
import logging

logger = logging.getLogger("error_log")


class Command(BaseCommand):
    help = 'Crawl Data.'

    def add_arguments(self, parser):
        # add arguments for command
        parser.add_argument('-src', '--sources', type=str)

    def handle(self, *args, **options):
        if not options['sources']:
            print("sources not found.")

        # split sources
        sources = str(options['sources']).split(",")
        for s in sources:
            feed = feedparser.parse(s)
            # get list item from RSS
            data = feed.entries
            for item in data:
                title = item.get("title")
                summary = item.get("summary")
                link = item.get("link")
                comment = item.get("comments")
                published = item.get("published")
                published = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z') if published else None

                # get or create objects
                n, created = News.objects.get_or_create(
                    title=title,
                    link=link,
                    defaults={
                        'summary': summary,
                        'comment': comment,
                        'published': published
                    },
                )

                if created:
                    print("{} Create new item -> {}({})".format(datetime.now(), title, link))
                else:
                    print("{} existed -> {}({})".format(datetime.now(), title, link))
