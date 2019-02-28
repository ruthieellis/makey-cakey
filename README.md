# ruthieellis.github.io
This is the GitHub repoistory for the [Makey Cakey blog](https://ruth.ellis.scot/). The site is hosted on [GitHub Pages](https://pages.github.com/) using the [Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/). The blog was imoported from [http://makey-cakey.blogspot.com/](http://makey-cakey.blogspot.com/). 

# Create a new post
* Go to [https://github.com/ruthieellis/ruthieellis.github.io/tree/master/_posts](https://github.com/ruthieellis/ruthieellis.github.io/tree/master/_posts) 
* Click "Create new file"
* Name the file in the yyyy-mm-dd-post-title.md format 
* Add the following header:
```
---
title: Post title
tags:
- dairy free
- picnic
- dried fruit
header:
  teaser: "/assets/yyyy-mm-dd-image-0000.jpg"
---
Start your blog post here

```
* Posts are written in Markdown - [read more here](https://mmistakes.github.io/minimal-mistakes/markup/markup-html-tags-and-formatting/)

# Edit an old posts
Old posts are HTML format and may have broken links or missing external images. To edit, edit the file from the [posts](https://github.com/ruthieellis/ruthieellis.github.io/tree/master/_posts) folder.

# Upload an image
* Go to [https://github.com/ruthieellis/ruthieellis.github.io/tree/master/assets](https://github.com/ruthieellis/ruthieellis.github.io/tree/master/assets)
* Upload files, ideally in this format (but it's not essential) or you can add to a folder by year or year and month: 
```
/assets/yyyy-mm-dd-image-0000.jpg
```

You can also add an [image gallery](https://mmistakes.github.io/minimal-mistakes/docs/helpers/) - add the image links to the header and then embed the gallery in the post. 

# Add video
For YouTube:
```
{% include video id="XsxDH4HcOWA" provider="youtube" %}
```

For Vimeo:
```
{% include video id="212731897" provider="vimeo" %}
```

For Google Drive:
```
{% include video id="1u41lIbMLbV53PvMbyYc9HzvBug5lNWaO" provider="google-drive" %}
```

# Add an emoji
* The blog uses [https://github.com/jekyll/jemoji](https://github.com/jekyll/jemoji)
* Search for an emoji on [https://emojipedia.org/](https://emojipedia.org/)
* Copy the shortcode
* Add ```:+1:``` to your post to add a +1 emoji




# Future changes
* Set up a [Forestry CMS](https://forestry.io/)
