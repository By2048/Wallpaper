# coding=utf-8
import datetime

from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

from home import admin as index_admin
from image.models import HotImage
from image.models import Image, Carousel, Tag, ImageScore, Rating, Category


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # def show_tags(self, obj):
    #     return ' '.join([tag.name for tag in obj.tags.all()])
    # tags= Tag.objects.filter(image_id=obj.id)

    # show_tags.short_description = '显示所有标签'

    list_display = ['id', 'name', 'url', 'width', 'height', 'type', 'date_add']
    list_display_links = ['id', 'name', 'url', 'width', 'height', 'type', 'date_add']

    search_fields = ['name', 'width', 'height', 'type']

    list_filder = ['width', 'height', 'type']
    ordering = ['id']

    fields = ('name', 'description', 'categorys', 'url', 'url_thumb',
              ('width', 'height', 'type'), 'click', ('user', 'date_add'), 'filter', 'content')
    # exclude = ('name',)  # 排除该字段

    # 详细时间分层筛选　
    date_hierarchy = 'date_add'

    # 直接在列表中修改
    # list_editable = ['name', 'url']

    actions = [index_admin.export_as_json]

    list_per_page = 10


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    def get_image_name(self, obj):
        return obj.image.name

    get_image_name.short_description = '图片名'

    def get_image_url_thumb(self, obj):
        return obj.image.url_thumb

    get_image_url_thumb.short_description = '图片链接'

    list_display = ['id', 'index', 'get_image_name', 'get_image_url_thumb', 'date_add']
    list_display_links = ['id', 'index', 'get_image_name', 'get_image_url_thumb', 'date_add']

    search_fields = ['image.name', 'width', 'height', 'type']

    ordering = ['index']

    actions = [index_admin.export_as_json]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    class CountFilter(admin.SimpleListFilter):
        title = '标签数量'
        parameter_name = 'count'

        def lookups(self, request, model_admin):
            return (
                ('0', '小于 100'),
                ('1', '大于 100'),
            )

        def queryset(self, request, queryset):
            if self.value() == '0':
                return queryset.filter(count__lte='100')
            if self.value() == '1':
                return queryset.filter(count__gte='100')

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    list_filter = (CountFilter,)

    search_fields = ['id', 'name']
    list_per_page = 10

    ordering = ['id']

    empty_value_display = '- null -'

    actions = [index_admin.export_as_json]


# @admin.register(TagImage)
# class TagImageAdmin(admin.ModelAdmin):
#
#     def show_tag(self, obj):
#         return ','.join([item.get_tag_name() for item in obj.tags.all()])
#
#     show_tag.short_description = '分类名'
#
#     def show_image(self, obj):
#         return obj.image.get_image_url()
#
#     show_image.short_description = '图片链接'
#
#     def show_user(self, obj):
#         return obj.user.get_user_username()
#
#     show_user.short_description = '用户'
#
#     list_display = ['id', 'show_tag', 'show_image', 'show_user', 'date_add']
#     list_display_links = ['id', 'show_tag', 'show_image', 'show_user', 'date_add']
#
#     # list_filter = ['tag__count', 'date_add']
#     list_filter = ['date_add']
#
#     filter_horizontal = ['tags']
#
#     search_fields = ['tag__name', 'date_add']
#
#     ordering = ['id']
#     list_per_page = 10
#
#     actions = [index_admin.export_as_json]
#
#     empyt_value_dispaly = '- null -'


@admin.register(ImageScore)
class ImageSourceAdmin(admin.ModelAdmin):
    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    list_display = ('id', 'show_image', 'average_stars', 'date_update')
    list_display_links = ('id', 'show_image', 'average_stars', 'date_update')

    list_filter = ['date_update', 'average_stars']

    search_fields = ['image__name', 'average_stars']
    list_per_page = 10

    ordering = ['id']

    empty_value_display = '- null -'

    actions = [index_admin.export_as_json]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    def show_user(self, obj):
        return obj.user.get_user_username()

    show_user.short_description = '用户'

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    list_display = ['id', 'show_user', 'show_image', 'date_add']
    list_display_links = ['id', 'show_user', 'show_image', 'date_add']

    # list_filter = ['tag__count', 'date_add']
    list_filter = ['star', 'date_add']

    search_fields = ['user__name', 'image__name', 'image__url', 'date_add']

    ordering = ['id']
    list_per_page = 10

    actions = [index_admin.export_as_json]

    empyt_value_dispaly = '- null -'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # def upper_case_name(obj):
    #     return obj.name.upper()
    # upper_case_name.short_description = 'Upper Name'
    # list_display = (upper_case_name,)

    class CountFilter(admin.SimpleListFilter):
        title = '图片数量'
        parameter_name = 'count'

        def lookups(self, request, model_admin):
            return (
                ('0', '小于 300'),
                ('1', '大于 300'),
            )

        def queryset(self, request, queryset):
            if self.value() == '0':
                return queryset.filter(count__lte='300')
            if self.value() == '1':
                return queryset.filter(count__gte='300')

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    list_filter = (CountFilter,)
    show_full_result_count = True

    search_fields = ['id', 'name', 'count']
    list_per_page = 10

    # 进入实际链接查看
    # def view_on_site(self, obj):
    #     url = reverse('person-detail', kwargs={'slug': obj.slug})
    #     return 'https://example.com' + url
    # view_on_site = True

    ordering = ['id']

    actions = ['make_published', index_admin.export_as_json]

    empty_value_display = '- empty value display -'

    def make_published(self, request, queryset):
        rows_updated = queryset.update(count='100')
        if rows_updated == 1:
            message_bit = "1 个分类"
        else:
            message_bit = "%s 个分类" % rows_updated
        self.message_user(request, "%s 成功更新." % message_bit)

    make_published.short_description = '设置图片数量为 100'

    # 重定向测试
    def export_selected_objects(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

    # 禁用默认的删除选项
    # admin.site.disable_action('delete_selected')


@admin.register(HotImage)
class HotImageAdmin(admin.ModelAdmin):

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    def show_exist_time(self, obj):
        date_add = obj.date_add
        data_now = datetime.datetime.now()
        seconds = (data_now - date_add).seconds
        if seconds < 3600:
            return str(seconds // 60) + ' 分钟'
        else:
            return str(seconds // 3600) + ' 小时'

    show_exist_time.short_description = '已经添加的时间'

    def show_click(self, obj):
        return obj.image.click

    show_click.short_description = '图片点击的次数'

    list_display = ['index', 'show_image', 'date_add', 'show_exist_time', 'show_click']

    fields = ('index', 'show_image', 'date_add', 'show_exist_time', 'show_click')

    ordering = ['index']

    # def get_readonly_fields(self, request, obj=None):
    #     """  重新定义此函数，限制普通用户所能修改的字段  """
    #     if request.user.is_superuser:
    #         self.readonly_fields = []
    #     return self.readonly_fields

    readonly_fields = ('index', 'show_image', 'date_add', 'show_exist_time', 'show_click')
