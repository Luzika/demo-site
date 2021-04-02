from django.db import connections
from django.db import models

class OrderDetails(models.Model):
	COMPANY = (
		('CENTRA','CENTRA'),
		('CMSHIP','CMSHIP'),
		('DAN MO','DAN MO'),
		('DORVAL','DORVAL'),
		('EUCO','EUCO'),
		('FORTUNE WILL','FORTUNE WILL'),
		('GLOVIS','GLOVIS'),
		('GOLTENS','GOLTENS'),
		('GOWIN','GOWIN'),
		('INTERGIS','INTERGIS'),
		('KLCSM','KLCSM'),
		('KNK','KNK'),
		('KSS','KSS'),
		('MAN','MAN'),
		('MARUBISHI','MARUBISHI'),
		('POSSM','POSSM'),
		('SAEHAN','SAEHAN'),
		('SEOYANG','SEOYANG'),
		('SHI OCEAN','SHI OCEAN'),
		('STX','STX'),
		('SUNAMI','SUNAMI'),
		('SUNRIO','SUNRIO'),
		('보성상사','보성상사'),
		('오션마린','오션마린'),
		('이강공사','이강공사'),
		)

	WEARHOUSE = (
		('SL','SL'),
		('KIM-IGS','KIM-IGS'),
		('ICN-IGS','ICN-IGS'),
		)

	BY = (
		('DHL','DHL'),
		('FDX','FDX'),
		('TNT','TNT'),
		('AIR','AIR'),
		('SEA','SEA'),
		('SFX','SFX'),
		)
	DIVISION = (
        ("D", "D"),
        ("B", "B"),
        ("L", "L"),
    	)
	FLAG1 = (
    	('BLANK','BLANK'),
		('STAY','STAY'),
		('START','START'),
		('COMPLETED','COMPLETED'),
    	)

   

	# no = models.CharField(max_length=200, null=True)
	no = models.BigAutoField(primary_key=True)
	# kantor_id = models.CharField(null=True, db_column="kantor_id", max_length=30)
	company = models.CharField(max_length=200, null=True, choices=COMPANY)
	vessel = models.CharField(max_length=200, null=True)
	docs = models.CharField(null=True, db_column="doc", max_length=300)
	odr = models.CharField(max_length=200, null=True)

	supplier = models.CharField(max_length=200, null=True)
	qty = models.CharField(max_length=200, null=True)
	unit = models.CharField(null=True, db_column="unit", max_length=30)	
	size = models.CharField(max_length=200, null=True)

	weight = models.CharField(max_length=200, null=True)
	in1 = models.CharField(max_length=200, null=True)
	whouse = models.CharField(max_length=200, null=True, choices=WEARHOUSE)
	by1 = models.CharField(max_length=200, null=True, choices=BY)

	BLNO = models.CharField(blank=True, db_column="blno", max_length=30)
	port = models.CharField(max_length=200, null=True)
	outdate = models.CharField(null=True, db_column="out1", max_length=30)
	REMARK = models.CharField(null=True, db_column="remark", max_length=30)

	division = models.CharField(max_length=200, null=True, choices=DIVISION)
	jobnumber = models.CharField(null=True, db_column="jobno", max_length=30)
	# image = models.FileField(upload_to=None, db_column="img", max_length=30, null=True)
	# image1 = models.FileField(upload_to=None, db_column="img1", max_length=30, null=True)
	# image2 = models.FileField(upload_to=None, db_column="img2", max_length=30, null=True)
	# pdffile = models.CharField(null=True, db_column="pdf", max_length=30)
	


	# # 	no = models.BigAutoField(primary_key=True)
	# kantor_id = models.CharField(null=True, db_column="kantor_id", max_length=30)
	# insert_org = models.CharField(null=True, db_column="insert_org", max_length=30)
	# correct_org = models.CharField(null=True, db_column="correct_org", max_length=30)
	# reg_date = models.DateTimeField(auto_now=True, blank=True, db_column="regdate", max_length=30)
	# company = models.CharField(null=False, db_column="company", choices=COMPANY, max_length=30)
	# vessel = models.CharField(null=True, db_column="vessel", max_length=30)
	# by = models.CharField(null=True, db_column="by1", max_length=30)
	# BLno = models.CharField(null=True, db_column="blno", max_length=30)
	# docs = models.CharField(null=True, db_column="doc", max_length=300)
	# odr = models.CharField(null=True, db_column="odr", max_length=30)
	# supplier = models.CharField(null=True, db_column="supplier", max_length=30)
	# quanty = models.CharField(null=True, db_column="qty", max_length=30)
	# unit = models.CharField(null=True, db_column="unit", max_length=30)
	# size = models.CharField(null=True, db_column="size", max_length=30)
	# weight = models.CharField(null=True, db_column="weight", max_length=30)
	# indate = models.CharField(null=True, db_column="in1", max_length=30)
	# warehouse = models.CharField(null=True, db_column="whouse", max_length=30)
	# port = models.CharField(null=True, db_column="port", max_length=30)
	# outdate = models.CharField(null=True, db_column="out1", max_length=30)
	# remark = models.CharField(null=True, db_column="remark", max_length=30)
	# # image = models.FileField(upload_to=None, db_column="img", max_length=30, null=True)
	# # image1 = models.FileField(upload_to=None, db_column="img1", max_length=30, null=True)
	# # image2 = models.FileField(upload_to=None, db_column="img2", max_length=30, null=True)
	# pdffile = models.CharField(null=True, db_column="pdf", max_length=30)
	# division = models.CharField(null=True, db_column="division", choices=DIVISION, max_length=30)
	# flagstatus = models.CharField(null=True, db_column="flg", choices=FLAG1, max_length=30)
	# jobnumber = models.CharField(null=True, db_column="jobno", max_length=30)
	# work = models.CharField(null=True, db_column="work", max_length=30)
	# work_regdate = models.CharField(null=True, db_column="work_regdate", max_length=30)


	class Meta:
		db_table = "pla_databoard"