from rest_framework import serializers
from article.models import Article

from dateutil import parser
from datetime import datetime,date,timezone
from django.utils.timesince import timesince

from django.contrib.auth.models import User

#eğer ArticleSerializer içinde author = UserSerializer kullanmak istiyorsak 
# class UserSerializer(serializers.ModelSerializer): #içinde belirtileceği class'dan önce belirtilmezse sayfa hata verir
#     class Meta:
#         model = User
#         fields = ["id","username","first_name","email"]

#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class ArticleSerializer(serializers.ModelSerializer):
    
    #author = serializers.StringRelatedField() #article model'inde foreignkey ile related edilmiş user objectlerinin def __str__() altında return ile belirtilmiş değerlerinin görünmesini sağlamak için bu ifadeyi kullandık(author = yani serializer içindeki author attributeunu ilişkili objedeki str metodu altındaki değeri gösterdik)
    # author = UserSerializer() #çok güzel bir özellik yazarları özellikleriyle beraber çekmiş oluruz, *related_name = UserSerializer()
    class Meta:
        model = Article
        #fields = ["id","author","title","content","created_date","article_image"]
        #exclude = ["id","author"] hariç tut demek
        fields = "__all__"
        #read_only_fields = ["id","created_date"]
        read_only_fields = ["id","created_date"]
    
    time_since_pub = serializers.SerializerMethodField()#bir attribute belirtiyor ve ekliyoruz(model den çekilen attribute yanına başka bir attribute (özellik) eklemek için)
    def get_time_since_pub(self,object):#get_time yani time adlı bir attribute ekliyoruz serializers'a
        now = datetime.now(timezone.utc)#dönüşüm için önemli
        pub_date = object.created_date
        time_delta = timesince(pub_date,now)#oluşturulma tarihinden bu zamana kadar geçen süreyi hesaspladık
        return time_delta


    #https://www.django-rest-framework.org/api-guide/validators/    
    #custom validate belirtme(modelde def celan ile de belirtilirse burası için geçerli olabilir) 
    
    def validate_created_date(self,date_value):
        today = date.today()
        if date_value > today:
            raise serializers.ValidationError("Yaratılma Tarihi ileri bir tarih olamaz.")
        return date_value
    
    def validate(self,data): #object level (obje bazında kontrol)
        if data['title'] == data['content']:
            raise serializers.ValidationError("Başlık ve açıklama alanları aynı olamaz.")
        return data
    def validate_title(self, value): #field level (alan bazında kontrol) #validate_kontroledilmekistenenalan
        if len(value) < 2:
            raise serializers.ValidationError(f"Başlık alanı minimum 20 karakter olmalı. Siz {len(value)} girdiniz.")
        return value

#eğer user lar ile alakalı yeni bir sayfaf ve altalrında da ilişkili oldukları makaleleri göstermek istiyorsak
class UserSerializer(serializers.ModelSerializer):
    #articles = serializers.SerializerMethodField() #böyle bir belirtmede get_articles belirtmeliyiz 
    #HyperLink Related ekleme sebebimiz ilişkili veriyi çekmemiz *related_name = serializers.HyperlinkedRelatedField()* eğer sadece okumak istiyorsak tüm objeleri many=True,read_only=True eklemeliyiz
    #articles = ArticleSerializer(many = True,read_only = True) #böyle bir belirtmede get_articles belirmtemize gerek yok bu sayede tüm articles göüzkecektir #makale vermeden yazar oluşturabiliyoruz artık
    class Meta:
        model = User
        fields = "__all__"
    articles = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name="api-articles"
    )
    #view_name'yi gideceğimiz linklerin yoluna verilen name= attrsini veriyoruz
    #context={'request':request}'i sorumlu UserListCreateAPIView altına Response'a eklememiz gerekiyor
    
    
    # def get_articles(self,object):
    #     serializer = ArticleSerializer(Article.objects.all(),many = True)
    #     return serializer.data
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only= True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     content = serializers.CharField()
#     created_date = serializers.CharField(read_only = True)
#     article_image = serializers.FileField()
    

#     def create(self,validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)        

#     def update(self,instance,validated_data):
#         instance.author = validated_data.get('yazar',instance.author)
#         instance.title = validated_data.get('baslik',instance.title)
#         instance.content = validated_data.get('aciklama',instance.content)
#         instance.created_date = validated_data.get('yazar',instance.aktif)
#         instance.article_image = validated_data.get('yazar',instance.article_image)
#         instance.save()
#         return instance
#   def validate(self,data):
#       if data ['title'] == data['content']:
#             raise serializers.ValidationError("Başlık ve açıklama alanları aynı olamaz.")
#        return data
#   def validate_title(self, value): #field level (alan bazında kontrol) #validate_kontroledilmekistenenalan
#         if len(value) < 2:
#             raise serializers.ValidationError(f"Başlık alanı minimum 20 karakter olmalı. Siz {len(value)} girdiniz.")
#         return value