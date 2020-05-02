from datetime import datetime, timedelta
import unittest
from webapp import app
from webapp.models import User, Post, Lesson, db, Comment, likes, Upload
from flask import jsonify
import psycopg2

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@qwerty1234!@localhost/postgres'
        db.drop_all()
        db.create_all()

    def test_functions(self):
        u1 = User(role=2,username='john', password='thisatest',   fullname='John Oula',id_type='Passport',id_number='AK0123545',nationality='American',occupation='Engineer',email="thisisatest1@gmail.com",province='Jiangsu',city='Nanjing',phone='133023545797')
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

        p1 = Post(user_id=1, title='tech', description='this is a test ',category='MANDARIN', date='2019-12-4')
        p2 = Post(user_id=1, title='china', description='this is a test', category="CAREER", date='2019-12-3')
        p3 = Post(user_id=4, title='biz', description='this is a test', category="LEGAL", date='2019-12-2')
        p4 = Post(user_id=2, title='living', description='this is a test', category="BUSINESS", date='2019-12-1')
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.commit()

        l1 = Lesson(title='Introduction', description="this is a test", post_id=1, user_id=1)
        l2 = Lesson(title='Introduction II', description="this is a test", post_id=1, user_id=1)
        l3 = Lesson(title='Introduction III', description="this is a test", post_id=1, user_id=2)
        l4 = Lesson(title='Introduction', description="this is a test", post_id=4, user_id=4)

        db.session.add(l1)
        db.session.add(l2)
        db.session.add(l3)
        db.session.add(l4)
        db.session.commit()

        up1 = Upload(title = 'funcionality',user_id=1)
        c1 = Comment(content = 'This is just a test.This is for the funcionality',user_id=1,upload_id=1)
        c2 = Comment(content = 'This is just a test.This is for the funcionality',user_id=2,upload_id=1)
        c3 = Comment(content = 'This is just a test.This is for the funcionality',user_id=3,upload_id=1)
        c4 = Comment(content = 'This is just a test.This is for the funcionality',user_id=4,upload_id=1)
        db.session.add(up1)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.commit()





        posts = Post.query.all()
        for lesson in p1.lesson:
            print(lesson.title)

            if lesson.post_id == p4.id:
                print(lesson.title)
            else:
                pass
        posts = Post.query.all()
        for post in u1.lesson:
            if post.post_id == p2.id:

                print(post.title)
            else:
                pass

        print(l1.lessons.title)
        p1.bookers.append(u1)
        p2.bookers.append(u3)
        p4.bookers.append(u1)
        p3.bookers.append(u2)
        db.session.commit()

        user = User.query.all()

        for posts in u2.book:
            print(u2.username,'has','booked',posts.title,'session','on',posts.date)

        for created_posts in u2.posts:
            print(created_posts.title, created_posts.category)

        author1 = p1.author.username
        author2 = p4.author.username
        #       join=Post.query.join(user, (id == p1.user_id))
        #       print(join)
        print(author1, 'created session titled')
        print(author2)

db.drop_all()
if __name__ == '__main__':
    unittest.main(verbosity=2)