#  run using
# ruby -rubygems jekyll.rb
# from https://stackoverflow.com/questions/37371947/importing-my-blogger-blog-into-jekyll

# from https://import.jekyllrb.com/docs/blogger/
require "jekyll-import";
        JekyllImport::Importers::Blogger.run({
          "source"                => "blog-03-20-2019.xml",
          "no-blogger-info"       => "true", # not to leave blogger-URL info (id and old URL) in the front matter
          "replace-internal-link" => "true", # replace internal links using the post_url liquid tag.
        })
