
# Python 網頁學習筆記 📝  

## 目的 🚀  
用Django框架開發網頁

## MTV 架構 🔥  
| 核心        | 說明         |
| :--------- | :----------  |
| Model      | 描述你的資料類型        |
| Template   | 使用者看到網頁的形式         |
| Views      | 傳達資料(重點在於資料傳達的內容   |    

## 環境 ✨  
安裝套件:  
~~~bash  
sudo pip3 install django
~~~ 

檢查是否安裝完成:  
~~~bash  
python3 -m django --version
~~~ 

## 建立新專案🚗
~~~bash  
django-admin startproject [projectname]
~~~ 

## 結構說明📖
#### init.py:  
用來告訴Python這是一個套件(Package)
#### asgi.py:  
非同步伺服器閘道介面, 用來提供非同步的功能
#### settings.py:  
Django專案的設定檔
#### urls.py:
定義Django專案中, 各個應用程式(APP)的網址
#### wsgi.py:
網站伺服器閘道介面, 提供Django網站和伺服器間的標準介面
#### manage.py:
用來管理整個Django專案, 像是啟動本地端伺服器、連接資料庫及建立應用程式(APP)等  

## 查看幫助資訊
~~~bash  
python3 manage.py help
~~~ 

## 建立本地遷移DB💾
~~~bash  
python3 manage.py migrate
~~~ 
預設為SQLite, 後續可在`settings.py`修改

## 啟動本地端伺服器
~~~bash  
python3 manage.py runserver
~~~ 

## 服務設定🔧
如果要看中文介面要到`settings.py`進行修改, 打開檔案搜尋`LANGUAGE_CODE`, 並設定成`zh-Hant`

預設的時區是`UTC`, 依照需求可調整成台灣時間`Asia/Taipei` 

## 建立app
一個app所代表的就是一項功能, 根據功能的差異來分類app
~~~bash  
python3 manage.py startapp [app_name]
~~~ 

## app 結構說明📖
#### admin.py:  
設定資料庫呈現的模式, 之後會跟`models`溝通
#### models.py:  
建構你的資料庫型態
#### tests.py:  
拿來寫檢查商業邏輯的地方
#### views.py:
拿來寫商業邏輯的地方(`controller`), 它會跟`urls.py`做呼應, 並將所需傳達給`前端`
#### urls.py:
讓`views.py`與相對的網站做對應, `urls.py`要自己建立, 可以把外部的`urls.py`複製貼過來再修改即可
#### apps.py:
用來區別app的一個檔案
#### init.py:
用來告訴Python這是一個套件(Package)
#### migrations:
這資料夾裡面存放的內容, 記錄著models裡面所創建的資料庫型態

## app功能的路由綁定

在`[mydjango]`底下建立一個`app_test`
~~~bash  
python3 manage.py startapp app_test
~~~ 

路徑: `[mydjango]/app_test/views.py`
~~~bash  
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('測試app功能路由綁定')
~~~ 

路徑: `[mydjango]/app_test/urls.py` (從外部的`urls.py`複製貼過)
~~~bash  
from django.urls import path

from app_test import views

urlpatterns = [
    path('', views.index, name='index'),
]
~~~ 

路徑: `[mydjango]/urls.py`
~~~bash  
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('app_test.urls')),
]
~~~ 
說明:  
`include` 是路由的前綴, 綁定`app_test`底下的`urls.py`中全部路由的前綴為`test/`, 使用時須先在`django.urls`中`import include`

## 使用Mysql資料庫

如果還沒建立mysql資料庫則須先建立
~~~bash  
create database mydjango;
~~~

打開`settings.py`搜尋`DATABASES`關鍵字並修改設定
~~~bash  
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 指定使用的資料庫引擎，可以通過 Django.db.backends 來檢視哪些資料庫可以與 Django 配合使用；
        'NAME': 'mydjango',  # 資料庫名字
        'USER': "root",  # mysql 使用者名稱稱
        'PASSWORD': 'root',  # 資料庫的密碼
        'HOST': "127.0.0.1",  # 資料庫服務地址， 這裡我們是測試開發 填本地地址 
        'PORT': 3306,   # mysql 對應的埠號 
        'default-character-set': "UTF8",  # 設定編碼規則 utf8 
    }
}
~~~ 

接著安裝 pymysql 這個庫
~~~bash  
pip3 install PyMySQL
~~~

在同一層的`init.py`中 加入一段程式碼
~~~bash
import pymysql 
pymysql.install_as_MySQLdb()
~~~

最後執行`migrate`進行資料遷移, 在mysql中就會看到django幫你建立好的資料表
~~~bash
python3 manage.py migrate
~~~

當資料表更改後, 需執行`makemigrations`指令, 並再次執行`migrate`指令讓新的遷移檔案生效並同步回資料庫
~~~bash
python3 manage.py makemigrations
python3 manage.py migrate
~~~

總結:  
每一次資料表更改後，都需要執行上面的兩個指令
