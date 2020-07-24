# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'test'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, help='执行动作')
        parser.add_argument('-u', required=False, help='账户名称')
        parser.add_argument('-p', required=False, help='账户密码')
        parser.add_argument('-n', required=False, help='账户昵称')
        parser.add_argument('-s', default=False, action='store_true', help='是否是超级用户（默认否）')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('ok action= %s, -u=%s' % (options['action'], options['u'])))
        self.stdout.write("hello")

