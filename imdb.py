#!/usr/bin/env python

def get_middle(s, start, end):
    import re
    try:
        return re.search(re.escape(start) + '(.*?)' + re.escape(end), s).group(1)
    except:
        return 'no-data'

def make_url(movie_id):
    return 'http://www.imdb.com/title/{mid}'.format(
        mid=movie_id)

def get_source(movie_id):
    import urllib2
    url = make_url(movie_id)
    stream = urllib2.urlopen(url)
    return stream.read()

def get_rating(source):
    return get_middle(source, '<span itemprop="ratingValue">', '</span>')

def get_title(source):
    return get_middle(source, '<span class="itemprop" itemprop="name">','</span>')

def get_release(source):
    return get_middle(source, '<meta itemprop="datePublished" content="','" />')

def insert(movie_id, file_name, marker='%! FILMDATA !%\n'):
    """Insert information for this `movie-id` before the %! FILMDATA !% line in `file_name`.

This function should not delete the marker line.
"""
    with open(file_name, 'r') as f:
        file_lines = list(f)

    marker_line = file_lines.index(marker)

    source = get_source(movie_id)
    data = '\\film{%s}{%s}{%s}{%s}\n' % (
        make_url(movie_id),
        get_title(source),
        get_release(source),
        get_rating(source))
    
    file_lines.insert(marker_line, data)

    with open(file_name, 'w') as f:
        f.writelines(file_lines)

def main():
    import sys
    file_name = sys.argv[1]
    for movie_id in sys.argv[2:]:
        insert(movie_id, file_name)

if __name__ == '__main__':
    import sys
    print 'Welcome.'
    print 'Inserting data for {}'.format(str(sys.argv[2:]))
    main()
    print 'Done.'
