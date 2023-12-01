from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=100, null=False, unique=True)
    name = models.CharField("Category name" , max_length=25)
    image = models.ImageField("image", upload_to="category/", default="media\default\default_category.png")
    description = models.TextField("Description")
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="parent category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'M'
    XL = 'XL'
    SIZES = [
        (XS, 'XS'),
        (S, 's'),
        (M, 'M'),
        (L, 'L'),
        (XL, 'XL'),
    ]
    COLORS = [
        ("white", "White"),
        ("Black", "Black"),
        ("Green", "Green"),
        ("Red", "Red"),
        ("Blue", "Blue"),
    ]


    slug = models.SlugField("Slug", max_length=100, null=False, unique=True)
    name = models.CharField("Product name", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products" , null=True, blank=False, verbose_name="Category")
    price = models.DecimalField("Price", max_digits=7, decimal_places=2)
    size = models.CharField("Size", max_length=4, choices=SIZES)
    color = models.CharField("Color", max_length=10, choices=COLORS)
    description = models.TextField("Description")
    created = models.DateTimeField("Data created", auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="Product")
    image = models.ImageField("image", upload_to="products/", default="media\default\product-default-image.png")

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"

    def __str__(self):
        return self.product.name
    

class Review(models.Model):
    STATS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    slug = models.SlugField("Slug", max_length=100, null=False, unique=True)
    user = models.ForeignKey("account.User", on_delete=models.SET_NULL, related_name="reviews", null=True, verbose_name="Owner")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", verbose_name="product")
    text = models.TextField("Text")
    stars = models.PositiveSmallIntegerField("Stars", choices=STATS, null=True, blank=True)
    created = models.DateTimeField("Created at", auto_now_add=True)
    updated = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="images", verbose_name="Review")
    image = models.ImageField("Image", upload_to=f"reviews/", null=False, blank=True)


    class Meta:
        verbose_name = "Review image"
        verbose_name_plural = "Review images"
