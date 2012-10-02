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

	pip install cactus

Nods to other tools used to develop this:

 * [Bootstrap][]
 * [Sublime Text 2][]


Making a Blog Post
------------------
To make a new blog post create a new file in the "posts" directory.

	<ROOT>/posts/title-of-your-post.html

You can do straight HTML or you can use markdown.  I recommend copying an 
existing markdown post and editing it accordingly.

Modifying Non-Blog Posts
------------------------
Modify the .html file you want to.  You can edit your files using 
markdown now.


[MyBlog]: http://www.ckridgway.com/ "Chris Ridgway's Blog"
[Cactus]: https://github.com/koenbok/Cactus "Cactus"
[Django]: https://www.djangoproject.com/ "Django"
[Amazon S3]: http://aws.amazon.com/s3/ "Amazon S3"
[Bootstrap]: http://twitter.github.com/bootstrap/ "Twitter Bootstrap"
[Sublime Text 2]: http://www.sublimetext.com/2 "Sublime Text 2"
