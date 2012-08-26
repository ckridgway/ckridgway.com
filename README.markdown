My Blog
=======
This is the source for my [blog][MyBlog].  It's based on the [Cactus][] Static 
Site Generator (SSG) which uses [Django][] templates and deploys the site to 
[Amazon S3][].  

Feel free to use the code in your blog, but please do not copy the blog 
content.


Requirements
------------

 * [Python](http://python.org/)
 * [Cactus][]
 * [Markdown](http://www.freewisdom.org/projects/python-markdown/)

To install the needed tools:

	sudo easy_install https://github.com/koenbok/Cactus/zipball/master
	sudo pip install markdown

Nods to other tools used to develop this:

 * [Bootstrap][]
 * [Sublime Text 2][]


Making a Blog Post
------------------
To make a new blog post create a file in the  "posts" directory.

	<ROOT>/posts/YYYY-MM-DD-title-of-your-post.markdown

Where:
  
 * YYYY = 4 digit year
 * MM = 2 digit month (01..12)
 * DD = 2 digit day of month

Edit the new post accordingly, making sure to have the following meta parameters
at the top:

	Title: Title of Your Post
	Authors: FirstName LastName
	Date: YYYY/MM/DD HH:MM:SS

	Lorem ipsum dolor
	=================
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tempor 
	tincidunt feugiat. Morbi risus augue, pulvinar in hendrerit at, sollicitudin 
	ac velit. Duis bibendum leo egestas lectus fermentum pharetra. Vestibulum et 
	quam sed nisl egestas faucibus. Praesent consequat augue sit amet magna 
	tristique adipiscing. Pellentesque lobortis posuere elit sit amet interdum. 
	Suspendisse potenti. Ut dapibus ultricies enim, vitae iaculis arcu rutrum eu. 
	Pellentesque placerat luctus diam quis ultricies. Morbi sagittis molestie auctor.

Modifying Non-Blog Posts
------------------------
Modify the .html file you want to.  I've added support for the markdown tag in the 
Django based templates:

	{% markdown %}
	Lorem ipsum dolor
	=================
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tempor 
	tincidunt feugiat. Morbi risus augue, pulvinar in hendrerit at, sollicitudin 
	ac velit. Duis bibendum leo egestas lectus fermentum pharetra. 
	{% endmarkdown %}


[MyBlog]: http://www.ckridgway.com/ "Chris Ridgway's Blog"
[Cactus]: https://github.com/koenbok/Cactus "Cactus"
[Django]: https://www.djangoproject.com/ "Django"
[Amazon S3]: http://aws.amazon.com/s3/ "Amazon S3"
[Bootstrap]: http://twitter.github.com/bootstrap/ "Twitter Bootstrap"
[Sublime Text 2]: http://www.sublimetext.com/2 "Sublime Text 2"
