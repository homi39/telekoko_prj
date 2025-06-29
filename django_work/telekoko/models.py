from django.db import models
import uuid

class Group(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
  group_name = models.CharField(max_length=50, verbose_name="グループ名")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
  is_deleted = models.BooleanField(default=False, verbose_name="削除フラグ")
  
  def __str__(self):
        return self.group_name

class GroupUser(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
  group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name="グループID")
  user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="ユーザID")

  def __str__(self):
        return f"{self.group.name} ・ {self.user.name}"

class User(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
  name = models.CharField(max_length=50, verbose_name="名前")
  feeling = models.ForeignKey('Feeling',on_delete=models.PROTECT, verbose_name="気持ちID")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
  is_deleted = models.BooleanField(default=False, verbose_name="削除フラグ")

  def __str__(self):
      return self.name



class Feeling(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
  name = models.CharField(max_length=50, verbose_name="気持ち名")
  feeling_image = models.ImageField(upload_to="image", blank=True, verbose_name="気持ちイメージ", help_text="登録しない場合は、デフォルトの気持ちイメージを使用する")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
  is_deleted = models.BooleanField(default=False, verbose_name="削除フラグ")
  
  def __str__(self):
      return self.name




