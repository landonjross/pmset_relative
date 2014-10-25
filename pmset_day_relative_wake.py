import datetime
import argparse
import os

program_description = 'Schedule day-relative pmset wake event.'
parser = argparse.ArgumentParser(description=program_description)
parser.add_argument('--day_shift', type=int)
parser.add_argument('--hour', type=int)
parser.add_argument('--minute', type=int)
args = parser.parse_args()

now = datetime.datetime.now()
schedule_date = now + datetime.timedelta(days=args.day_shift)
schedule = datetime.datetime(year=schedule_date.year,
                             month=schedule_date.month,
                             day=schedule_date.day,
                             hour=args.hour,
                             minute=args.minute)
pmset_date = schedule.strftime('"%m/%d/%y %H:%M:%S"')
os.system('pmset schedule wake %s' % pmset_date)
