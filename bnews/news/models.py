from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    description = models.TextField("Описание")
    img_small = models.ImageField("Изо_маленькое", upload_to="news/")
    img_middle = models.ImageField("Изо_среднее", upload_to="news/")
    img_large = models.ImageField("Изо_большое", upload_to="news/")
    catigory = models.ForeignKey('Catigories', on_delete=models.PROTECT, verbose_name="Категория")
    published = models.DateTimeField(auto_now=True, db_index=True)
    sourсe = models.CharField("Источник", max_length=100)
    url = models.SlugField(max_length=30)
    url_cat = models.SlugField(max_length=30)


    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def get_single(self):
        return reverse("get_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Catigories(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название")
    url_cat = models.SlugField(max_length=30)


    def __str__(self):
        return self.name


    def get_catt(self):
        return reverse("by_rubric", kwargs={"slug": self.url_cat})


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Текст", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    news = models.ForeignKey(News, verbose_name="Новость", on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.name} - {self.news}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


