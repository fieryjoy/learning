from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, 
                        String, Table,
                        Text, Sequence)
from sqlalchemy.orm import (sessionmaker, relationship, 
                            aliased, subqueryload, 
                            joinedload, contains_eager, 
                            validates)
from sqlalchemy.sql import func, exists

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


post_keywords = Table('post_keywords', Base.metadata,
                    Column('post_id', ForeignKey('posts.id'), primary_key=True),
                    Column('keyword_id', ForeignKey('keywords.id'), primary_key=True))


# one user many addresses
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    addresses = relationship("Address", 
                                back_populates="user", 
                                cascade="all, delete, delete-orphan")

    posts = relationship("BlogPost",
                            back_populates="author", lazy="dynamic")

    @validates('addresses')
    def validate_address(self, key, address):
        assert '@' in address.email_address
        return address
    
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User",
                             back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

# many to many relationship
class BlogPost(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=False)
    body = Column(Text)
    author = relationship(User, 
                            back_populates="posts")

    # many to many BlogPost <-> Keyword
    keywords = relationship('Keyword', 
                            secondary=post_keywords, 
                            back_populates='posts')

    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body

    def __repr__(self):
        return "BlogPost(%r, %r, %r)" % (self.headline, self.body, self.author)

    
class Keyword(Base):
    __tablename__ = 'keywords'
    
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)
    posts = relationship('BlogPost', 
                            secondary=post_keywords, 
                            back_populates='keywords')

    def __init__(self, keyword):
        self.keyword = keyword


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.commit()

    session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])

    session.commit()

    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)

    for name, fullname in session.query(User.name, User.fullname):
        print(name, fullname)

    for row in session.query(User, User.name).all():
        print(row.User, row.name)

    jack = User(name='jack', fullname='Jack Bean', password='giffdd')
    print jack.addresses

    jack.addresses = [
        Address(email_address='jack@google.com'),
        Address(email_address='j25@yahoo.com')]

    print jack.addresses[1]
    session.add(jack)
    session.commit()
    print jack.addresses

    print
    for u, a in session.query(User, Address).filter(User.id == Address.user_id).filter(Address.email_address=='jack@google.com').all():
        print u
        print a

    print
    for u in session.query(User).join(Address).filter(Address.email_address.like('%.com%')).all():
        print u

    adalias1 = aliased(Address)
    adalias2 = aliased(Address)
    for username, email1, email2 in \
            session.query(User.name, adalias1.email_address, adalias2.email_address).\
            join(adalias1, User.addresses).\
            join(adalias2, User.addresses).\
            filter(adalias1.email_address=='jack@google.com').\
            filter(adalias2.email_address=='j25@yahoo.com'):
        print(username, email1, email2)

    stmt = session.query(Address.user_id, func.count('*').label('address_count')).group_by(Address.user_id).subquery()
    for u, count in session.query(User, stmt.c.address_count).\
                            outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id):
        print(u, count)

    stmt = session.query(Address).filter(Address.email_address != 'j25@yahoo.com').subquery()
    adalias = aliased(Address, stmt)
    for user, address in session.query(User, adalias).join(adalias, User.addresses):
        print user
        print address

    stmt = exists().where(Address.user_id==User.id)
    for name, in session.query(User.name).filter(stmt):
        print name

    for name, in session.query(User.name).filter(User.addresses.any()):
        print name

    for name, in session.query(User.name).filter(User.addresses.any(Address.email_address.like('%google%'))):
        print name

    print session.query(Address).filter(~Address.user.has(User.name=='jack')).all()
    
    jack = session.query(User).options(subqueryload(User.addresses)).filter_by(name='jack').one()
    print jack
    
    jack = session.query(User).options(joinedload(User.addresses)).filter_by(name='jack').one()
    print jack
    
    jacks_addresses = session.query(Address).join(Address.user).\
                                filter(User.name=='jack').\
                                options(contains_eager(Address.user)).\
                                all()
    print jacks_addresses
    print jacks_addresses[0].user

    session.delete(jack)
    print session.query(User).filter_by(name='jack').count()

    print session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).count()

    wendy = session.query(User).filter_by(name='wendy').one()
    post = BlogPost("Wendy's Blog Post", "This is a test", wendy)
    session.add(post)

    post.keywords.append(Keyword('wendy'))
    post.keywords.append(Keyword('firstpost'))

    print session.query(BlogPost).filter(BlogPost.keywords.any(keyword='firstpost')).all()
    print wendy.posts.filter(BlogPost.keywords.any(keyword='firstpost')).all()
