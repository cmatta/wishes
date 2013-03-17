from peewee import *
import csv
import logging
from dateutil.parser import *
from dateutil.tz import *
import pprint

TZOFFSETS = {"PDT": -25200}

pp = pprint.PrettyPrinter(indent=4)

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)

db = SqliteDatabase('frontend/wishes.db')
db.connect()

class BaseModel(Model):

  class Meta:
    database = db

class Wish(BaseModel):
  HitId = CharField()
  HitTitle = CharField()
  Annotation = CharField(null=True)
  AssignmentId = CharField()
  WorkerId = CharField()
  Status = CharField()
  AcceptTime = DateTimeField()
  SubmitTime = DateTimeField()
  Wish = CharField()

def main():
  Wish.create_table(fail_silently=True)
  csv_file = "master_turk.csv"

  with open(csv_file, 'rb') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')

    for row in csv_reader:
      try:
        submit_date = parse(row['SubmitTime'], tzinfos=TZOFFSETS)
        accept_date = parse(row['AcceptTime'], tzinfos=TZOFFSETS)
        
        try:
          wish = Wish.create(HitId=row['HitId'],
                      HitTitle=row['HitTitle'],
                      Annotation=row['Annotation'],
                      AssignmentId=row['AssignmentId'],
                      WorkerId=row['WorkerId'],
                      Status=row['Status'],
                      AcceptTime=accept_date,
                      SubmitTime=submit_date,
                      Wish=row['Wish'])

        except Exception, e:
          logger.exception(e)
      except Exception, e:
        logger.exception(e)

if __name__ == '__main__':
  main()