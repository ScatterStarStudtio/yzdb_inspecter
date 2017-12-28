# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models

from utils.common import getYzDefaultFmtDateTime

class SysAppUser(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rights = models.CharField(db_column='RIGHTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role_id = models.CharField(db_column='ROLE_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_login = models.CharField(db_column='LAST_LOGIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sfid = models.CharField(db_column='SFID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    start_time = models.CharField(db_column='START_TIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    end_time = models.CharField(db_column='END_TIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    years = models.IntegerField(db_column='YEARS', blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='NUMBER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_app_user'


class SysDictionaries(models.Model):
    zd_id = models.CharField(db_column='ZD_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bianma = models.CharField(db_column='BIANMA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ordy_by = models.IntegerField(db_column='ORDY_BY', blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(db_column='PARENT_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jb = models.IntegerField(db_column='JB', blank=True, null=True)  # Field name made lowercase.
    p_bm = models.CharField(db_column='P_BM', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_dictionaries'


class SysGlQx(models.Model):
    gl_id = models.CharField(db_column='GL_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    role_id = models.CharField(db_column='ROLE_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fx_qx = models.IntegerField(db_column='FX_QX', blank=True, null=True)  # Field name made lowercase.
    fw_qx = models.IntegerField(db_column='FW_QX', blank=True, null=True)  # Field name made lowercase.
    qx1 = models.IntegerField(db_column='QX1', blank=True, null=True)  # Field name made lowercase.
    qx2 = models.IntegerField(db_column='QX2', blank=True, null=True)  # Field name made lowercase.
    qx3 = models.IntegerField(db_column='QX3', blank=True, null=True)  # Field name made lowercase.
    qx4 = models.IntegerField(db_column='QX4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_gl_qx'


class SysMenu(models.Model):
    menu_id = models.IntegerField(db_column='MENU_ID', primary_key=True)  # Field name made lowercase.
    menu_name = models.CharField(db_column='MENU_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    menu_url = models.CharField(db_column='MENU_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(db_column='PARENT_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    menu_order = models.CharField(db_column='MENU_ORDER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    menu_icon = models.CharField(db_column='MENU_ICON', max_length=30, blank=True, null=True)  # Field name made lowercase.
    menu_type = models.CharField(db_column='MENU_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysRole(models.Model):
    role_id = models.CharField(db_column='ROLE_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    role_name = models.CharField(db_column='ROLE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rights = models.CharField(db_column='RIGHTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(db_column='PARENT_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    add_qx = models.CharField(db_column='ADD_QX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    del_qx = models.CharField(db_column='DEL_QX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    edit_qx = models.CharField(db_column='EDIT_QX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cha_qx = models.CharField(db_column='CHA_QX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qx_id = models.CharField(db_column='QX_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysUser(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rights = models.CharField(db_column='RIGHTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role_id = models.CharField(db_column='ROLE_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_login = models.CharField(db_column='LAST_LOGIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    skin = models.CharField(db_column='SKIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='NUMBER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserQx(models.Model):
    u_id = models.CharField(db_column='U_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    c1 = models.IntegerField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    c2 = models.IntegerField(db_column='C2', blank=True, null=True)  # Field name made lowercase.
    c3 = models.IntegerField(db_column='C3', blank=True, null=True)  # Field name made lowercase.
    c4 = models.IntegerField(db_column='C4', blank=True, null=True)  # Field name made lowercase.
    q1 = models.IntegerField(db_column='Q1', blank=True, null=True)  # Field name made lowercase.
    q2 = models.IntegerField(db_column='Q2', blank=True, null=True)  # Field name made lowercase.
    q3 = models.IntegerField(db_column='Q3', blank=True, null=True)  # Field name made lowercase.
    q4 = models.IntegerField(db_column='Q4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_user_qx'


class SysUserphoto(models.Model):
    userphoto_id = models.CharField(db_column='USERPHOTO_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    photo0 = models.CharField(db_column='PHOTO0', max_length=255, blank=True, null=True)  # Field name made lowercase.
    photo1 = models.CharField(db_column='PHOTO1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    photo2 = models.CharField(db_column='PHOTO2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    photo3 = models.CharField(db_column='PHOTO3', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_userphoto'


class TChapter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    textbookid = models.IntegerField(db_column='TextbookId', blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='Parent_Id', blank=True, null=True)  # Field name made lowercase.
    chaptername = models.CharField(db_column='ChapterName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    chapterrights = models.TextField(db_column='ChapterRights', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_chapter'


class TChapterknowledge(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    chapterid = models.IntegerField(db_column='ChapterId', blank=True, null=True)  # Field name made lowercase.
    knowledgeid = models.IntegerField(db_column='KnowledgeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_chapterknowledge'

class TSchool(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schooltype = models.IntegerField(db_column='SchoolType', blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    faculty = models.CharField(db_column='Faculty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licenceurl = models.CharField(db_column='LicenceUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardfronturl = models.CharField(db_column='CardFrontUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardbackurl = models.CharField(db_column='CardBackUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logourl = models.CharField(db_column='LogoUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=255, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adminuser = models.CharField(db_column='AdminUser', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adminphone = models.CharField(db_column='AdminPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    examine = models.IntegerField(db_column='Examine', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.schoolname

    class Meta:
        managed = False
        db_table = 't_school'
        verbose_name_plural = '学校'

class TClass(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='Introduction', max_length=400, blank=True, null=True)  # Field name made lowercase.
    classadviserid = models.IntegerField(db_column='ClassAdviserId', blank=True, null=True)  # Field name made lowercase.
    studentnum = models.IntegerField(db_column='StudentNum', blank=True, null=True)  # Field name made lowercase.
    teachernum = models.IntegerField(db_column='TeacherNum', blank=True, null=True)  # Field name made lowercase.
    enteryear = models.CharField(db_column='EnterYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    endenteryear = models.CharField(db_column='EndEnterYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_class'


class TClasslearning(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    subjectsid = models.IntegerField(db_column='SubjectsId', blank=True, null=True)  # Field name made lowercase.
    leartype = models.IntegerField(db_column='LearType', blank=True, null=True)  # Field name made lowercase.
    completion = models.CharField(db_column='Completion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    totalscore = models.CharField(db_column='TotalScore', max_length=10, blank=True, null=True)  # Field name made lowercase.
    averagescore = models.CharField(db_column='AverageScore', max_length=10, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_classlearning'


class TClassnotice(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_classnotice'


class TClassstudent(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_classstudent'


class TClassteacher(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId', blank=True, null=True)  # Field name made lowercase.
    subjectsid = models.IntegerField(db_column='SubjectsId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_classteacher'


class TConstant(models.Model):
    namekey = models.CharField(db_column='NameKey', primary_key=True, max_length=100)  # Field name made lowercase.
    nametype = models.IntegerField(db_column='NameType')  # Field name made lowercase.
    namevalue = models.CharField(db_column='NameValue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_constant'
        unique_together = (('namekey', 'nametype'),)


class TExamtype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.typename

    class Meta:
        managed = False
        db_table = 't_examtype'

class TExamachievement(models.Model):
    examid = models.IntegerField(db_column='ExamId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scoringrate = models.CharField(db_column='ScoringRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    examtype = models.IntegerField(db_column='examType', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_examachievement'


class TExamcard(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId')  # Field name made lowercase.
    testpaperid = models.IntegerField(db_column='TestPaperId', blank=True, null=True)  # Field name made lowercase.
    testpaperversion = models.IntegerField(db_column='TestPaperVersion', blank=True, null=True)  # Field name made lowercase.
    papersize = models.CharField(db_column='PaperSize', max_length=100, blank=True, null=True)  # Field name made lowercase.
    layouttype = models.IntegerField(db_column='LayoutType', blank=True, null=True)  # Field name made lowercase.
    versiontype = models.IntegerField(db_column='VersionType', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.IntegerField(db_column='SourceType', blank=True, null=True)  # Field name made lowercase.
    prohibittype = models.IntegerField(db_column='ProhibitType', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    cardhtml = models.TextField(db_column='CardHtml', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_examcard'

class TExaminfo(models.Model):
    exam_mode_choice = (
        (0, '线上'),
        (1, '线下')
    )


    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    #schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    schoolid = models.ForeignKey(TSchool, db_column='SchoolId')
    examname = models.CharField(db_column='examName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    examtype = models.CharField(db_column='examType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    examtypeid = models.ForeignKey(TExamtype, db_column='examTypeId')
    begindate = models.CharField(db_column='BeginDate', max_length=32, blank=True, null=True, default=getYzDefaultFmtDateTime())  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=32, blank=True, null=True, default=getYzDefaultFmtDateTime())  # Field name made lowercase.
    exammode = models.IntegerField(db_column='examMode', blank=True, null=True, choices=exam_mode_choice)  # Field name made lowercase.
    examisstate = models.IntegerField(db_column='examIsstate', blank=True, null=True)  # Field name made lowercase.
    schoolrange = models.IntegerField(db_column='SchoolRange', blank=True, null=True)  # Field name made lowercase.
    studentnum = models.IntegerField(db_column='StudentNum', blank=True, null=True)  # Field name made lowercase.
    isanswecard = models.IntegerField(db_column='IsAnsweCard', blank=True, null=True)  # Field name made lowercase.
    totalscore = models.FloatField(db_column='TotalScore', blank=True, null=True)  # Field name made lowercase.
    isresults = models.IntegerField(db_column='IsResults', blank=True, null=True)  # Field name made lowercase.
    judgestatus = models.IntegerField(db_column='JudgeStatus', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    subjectids = models.CharField(db_column='SubjectIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    faculty = models.CharField(db_column='Faculty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='GradeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gradeid = models.CharField(db_column='GradeId', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_examinfo'


class TExamstudent(models.Model):
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    studentname = models.CharField(db_column='StudentName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId', blank=True, null=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='GradeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_examstudent'


class TExamstudentTemp(models.Model):
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_examstudent_temp'


class TExamsubject(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId', blank=True, null=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='GradeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    begindate = models.CharField(db_column='BeginDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    testpapername = models.CharField(db_column='TestPaperName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    testpaperid = models.IntegerField(db_column='TestPaperId', blank=True, null=True)  # Field name made lowercase.
    corrprosinglenum = models.IntegerField(db_column='CorrProSingleNum', blank=True, null=True)  # Field name made lowercase.
    corrprototalnum = models.IntegerField(db_column='CorrProTotalNum', blank=True, null=True)  # Field name made lowercase.
    scannum = models.IntegerField(db_column='ScanNum', blank=True, null=True)  # Field name made lowercase.
    errornum = models.IntegerField(db_column='ErrorNum', blank=True, null=True)  # Field name made lowercase.
    markednum = models.IntegerField(db_column='MarkedNum', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_examsubject'


class TFavorites(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    favoritesname = models.CharField(db_column='FavoritesName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    platformid = models.CharField(db_column='PlatformId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_favorites'


class TFavoritesquestions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    platformid = models.CharField(db_column='PlatformId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    favid = models.IntegerField(db_column='FavId', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_favoritesquestions'


class TFrontenduser(models.Model):
    platformnumber = models.CharField(db_column='PlatformNumber', primary_key=True, max_length=255)  # Field name made lowercase.
    role_id = models.CharField(db_column='Role_Id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idcard = models.CharField(db_column='IdCard', max_length=18, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    wechat = models.CharField(db_column='WeChat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sina = models.CharField(db_column='Sina', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_type = models.IntegerField(db_column='User_Type', blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    currentrole = models.IntegerField(db_column='CurrentRole', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    introduce = models.CharField(db_column='Introduce', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    photourl = models.CharField(db_column='PhotoUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_frontenduser'


class TGradesubjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fatherid = models.IntegerField(db_column='FatherId', blank=True, null=True)  # Field name made lowercase.
    faculty = models.CharField(db_column='Faculty', max_length=10)  # Field name made lowercase.
    namevalue = models.CharField(db_column='NameValue', max_length=10)  # Field name made lowercase.
    nametype = models.IntegerField(db_column='NameType')  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate')  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_gradesubjects'


class TKnowledge(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    subjectsid = models.IntegerField(db_column='SubjectsId', blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='Parent_Id', blank=True, null=True)  # Field name made lowercase.
    knowledgename = models.CharField(db_column='KnowledgeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_knowledge'


class TLogintoken(models.Model):
    platformnumber = models.CharField(db_column='PlatformNumber', primary_key=True, max_length=150)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=255)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_logintoken'


class TMenu(models.Model):
    menu_id = models.AutoField(db_column='Menu_Id', primary_key=True)  # Field name made lowercase.
    menu_type = models.IntegerField(db_column='Menu_Type')  # Field name made lowercase.
    menu_name = models.CharField(db_column='Menu_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    menu_url = models.CharField(db_column='Menu_Url', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='Parent_Id')  # Field name made lowercase.
    menu_order = models.IntegerField(db_column='Menu_Order', blank=True, null=True)  # Field name made lowercase.
    menu_icon = models.CharField(db_column='Menu_Icon', max_length=60, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_menu'
        unique_together = (('menu_id', 'menu_type'),)


class TPlatform(models.Model):
    plat_number = models.IntegerField(db_column='Plat_number')  # Field name made lowercase.
    iid = models.IntegerField(db_column='IID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_platform'


class TQuestionssource(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    questionname = models.CharField(db_column='QuestionName', max_length=100)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adminnumber = models.IntegerField(db_column='AdminNumber', blank=True, null=True)  # Field name made lowercase.
    schoolnumber = models.IntegerField(db_column='SchoolNumber', blank=True, null=True)  # Field name made lowercase.
    teachernumber = models.IntegerField(db_column='TeacherNumber', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_questionssource'


class TQulog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    testtype = models.CharField(db_column='TestType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logtype = models.IntegerField(db_column='LogType', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usertype = models.IntegerField(db_column='UserType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_qulog'


class TQuoldtestpaper(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    quid = models.IntegerField(db_column='QuId', blank=True, null=True)  # Field name made lowercase.
    quname = models.CharField(db_column='QuName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='GradeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=4, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=100, blank=True, null=True)  # Field name made lowercase.
    totalscore = models.CharField(db_column='TotalScore', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    paperisstate = models.IntegerField(db_column='PaperIsstate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qutype = models.CharField(db_column='QuType', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_quoldtestpaper'


class TQupaperattribute(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    testpaperid = models.IntegerField(db_column='TestPaperId', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attributetype = models.IntegerField(db_column='AttributeType', blank=True, null=True)  # Field name made lowercase.
    problemmaker = models.CharField(db_column='ProblemMaker', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attributejson = models.CharField(db_column='AttributeJson', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='GradeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_qupaperattribute'


class TQuscore(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    testpaperid = models.IntegerField(db_column='TestPaperId', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    titletype = models.CharField(db_column='TitleType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    mark = models.TextField(db_column='Mark', blank=True, null=True)  # Field name made lowercase.
    promark = models.TextField(db_column='ProMark', blank=True, null=True)  # Field name made lowercase.
    titlemark = models.CharField(db_column='TitleMark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_quscore'


class TQutest(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    testpaperid = models.IntegerField(db_column='TestPaperId', blank=True, null=True)  # Field name made lowercase.
    questionid = models.IntegerField(db_column='QuestionId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    qutype = models.IntegerField(db_column='QuType', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createusertype = models.IntegerField(db_column='CreateUserType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_qutest'


class TQutestcart(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    testpaperid = models.IntegerField(db_column='TestPaperId', blank=True, null=True)  # Field name made lowercase.
    questionid = models.IntegerField(db_column='QuestionId', blank=True, null=True)  # Field name made lowercase.
    qutype = models.CharField(db_column='QuType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    scoretitle = models.CharField(db_column='ScoreTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createusertype = models.IntegerField(db_column='CreateUserType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_qutestcart'


class TRole(models.Model):
    role_id = models.CharField(db_column='Role_Id', primary_key=True, max_length=100)  # Field name made lowercase.
    role_name = models.CharField(db_column='Role_Name', max_length=100)  # Field name made lowercase.
    rights = models.CharField(db_column='Rights', max_length=255)  # Field name made lowercase.
    parent_id = models.CharField(db_column='Parent_Id', max_length=100)  # Field name made lowercase.
    btn_sel = models.CharField(db_column='Btn_Sel', max_length=255)  # Field name made lowercase.
    btn_edit = models.CharField(db_column='Btn_Edit', max_length=255)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate')  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role'


class TSchoollog(models.Model):
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_schoollog'


class TStudent(models.Model):
    genders = (
        (0, '男'),
        (1, '女')
    )

    validators = {
        (0, '未启用'),
        (1, '启用')
    }

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    #schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    schoolid = models.ForeignKey(TSchool, db_column='SchoolId')
    platformid = models.CharField(db_column='PlatformId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex', blank=True, null=True, choices=genders)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    studentnumber = models.CharField(db_column='StudentNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    idcard = models.CharField(db_column='IdCard', max_length=18)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True, choices=validators)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True, default=getYzDefaultFmtDateTime())  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_student'


class TTeacher(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    platformid = models.CharField(db_column='PlatformId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    teachernumber = models.CharField(db_column='TeacherNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    idcard = models.CharField(db_column='IdCard', max_length=18)  # Field name made lowercase.
    nature = models.IntegerField(db_column='Nature', blank=True, null=True)  # Field name made lowercase.
    working = models.IntegerField(db_column='Working', blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_teacher'


class TTeachertemp(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    teachernumber = models.CharField(db_column='TeacherNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idcard = models.CharField(db_column='IdCard', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nature = models.IntegerField(db_column='Nature', blank=True, null=True)  # Field name made lowercase.
    working = models.IntegerField(db_column='Working', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_teachertemp'


class TTestcorrection(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    errorid = models.CharField(db_column='ErrorId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    errortype = models.CharField(db_column='ErrorType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testcorrection'


class TTesterrors(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    platformid = models.CharField(db_column='PlatformId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=400, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isconquer = models.IntegerField(db_column='IsConquer', blank=True, null=True)  # Field name made lowercase.
    imgpath = models.CharField(db_column='ImgPath', max_length=400, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testerrors'


class TTesterrorstemp(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    platformid = models.CharField(db_column='PlatformId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testerrorstemp'


class TTestoption(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    problemid = models.IntegerField(db_column='ProblemId', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    opnum = models.CharField(db_column='OpNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testoption'


class TTestoptionHistory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    problemid = models.IntegerField(db_column='ProblemId', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    opnum = models.CharField(db_column='OpNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testoption_history'
        unique_together = (('id', 'versionid'),)


class TTestproblem(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    qutitle = models.TextField(db_column='QuTitle', blank=True, null=True)  # Field name made lowercase.
    analysis = models.TextField(db_column='Analysis', blank=True, null=True)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    qutype = models.CharField(db_column='QuType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    chapterid = models.TextField(db_column='ChapterId', blank=True, null=True)  # Field name made lowercase.
    knowledgeid = models.TextField(db_column='KnowledgeId', blank=True, null=True)  # Field name made lowercase.
    textbookid = models.IntegerField(db_column='TextbookId', blank=True, null=True)  # Field name made lowercase.
    textbookname = models.CharField(db_column='TextbookName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ishide = models.IntegerField(db_column='IsHide', blank=True, null=True)  # Field name made lowercase.
    facilityvalue = models.CharField(db_column='FacilityValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    totalscore = models.FloatField(db_column='TotalScore', blank=True, null=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testproblem'


class TTestproblemHistory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    qutitle = models.TextField(db_column='QuTitle', blank=True, null=True)  # Field name made lowercase.
    analysis = models.TextField(db_column='Analysis', blank=True, null=True)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    qutype = models.CharField(db_column='QuType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    chapterid = models.TextField(db_column='ChapterId', blank=True, null=True)  # Field name made lowercase.
    knowledgeid = models.TextField(db_column='KnowledgeId', blank=True, null=True)  # Field name made lowercase.
    textbookid = models.IntegerField(db_column='TextbookId', blank=True, null=True)  # Field name made lowercase.
    textbookname = models.CharField(db_column='TextbookName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ishide = models.IntegerField(db_column='IsHide', blank=True, null=True)  # Field name made lowercase.
    facilityvalue = models.CharField(db_column='FacilityValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    totalscore = models.FloatField(db_column='TotalScore', blank=True, null=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testproblem_history'
        unique_together = (('id', 'versionid'),)


class TTestquestions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=500, blank=True, null=True)  # Field name made lowercase.
    collectionnum = models.IntegerField(db_column='CollectionNum', blank=True, null=True)  # Field name made lowercase.
    quotenum = models.IntegerField(db_column='QuoteNum', blank=True, null=True)  # Field name made lowercase.
    correctrate = models.CharField(db_column='CorrectRate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    faculty = models.CharField(db_column='Faculty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    titletype = models.CharField(db_column='TitleType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ishide = models.IntegerField(db_column='IsHide', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createusertype = models.IntegerField(db_column='CreateUserType', blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    facilityvalue = models.CharField(db_column='FacilityValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    totalscore = models.FloatField(db_column='TotalScore', blank=True, null=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testquestions'


class TTestquestionsHistory(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=500, blank=True, null=True)  # Field name made lowercase.
    collectionnum = models.IntegerField(db_column='CollectionNum', blank=True, null=True)  # Field name made lowercase.
    quotenum = models.IntegerField(db_column='QuoteNum', blank=True, null=True)  # Field name made lowercase.
    correctrate = models.CharField(db_column='CorrectRate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    faculty = models.CharField(db_column='Faculty', max_length=255, blank=True, null=True)  # Field name made lowercase.
    titletype = models.CharField(db_column='TitleType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ishide = models.IntegerField(db_column='IsHide', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createusertype = models.IntegerField(db_column='CreateUserType', blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    facilityvalue = models.CharField(db_column='FacilityValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    totalscore = models.FloatField(db_column='TotalScore', blank=True, null=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_testquestions_history'
        unique_together = (('id', 'versionid'),)


class TTextbook(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    textbookname = models.CharField(db_column='TextbookName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    faculty = models.CharField(db_column='Faculty', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectsid = models.IntegerField(db_column='SubjectsId', blank=True, null=True)  # Field name made lowercase.
    subjectsname = models.CharField(db_column='SubjectsName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_textbook'


class TTextbookversion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    faculty = models.CharField(db_column='Faculty', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectsid = models.CharField(db_column='SubjectsId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subjectsname = models.CharField(db_column='SubjectsName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    versionname = models.CharField(db_column='VersionName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='UpdateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_textbookversion'


class TUserpaperattribute(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=500, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    describes = models.CharField(db_column='Describes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attributetype = models.CharField(db_column='AttributeType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    problemmaker = models.CharField(db_column='ProblemMaker', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='GradeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iscomplete = models.IntegerField(db_column='IsComplete', blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=255, blank=True, null=True)  # Field name made lowercase.
    testnum = models.IntegerField(db_column='TestNum', blank=True, null=True)  # Field name made lowercase.
    examnum = models.IntegerField(db_column='ExamNum', blank=True, null=True)  # Field name made lowercase.
    homeworknum = models.IntegerField(db_column='HomeWorkNum', blank=True, null=True)  # Field name made lowercase.
    questionsnum = models.IntegerField(db_column='QuestionsNum', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    testsourceid = models.IntegerField(db_column='TestSourceId', blank=True, null=True)  # Field name made lowercase.
    testsourcename = models.CharField(db_column='TestSourceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sharingcode = models.CharField(db_column='SharingCode', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userpaperattribute'


class TUserrole(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    menuname = models.CharField(db_column='MenuName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    btnsel = models.CharField(db_column='BtnSel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btnopt = models.CharField(db_column='BtnOpt', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userrole'


class TUserscore(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    attributeid = models.IntegerField(db_column='AttributeId', blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    titletype = models.CharField(db_column='TitleType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scorejson = models.TextField(db_column='ScoreJson', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    isequal = models.IntegerField(db_column='IsEqual', blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userscore'


class TUserscorecart(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    titletype = models.CharField(db_column='TitleType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scorejson = models.TextField(db_column='ScoreJson', blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    isequal = models.IntegerField(db_column='IsEqual', blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userscorecart'


class TUserstudentquestion(models.Model):
    testid = models.IntegerField(db_column='TestId')  # Field name made lowercase.
    proid = models.IntegerField(db_column='ProId')  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId')  # Field name made lowercase.
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    attributeid = models.IntegerField(db_column='AttributeId', blank=True, null=True)  # Field name made lowercase.
    qutype = models.CharField(db_column='QuType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proscore = models.CharField(db_column='ProScore', max_length=50, blank=True, null=True)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iscorrect = models.IntegerField(db_column='IsCorrect', blank=True, null=True)  # Field name made lowercase.
    iscorrecting = models.IntegerField(db_column='IsCorrecting', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    oldproscore = models.CharField(db_column='OldProScore', max_length=50, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qucandidate = models.CharField(db_column='QuCandidate', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userstudentquestion'


class TUserstudenttest(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    attributeid = models.IntegerField(db_column='AttributeId', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    isstate = models.IntegerField(db_column='Isstate', blank=True, null=True)  # Field name made lowercase.
    correctrate = models.CharField(db_column='CorrectRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    errorrate = models.CharField(db_column='ErrorRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usetime = models.CharField(db_column='UseTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    begindate = models.CharField(db_column='BeginDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    suspenddate = models.CharField(db_column='SuspendDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userstudenttest'


class TUsertest(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    attributeid = models.IntegerField(db_column='AttributeId', blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    titletype = models.CharField(db_column='TitleType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    testversionid = models.IntegerField(db_column='TestVersionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_usertest'


class TUsertestcart(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='TestId', blank=True, null=True)  # Field name made lowercase.
    titletype = models.CharField(db_column='TitleType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_usertestcart'


class TUsertestfjlist(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    probelmid = models.IntegerField(db_column='ProbelmId')  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_usertestfjlist'


class TUsertestjudgemode(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    judges = models.CharField(db_column='Judges', max_length=256)  # Field name made lowercase.
    finaljudges = models.CharField(db_column='FinalJudges', max_length=256, blank=True, null=True)  # Field name made lowercase.
    pointgap = models.DecimalField(db_column='PointGap', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    proindexes = models.CharField(db_column='ProIndexes', max_length=256)  # Field name made lowercase.
    proids = models.CharField(db_column='ProIds', max_length=256)  # Field name made lowercase.
    classids = models.CharField(db_column='ClassIds', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_usertestjudgemode'


class TUsertestjudges(models.Model):
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId')  # Field name made lowercase.
    teachername = models.CharField(db_column='TeacherName', max_length=128)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_usertestjudges'


class TUsertestjudgetask(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId')  # Field name made lowercase.
    donenum = models.IntegerField(db_column='DoneNum', blank=True, null=True)  # Field name made lowercase.
    tasknum = models.IntegerField(db_column='TaskNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_usertestjudgetask'


class TUsertestscanproblem(models.Model):
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    attributeid = models.IntegerField(db_column='AttributeId', blank=True, null=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId')  # Field name made lowercase.
    problemid = models.IntegerField(db_column='ProblemId')  # Field name made lowercase.
    scanimg = models.CharField(db_column='ScanImg', max_length=512, blank=True, null=True)  # Field name made lowercase.
    oldproscore = models.CharField(db_column='OldProScore', max_length=11)  # Field name made lowercase.
    proscore = models.CharField(db_column='ProScore', max_length=11)  # Field name made lowercase.
    memo = models.TextField(db_column='Memo', blank=True, null=True)  # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True, null=True)  # Field name made lowercase.
    procandidate = models.CharField(db_column='ProCandidate', max_length=256, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_usertestscanproblem'


class TUserteststructure(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bigtile = models.IntegerField(db_column='BigTile')  # Field name made lowercase.
    biggroup = models.IntegerField(db_column='BigGroup', blank=True, null=True)  # Field name made lowercase.
    bigindex = models.IntegerField(db_column='BigIndex')  # Field name made lowercase.
    bigalias = models.CharField(db_column='BigAlias', max_length=128, blank=True, null=True)  # Field name made lowercase.
    questionid = models.IntegerField(db_column='QuestionId')  # Field name made lowercase.
    problemid = models.IntegerField(db_column='ProblemId')  # Field name made lowercase.
    attributeid = models.IntegerField(db_column='AttributeId')  # Field name made lowercase.
    issubjective = models.SmallIntegerField(db_column='IsSubjective', blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    inposition = models.IntegerField(db_column='InPosition', blank=True, null=True)  # Field name made lowercase.
    indetail = models.CharField(db_column='InDetail', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userteststructure'


class TUserteststudentscan(models.Model):
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    admissionticket = models.CharField(db_column='AdmissionTicket', max_length=128, blank=True, null=True)  # Field name made lowercase.
    examdir = models.CharField(db_column='ExamDir', max_length=128)  # Field name made lowercase.
    studenttestdir = models.CharField(db_column='StudentTestDir', max_length=128)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=512)  # Field name made lowercase.
    errortype = models.IntegerField(db_column='ErrorType', blank=True, null=True)  # Field name made lowercase.
    createuser = models.CharField(db_column='CreateUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userteststudentscan'


class TUserteststudentscanraw(models.Model):
    examsubjectid = models.IntegerField(db_column='examSubjectId')  # Field name made lowercase.
    examdir = models.CharField(db_column='ExamDir', max_length=128)  # Field name made lowercase.
    studenttestdir = models.CharField(db_column='StudentTestDir', max_length=128)  # Field name made lowercase.
    testindex = models.IntegerField(db_column='TestIndex')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=512)  # Field name made lowercase.
    rawanswer = models.TextField(db_column='RawAnswer')  # Field name made lowercase.
    amendanswer = models.TextField(db_column='AmendAnswer', blank=True, null=True)  # Field name made lowercase.
    rawerrors = models.TextField(db_column='RawErrors', blank=True, null=True)  # Field name made lowercase.
    errorstofix = models.TextField(db_column='ErrorsToFix', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userteststudentscanraw'


class TbPictures(models.Model):
    pictures_id = models.CharField(db_column='PICTURES_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='CREATETIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_id = models.CharField(db_column='MASTER_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_pictures'


class VTextbook(models.Model):
    textbookname = models.IntegerField(db_column='TextbookName')  # Field name made lowercase.
    faculty = models.IntegerField(db_column='Faculty')  # Field name made lowercase.
    namevalue = models.IntegerField(db_column='NameValue')  # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    versionid = models.IntegerField(db_column='VersionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'v_textbook'


class VVersionsubject(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    subjectsid = models.IntegerField(db_column='SubjectsId')  # Field name made lowercase.
    versionname = models.IntegerField(db_column='VersionName')  # Field name made lowercase.
    memo = models.IntegerField(db_column='Memo')  # Field name made lowercase.
    faculty = models.IntegerField(db_column='Faculty')  # Field name made lowercase.
    namevalue = models.IntegerField(db_column='NameValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'v_versionsubject'


class WeixinCommand(models.Model):
    command_id = models.CharField(db_column='COMMAND_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commandcode = models.CharField(db_column='COMMANDCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='CREATETIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weixin_command'


class WeixinImgmsg(models.Model):
    imgmsg_id = models.CharField(db_column='IMGMSG_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='CREATETIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title1 = models.CharField(db_column='TITLE1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description1 = models.CharField(db_column='DESCRIPTION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl1 = models.CharField(db_column='IMGURL1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl1 = models.CharField(db_column='TOURL1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title2 = models.CharField(db_column='TITLE2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description2 = models.CharField(db_column='DESCRIPTION2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl2 = models.CharField(db_column='IMGURL2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl2 = models.CharField(db_column='TOURL2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title3 = models.CharField(db_column='TITLE3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description3 = models.CharField(db_column='DESCRIPTION3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl3 = models.CharField(db_column='IMGURL3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl3 = models.CharField(db_column='TOURL3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title4 = models.CharField(db_column='TITLE4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description4 = models.CharField(db_column='DESCRIPTION4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl4 = models.CharField(db_column='IMGURL4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl4 = models.CharField(db_column='TOURL4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title5 = models.CharField(db_column='TITLE5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description5 = models.CharField(db_column='DESCRIPTION5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl5 = models.CharField(db_column='IMGURL5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl5 = models.CharField(db_column='TOURL5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title6 = models.CharField(db_column='TITLE6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description6 = models.CharField(db_column='DESCRIPTION6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl6 = models.CharField(db_column='IMGURL6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl6 = models.CharField(db_column='TOURL6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title7 = models.CharField(db_column='TITLE7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description7 = models.CharField(db_column='DESCRIPTION7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl7 = models.CharField(db_column='IMGURL7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl7 = models.CharField(db_column='TOURL7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title8 = models.CharField(db_column='TITLE8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description8 = models.CharField(db_column='DESCRIPTION8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imgurl8 = models.CharField(db_column='IMGURL8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tourl8 = models.CharField(db_column='TOURL8', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weixin_imgmsg'


class WeixinTextmsg(models.Model):
    textmsg_id = models.CharField(db_column='TEXTMSG_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='CREATETIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    bz = models.CharField(db_column='BZ', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weixin_textmsg'