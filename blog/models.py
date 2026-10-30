from encodings.punycode import T
from unicodedata import category
from venv import create

from django.db import models


class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  email = models.CharField(max_length=255, null = True,blank=True)
  password = models.CharField(max_length=255,null=True,blank=True)
  role = models.CharField(max_length=100,null=True,blank=True)
  created_at =models.DateTimeField(auto_now_add=True)


  class Meta:
    db_table = 'users'

    
  def str(self):
    return str(self.name)
  

class Category(models.Model):
  category_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  description = models.CharField(max_length=255,null=True,blank=True)
  created_at=models.DateTimeField(auto_now_add=True)


  class Meta:
    db_table ='category'

  def str(self):
    return str(self.name)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'post'

    def __str__(self):
        return str(self.title)

# class Post(models.Model):
#   post_id = models.AutoField(primary_key=True)
#   title = models.CharField(max_length=150)
#   content = models.TextField(default='')
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#   user = models.ForeignKey(User,on_delete=models.CASCADE)
#   category = models.ForeignKey(Category,on_delete=models.CASCADE)

#   class Meta:
#     db_table ='post'


#   def str(self):
#     return str(self.title)


class CommentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=CommentStatus.choices,
        default=CommentStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    # for user_id foreign key
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            db_column='user_id'
        )

    # for post_id foreign key
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        db_column='post_id', 
    )

    class Meta:
        db_table = 'comments'

    def str(self):
        return f"Comment {self.comment_id} - Status: {self.status}"

# for userProfile table

class ProfileVisibility(models.TextChoices):
    PUBLIC = 'public', 'Public'
    PRIVATE = 'private', 'Private'
class UserProfile(models.Model):
   profile_id = models.AutoField(primary_key=True)
   phone = models.CharField(max_length=20)
   address = models.CharField(max_length=255,null=True,blank=True)
   bio = models.TextField(null=True,blank=True)

   visibility = models.CharField(
        max_length=20,
        choices=ProfileVisibility.choices,
        default=ProfileVisibility.PUBLIC,
        db_index=True
    )

   
  # for user_id foreign key
   user = models.ForeignKey(
             User,
             on_delete=models.CASCADE,
             db_column='user_id'
         ) 
   class Meta:
      db_table = 'user_profiles'
   def str(self):
      return f"Profile {self.profile_id} - User ID: {self.user_id}"



class TagType(models.TextChoices):
    PROGRAMMING = 'programming', 'Programming'
    DESIGN = 'design', 'Design'
    BUSINESS = 'business', 'Business'
    OTHER = 'other', 'Other'
# create Tag table
class Tag(models.Model):
   tag_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)

   tag_type = models.CharField(
        max_length=50,
        choices=TagType.choices,
        default=TagType.OTHER,
        db_index=True)
   created_at = models.DateTimeField(auto_now_add=True)


   class Meta:
    db_table = 'tags'
   def str(self):
      return str(self.name)


# create PostTag table
class PostTag(models.Model):
   post_tag_id = models.AutoField(primary_key=True)
   post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        db_column='post_id',
        related_name='post_tags'
    )
    
    # tag_id (FK -> Tag.tag_id)
   tag = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
        db_column='tag_id',
        related_name='post_tags'
    )
   class Meta:
        db_table = 'post_tags'
        unique_together = ('post', 'tag')

   def str(self):
        return f"Post {self.post_id} - Tag {self.tag_id}"

class PostLike(models.Model):
    # like_id (PK, auto-increment)
    like_id = models.AutoField(primary_key=True)
    
    # created_at (datetime)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # user_id (FK -> User.user_id)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='post_likes'
    )
    
    # post_id (FK -> Post.post_id)
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        db_column='post_id',
        related_name='likes'
    )

    class Meta:
        db_table = 'post_likes'
        unique_together = ('user', 'post')

    def str(self):
        return f"User {self.user_id} liked Post {self.post_id}"