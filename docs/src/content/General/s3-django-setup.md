Title: Set up Amazon S3 to serve Django Static and Media files
Date: 2019-01-31 12:10
Authors: José Aniceto
Modified: 2019-02-03 20:46

Amazon S3 Buckets are a cheap way to store your staticfiles and media files. It also seems like the easiest way when serving a Django App. 

## 1) Sign up to AWS S3 and create IAM user

After signing up to Amazon AWS we need to create a user using the **IAM** service. This way you can restrict the access to the bucket. Each user will have its own access id and key. To do this:

* In the **Services** dropdown select **IAM**.

* Click on **Users** and select **Add User**.

* Type the name of the user and make sure that **Programmatic access** is selected under **Access type** as you will need this to provide upload access for your S3 bucket. Click **Next**.

* Select **Attatch existing policies directly**.

* From the list that appears select **AmazonS3FullAccess** and again click on **Next**.

* Click on **Create User**.

* This will create the user and generate an access id and key for the user. The id-key pair can only be downloaded at this step so do that by clicking on **Download .csv**. Keep it secret.

* From the Users Dashboard click on the user you have just created. Make a note of **User ARN**. You will be using this later.

## 2) Create a S3 Bucket

* From the Services dropdown select s3. This opens up the dashboard for the S3 buckets.

* Click on **Create Bucket**.

* Select the region you want.

  *Note: Try to create  a bucket in the same region where your app is running to take advantage of AWS's free in-region data transfer rates.*

* Give your bucket a name and click on next that brings you to the **Set Properties** tab. Click on **Next** a couple more times and then click on **Create Bucket** to create your bucket.

## 3) Set up Bucket permissions

Now let's define the policy for allowing restricted access to our bucket.

* Click on the name of the bucket that you just created.

* Click on the **Permissions** tab.

* Since you have to set the permissions for access, click on **Bucket Policy**.

* On the bottom left click on **AWS Policy Generator** which opens up the tool Amazon provides for quick policy generation. 

Now we have to generate two policy rules. The first one is to allow our hosted website to access your files from the bucket:

```
Select Type of Policy : S3 Bucket Policy
Effect : Allow
Principal : *      //This gives everybody access
AWS Service : Amazon S3
Actions : GetObject
Amazon Resource Name : arn:aws:s3:::<your bucket name>/* 
```
The `*` at the end siginifies that access is being given to all the files.

After setting the values as mentioned above click on **Add Statement**. Do not click on **Generate Policy** yet as you have to create a policy to allow the Django application to put files into the bucket on deployment. The policy will be as follows:

```
Select Type of Policy : S3 Bucket Policy
Effect : Allow
Principal : <User ARN>     //This is the user arn that you kept a note of earlier.
AWS Service : Amazon S3
Actions : *    //I gave full access, though I think GetObject, PutObject will be better. Will try it out soon. 
Amazon Resource Name : arn:aws:s3:::<your bucket name>/*,arn:aws:s3:::<your bucket name>  // Gives full access to buckets and its contents.
```

After setting the values mentioned above click on **Add Statement** and then **Generate Policy** . This will show you the policy which you can copy, paste in the dialogue box on S3 dashboard and click on **Save**.

## 4) Providing S3 access to your Heroku app

The last step for setting up the Bucket access is providing the application hosted on Heroku, access to the bucket content. This can be done by setting up the **CORS configuration**. To do this click on the **CORS Configuration** tab and click on Save. The default configuration will suffice. Something like this:

```
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

You have the bucket access set up. Now all you have to do is set up your Django application to access the bucket which is fairly easy. The first step to achieve the goal will be to install Boto3 and DjangoStorages. Nifty APIs to make working with S3 buckets easy. This can be easily done using pip.

```
pip install django-storages boto3
pip freeze >> requirements.txt
```

and add `storages` to the list of INSTALLED_APPS in the `settings.py` file.

```
INSTALLED_APPS = (
          ...,
          'storages',
     )
```

Next you have to add the following settings to the `settings.py` file in your application.

```python
# Set S3 as the place to store your files.
DEFAULT_FILE_STORAGE = 
storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_QUERYSTRING_AUTH = False # This will make sure that the file URL does not have unnecessary parameters like your access key.
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'

# Static media settings
STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
MEDIA_URL = STATIC_URL + 'media/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, "static"), )
STATIC_ROOT = 'staticfiles'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
```

Now, make sure the main `urls.py` file does include the url configuration for your media files:

```python
from django.conf import settings

urlpatterns = [
  ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

And as a last step there should be a folder called static in the root of your application (same level as the manage.py file). Git does not allow you to commit empty folders so you can inlcude a readme file in there to commit the folder.

If you are using Heroku before pushing your code use:

```
heroku config:set DISABLE_COLLECTSTATIC=1
```

to disable collectstatic running automatically as your static folder is not yet present on the server and an error will be thrown regarding the same. You can now push all changes to Heroku with

```
git push heroku master
```

or if you want to push from a different branch:

```
git push heroku testbranch:master
```

You can now run the `collectstatic` command manually using:

```
heroku run python manage.py collectstatic --noinput
```

If you get the following error:

```
UserWarning: The default behavior of S3Boto3Storage is insecure and will change in django-storages 2.0. By default files and new buckets are saved with an ACL of 'public-read' (globally publicly readable). Version 2.0 will default to using the bucket's ACL. To opt into the new behavior set AWS_DEFAULT_ACL = None, otherwise to silence this warning explicitly set AWS_DEFAULT_ACL. "The default behavior of S3Boto3Storage is insecure and will change "
...
AccessDenied
```

add the following variable to `settings.py`: 

```
AWS_DEFAULT_ACL = None
```

One important point before you go on this adventure. At the moment all the media files (files that are uploaded by the user) used in our models have the property `upload_to` set for them and as a result don't overwrite the static files. 

We are now ready to serve static and media files from the S3 bucket!


### References
* [Setting up Amazon S3 Bucket for serving Django Static and Media files](https://medium.com/@manibatra23/setting-up-amazon-s3-bucket-for-serving-django-static-and-media-files-3e781ab325d5)
* [Using Amazon S3 to Store your Django Site's Static and Media Files](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)
* [How to Setup Amazon S3 in a Django Project](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)
