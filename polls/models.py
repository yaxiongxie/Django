from __future__ import unicode_literals

from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     question_body = models.TextField(max_length=300, default='')
#     question_image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
#
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.country_name


class Subway(models.Model):
    subway_name = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.subway_name


class OfficeBuilding(models.Model):
    title = models.CharField(max_length=200)
    rent_price = models.IntegerField()
    sale_price = models.IntegerField()
    seats = models.IntegerField()
    decoration = models.CharField(max_length=200)
    userTime = models.CharField(max_length=200)
    floorNum = models.IntegerField()
    priceInclude = models.CharField(max_length=200)
    totalArea = models.IntegerField()
    blockNum = models.IntegerField()
    carNum = models.IntegerField()
    level = models.IntegerField()
    floorHeight = models.IntegerField()
    elevatorNum = models.IntegerField()
    propertyCompany = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    subway = models.ForeignKey(Subway, on_delete=models.CASCADE)
    createTime = models.DateTimeField('date published')
    buildTime = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s' % self.title


class RoomType(models.Model):
    room_type = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.room_type


class RoomDirection(models.Model):
    room_direction = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.room_direction


class Rent(models.Model):
    title = models.CharField(max_length=200)
    address =   models.CharField(max_length=200)
    price = models.IntegerField()
    area = models.IntegerField()
    subway = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    rentType = models.CharField(max_length=200)
    payType = models.CharField(max_length=200)
    currentStatus = models.CharField(max_length=200)
    heatingType = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    subway = models.ForeignKey(Subway, on_delete=models.CASCADE)
    roomType = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    roomDirection = models.ForeignKey(RoomDirection, on_delete=models.CASCADE)
    createTime = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s' % self.title
