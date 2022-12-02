
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

## 建立本地遷移DB💾
~~~bash  
python3 manage.py migrate
~~~ 

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
