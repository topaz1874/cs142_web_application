import os
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'web_site.settings')
import django
django.setup()

from photo_sharing.models import User, Photo, Comments
from datetime import datetime

def populate():
    jb = add_user(first_name='Justin', last_name='Bieber')
    ph = add_user(first_name='Paris', last_name='Hilton')
    mc = add_user(first_name='Miley', last_name='Cyrus')
    bo = add_user(first_name='Barack', last_name='Obama')
    sc = add_user(first_name='Santa', last_name='Claus')
    jo = add_user(first_name='John', last_name='Ousterhout')

    photo1 = add_photo(file_name='ouster.jpg', date_time='2012-08-30 10:44:23', user=jo)
    photo2 = add_photo(file_name='bieber1.jpg', date_time='2009-09-13 20:00:00', user=jb)
    photo3 = add_photo(file_name='bieber2.jpg', date_time='2009-09-13 20:05:03', user=jb)
    photo4 = add_photo(file_name='hilton1.jpg', date_time='2013-11-18 18:02:00', user=ph)
    photo5 = add_photo(file_name='hilton2.jpg', date_time='2013-09-20 17:30:00', user=ph)
    photo6 = add_photo(file_name='obama1.jpg', date_time='2009-07-10 16:02:49', user=bo)
    photo7 = add_photo(file_name='obama2.jpg', date_time='2010-08-30 14:26:00', user=bo)
    photo8 = add_photo(file_name='obama3.jpg', date_time='2010-03-18 23:47:00', user=bo)
    photo9 = add_photo(file_name='cyrus1.jpg', date_time='2013-12-03 09:02:00', user=mc)
    photo10 = add_photo(file_name='cyrus2.jpg', date_time='2013-12-03 09:03:02', user=mc)
    photo11 = add_photo(file_name='santa1.jpg', date_time='2013-09-04 09:16:03', user=sc)
    photo12 = add_photo(file_name='obama4.jpg', date_time='2013-10-16 17:12:28', user=bo)

    add_comment(comment="Learning new programming languages is hard...",
     date_time="2012-09-02 14:01:00", user=jo, photo=photo1)



def add_user(first_name, last_name):
    u = User.objects.get_or_create(first_name=first_name, last_name=last_name)[0]
    return u

def add_photo(user, file_name, date_time):
    p = Photo.objects.get_or_create(file_name=file_name, user=user)[0]
    p.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    # p.date_time = date_time
    p.save()
    return p

def add_comment(user, photo, comment, date_time):
    c = Comments.objects.get_or_create(comment=comment, user=user, photo=photo)[0]
    c.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    return c

if __name__ == '__main__':
    print "Starting populate data..."
    populate()

