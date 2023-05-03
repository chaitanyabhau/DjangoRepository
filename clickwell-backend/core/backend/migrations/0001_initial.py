# Generated by Django 4.1.7 on 2023-03-25 18:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tx_amount', models.IntegerField(default=0)),
                ('payment_mode', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(max_length=5000)),
                ('tx_id', models.CharField(max_length=1000, null=True)),
                ('tx_status', models.CharField(choices=[('INITIATED', 'INITIATED'), ('PENDING', 'PENDING'), ('INCOMPLETE', 'INCOMPLETE'), ('FAILED', 'FAILED'), ('FLAGGED', 'FLAGGED'), ('USER_DROPPED', 'USER_DROPPED'), ('SUCCESS', 'SUCCESS'), ('CANCELLED', 'CANCELLED'), ('VOID', 'VOID')], max_length=100, null=True)),
                ('tx_time', models.CharField(max_length=500, null=True)),
                ('tx_msg', models.CharField(max_length=500, null=True)),
                ('from_cart', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('otp', models.IntegerField()),
                ('validity', models.DateTimeField()),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=100000)),
                ('price', models.IntegerField(default=0)),
                ('offer_price', models.IntegerField(default=0)),
                ('delivery_charge', models.IntegerField(default=0)),
                ('star_5', models.IntegerField(default=0)),
                ('star_4', models.IntegerField(default=0)),
                ('star_3', models.IntegerField(default=0)),
                ('star_2', models.IntegerField(default=0)),
                ('star_1', models.IntegerField(default=0)),
                ('cod', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_set', to='backend.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('option', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options_set', to='backend.product')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True, max_length=1000)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=10)),
                ('district', models.CharField(blank=True, max_length=500)),
                ('state', models.CharField(blank=True, max_length=500)),
                ('cart', models.ManyToManyField(blank=True, related_name='cart', to='backend.productoption')),
                ('wishlist', models.ManyToManyField(blank=True, related_name='wishlist', to='backend.productoption')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=5000)),
                ('fcmtoken', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens_set', to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='product/')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_set', to='backend.productoption')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=5000)),
                ('validity', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_reset_tokens_set', to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='PageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='product/')),
                ('viewtype', models.IntegerField(choices=[(1, 'BANNER'), (2, 'SWIPER'), (3, 'GRID')])),
                ('title', models.CharField(blank=True, max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pageitems_set', to='backend.category')),
                ('product_options', models.ManyToManyField(blank=True, to='backend.productoption')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_price', models.IntegerField(default=0)),
                ('tx_price', models.IntegerField(default=0)),
                ('delivery_price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('rating', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('ORDERED', 'ORDERED'), ('PACKED', 'PACKED'), ('SHIPPED', 'SHIPPED'), ('OUT_FOR_DELIVERY', 'OUT_FOR_DELIVERY'), ('DELIVERED', 'DELIVERED'), ('CANCELLED', 'CANCELLED')], default='ORDERED', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_set', to='backend.order')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_options_set', to='backend.productoption')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_set', to='backend.user'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('body', models.TextField(max_length=1000)),
                ('seen', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='notifications/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_set', to='backend.user')),
            ],
        ),
    ]
