from django.contrib import admin
from testapp.models import User,Normal_User,Whole_Seller,Products,Bank_Detail,WishListss,Review,Blogs
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	pass
admin.site.register(User,UserAdmin)
class Normal_User_Admin(admin.ModelAdmin):
	list_display=['user','mobile']
admin.site.register(Normal_User,Normal_User_Admin)
class Whole_SellerAdmin(admin.ModelAdmin):
	list_display=['user','city','mobile','zip_code','gst_no']
admin.site.register(Whole_Seller,Whole_SellerAdmin)
class ProductAdmin(admin.ModelAdmin):
	list_display=['user','product_name','product_price','product_quantity','product_description','product_image','product_image1','product_image2']
admin.site.register(Products,ProductAdmin)
class Bank_DetailAdmin(admin.ModelAdmin):
	list_display=['user','name','acc_no','ifcs_code','branch_name','bank_name']
admin.site.register(Bank_Detail,Bank_DetailAdmin)
class WishlistAdmin(admin.ModelAdmin):
	list_display=['user','product_id']
admin.site.register(WishListss,WishlistAdmin)
class ReviewsAdmin(admin.ModelAdmin):
	list_display=['user','p_id','headline','description']
admin.site.register(Review,ReviewsAdmin)
class BlogAdmin(admin.ModelAdmin):
	list_display=['blog_title','blog_name','description','create_date','blog_image']
admin.site.register(Blogs,BlogAdmin)