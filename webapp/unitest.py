from datetime import datetime, timedelta
import unittest
from webapp import app, Series, Episode, Skill, Available, follow
from webapp import User, Post, Lesson, db, Comment, likes, Upload
from flask import jsonify
import psycopg2

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@qwerty1234!@localhost/postgres'
        db.drop_all()
        db.create_all()

    def test_functions(self):
        u1 = User(role=2,username='john', password='thisatest',   fullname='John Oula',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="johnoula@icloud.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u2 = User(role=1,username='eliora', password='thisisatest',fullname='Eliora Kwa',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest2@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u3 = User(role=0,username='kemal', password='thisisatest',fullname='Kemal ',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest3@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u4 = User(role=0,username='maggie', password='thisisatest', fullname='Maggie Ma',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest4@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u5 = User(role=0,username='linda', password='thisisatest', fullname='Linda',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest5@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u6 = User(role=0,username='keely', password='thisisatest', fullname='Keely',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest6@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u7 = User(role=0,username='jony', password='thisisatest', fullname='Jony',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest7@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u8 = User(role=0,username='cici', password='thisisatest', fullname='Cici',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest8@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        u9 = User(role=0,username='nued', password='thisisatest', fullname='Nued',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest9@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(u4)
        db.session.add(u5)
        db.session.add(u6)
        db.session.add(u7)
        db.session.add(u8)
        db.session.add(u9)
        db.session.commit()
        user_list=User.query.all()

        p1 = Post(user_id=1, title='tech', description='this is a test ',category='MANDARIN', date='2019-12-4')
        p2 = Post(user_id=2, title='china', description='this is a test', category="CAREER", date='2019-12-3')
        p3 = Post(user_id=3, title='biz', description='this is a test', category="LEGAL", date='2019-12-2')
        p4 = Post(user_id=4, title='living', description='this is a test', category="BUSINESS", date='2019-12-1')
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.commit()

        pages = Post.query.paginate(per_page=1)
        print(pages)

        l1 = Lesson(title='Introduction', description="this is a test", post_id=1, user_id=1)
        l2 = Lesson(title='Introduction II', description="this is a test", post_id=1, user_id=1)
        l3 = Lesson(title='Introduction III', description="this is a test", post_id=1, user_id=2)
        l4 = Lesson(title='Introduction', description="this is a test", post_id=4, user_id=4)

        db.session.add(l1)
        db.session.add(l2)
        db.session.add(l3)
        db.session.add(l4)
        db.session.commit()

        up1 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=1)
        up2 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=2)
        up3 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=2)
        up4 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=3)
        up5 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=3)
        up6 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=4)
        up7 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=4)
        up8 = Upload(title = 'funcionality',upload_ref='e4ddb88bfcfe5661.mp4',user_id=1)
        c1 = Comment(content = 'This is just a test.This is for the funcionality',user_id=1,upload_id=1)
        c2 = Comment(content = 'This is just a test.This is for the funcionality',user_id=2,upload_id=1)
        c3 = Comment(content = 'This is just a test.This is for the funcionality',user_id=3,upload_id=1)
        c4 = Comment(content = 'This is just a test.This is for the funcionality',user_id=4,upload_id=1)
        db.session.add(up1)
        db.session.add(up2)
        db.session.add(up3)
        db.session.add(up4)
        db.session.add(up5)
        db.session.add(up6)
        db.session.add(up7)
        db.session.add(up8)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.commit()

        s1 = Series(user_id=1, title='tech', description='this is a test ', category='MANDARIN', timestamp='2019-12-4')
        db.session.add(s1)
        db.session.commit()

        e1 = Episode(user_id=1, subtitle='subtitle=tech', description='this is a test ',upload_ref='c66bc66048db6fb0.mp4' , series_id=1,timestamp='2019-12-4')
        e2 = Episode(user_id=1, subtitle='tech', description='this is a test ',upload_ref='c66bc66048db6fb0.mp4' , series_id=1,timestamp='2019-12-4')
        e3 = Episode(user_id=1, subtitle='ech', description='this is a test ',upload_ref='c66bc66048db6fb0.mp4' ,series_id=1, timestamp='2019-12-4')
        e4 = Episode(user_id=1, subtitle='suble=tech', description='this is a test ',upload_ref='c66bc66048db6fb0.mp4' , series_id=1,timestamp='2019-12-4')
        db.session.add(e1)
        db.session.add(e2)
        db.session.add(e3)
        db.session.add(e4)
        db.session.commit()

        skill1 = Skill(skill_title='autoCad')
        skill2 = Skill(skill_title='business')
        skill3 = Skill(skill_title='education')
        skill4 = Skill(skill_title='painting')
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(skill3)
        db.session.add(skill4)

        skill1.user.append(u1)
        skill2.user.append(u3)
        skill3.user.append(u1)
        skill4.user.append(u2)
        for skill in u1.skill:
            print("User 1 is skilled in",skill.skill_title)
        db.session.commit()


        date1 = Available(date_available='2019-03-10')
        date2 = Available(date_available='2019-03-21')
        date3 = Available(date_available='2019-04-15')
        date4 = Available(date_available='2019-04-15')
        db.session.add(date1)
        db.session.add(date2)
        db.session.add(date3)
        db.session.add(date4)

        date1.user.append(u1)
        date2.user.append(u3)
        date3.user.append(u1)
        date4.user.append(u2)
        for date in u1.available and u2.available:
            print("User ",u1.id," is available on",date.date_available)
        db.session.commit()

        posts = Post.query.all()
#        for lesson in p1.lesson:
#            print(lesson.title)
#
#            if lesson.post_id == p4.id:
#                print(lesson.title)
#            else:
#                pass
        posts = Post.query.all()
#        for post in u1.lesson:
#            if post.post_id == p2.id:
#
#                print(post.title)
#            else:
#                pass
#
#        print(l1.lessons.title)
        p1.bookers.append(u1)
        p2.bookers.append(u3)
        p4.bookers.append(u1)
        p3.bookers.append(u2)
        up1.user_cart.append(u1)
        up1.user_cart.append(u2)
        up2.user_cart.append(u2)
        db.session.commit()


        u1.followed.append(u4)
        u1.followed.append(u3)
        u1.followed.append(u2)
        u2.followed.append(u8)
        u3.followed.append(u8)
        u3.followed.append(u1)
        db.session.commit()
        u2.followers.count()
        assert u2.followers.count() == 1
        count = 0
        for followers in u1.followed:

            print(u1.username," is followed by ",followers.username)
            count += count
        print(count)




        user = User.query.all()

#        for posts in u2.book:
#            print(u2.username,'has','booked',posts.title,'session','on',posts.date)
#
#        for created_posts in u2.posts:
#            print(created_posts.title, created_posts.category)

        author1 = p1.author.username
        author2 = p4.author.username
        #       join=Post.query.join(user, (id == p1.user_id))
        #       print(join)
        print(author1, 'created session titled')
#        for episodes in s1.episode:
#            print(episodes.subtitle)
#
#        ep = e1.sub.title
#
#        print(ep)
  # setup the followers
        up1 = u1.followed_uploads().all()
        # check the followed posts of each user
        f1 = u1.followed_posts()

        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()


        def update():
            f = u3.followed_posts().all()
            for i in f:
                print(type(i))

                posts = [i]
                final = posts.append(i)
                print(final)
            return print(final)
        pass
        update()
        print(u1.get_reset_token())

#        print(len(up1))
#        print(len(f2))
#        print(len(f3))
#        print(len(f4))
#        assert len(f1) == 4
#        assert len(f2) == 2
#        assert len(f3) == 2
#        assert len(f4) == 1
#        assert f1 == [p4, p3, p2,p1]
#        assert f2 == [p4, p2]
#        assert f3 == [p3, p2]
#        assert f4 == [p4]


if __name__ == '__main__':
    unittest.main(verbosity=2)