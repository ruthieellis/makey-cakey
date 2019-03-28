# Jekyll will import posts from Blogger, but they still contain links to larger
# image formats as references to Blogger's CDN. This script:
# - Finds all linked image references in an imported blogger page
# - Downloads the images into the assets/ directory
# - Rewrites the page with the appropriate image link

import re
import sys
if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

IMG_RE = re.compile('<a[^>]+href="(?P<src>[^"]+)"')
DATE_RE = re.compile('(?P<date>[0-9]+\-[0-9]+\-[0-9]+)')

for filename in sys.argv[1:]:
    date_prefix = DATE_RE.search(filename).group('date')
    with open(filename, 'r') as f:
        file_index = 0
        contents = f.read()
        for match in IMG_RE.finditer(contents):
            sourceurl = match.group('src')
            extstart = sourceurl.rfind('.')
            extension = sourceurl[extstart:]
            newfile = date_prefix + '-linked-image-{:04d}{}'.format(file_index, extension)
            file_index += 1
            # print('{} => {}'.format(sourceurl, newfile))
            # try:
            print("Try: Start")
            urlretrieve(sourceurl, '../assets/' + newfile)
            print("Try: End")
            contents = contents.replace(sourceurl, '{{ site.url }}/assets/' + newfile)
            # except:
            #     continue

    with open(filename, 'w') as f:
        f.write(contents)
