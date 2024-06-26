try:
    import utilities
    utilities.modify_system_path()
except:
    pass
import time
from apis import utilities, secret_tokens
import requests
import textwrap

__docformat__ = "google"


__all__ = [
    'get_businesses', 'get_categories',
    'generate_businesses_table',
    'generate_business_table', 'get_reviews'
]
def get_categories():
    """
    Simply returns a list of abbreviated categories from Yelp. Doesn't require any arguments.
   
    Note that while this function returns SOME of the valid yelp categories, there's a lot more. They are \
    <a href="https://blog.yelp.com/businesses/yelp_category_list/#section21">documented on Yelp's website</a>. \
    You can use any of those as valid categories for a search.

    Returns:
        a `list` of valid yelp categories which are strings. 
    """
    categories = [
        'mexican', 'chinese', 'pizza', 'italian', 'thai', 'japanese',
        'vietnamese', 'asianfusion', 'ethiopian', 'korean', 'indpak',
        'mideastern', 'tapas', 'pakistani', 'brazilian', 'filipino',
        'african', 'greek', 'coffee', 'dessert', 'pancakes', 'gastropubs'
    ]
    categories.sort()
    return categories

# retrieves data from any Yelp endpoint:
def _issue_get_request(url:str, debug: bool = True):
    '''
    Private function. Retrieves data from any Yelp endpoint using the authentication key.

    * url (str): [Required] The API Endpoint + query parameters.

    Returns whatever Yelp's API endpoint gives back.
    '''

    token = secret_tokens.YELP_API_TOKEN
    headers = {
        'Authorization': 'Bearer ' + token
    }
    url = url.replace(" ", "%20")
    response = requests.get(url, headers=headers, verify=True)
    
    if response.status_code != 200:
        time.sleep(1)

        from apis import authentication
        token = authentication.get_token(
            'https://www.apitutor.org/yelp/key')
        
        if debug:
            print("DEBUG: Using backup...")

        headers = {
            'Authorization': 'Bearer ' + token
        }
        response = requests.get(url, headers=headers, verify=True)

        if response.status_code != 200:
            raise Exception("COULD NOT COMMUNICATE WITH YELP. Did you run the verification tests?")
        else:
            return response.json()
        
    return response.json()

   
def _simplify_businesses(data:list):
    '''
    Private function. Simplifies Yelp businesses.

    * data (list): The original data list returned by the Yelp API

    Returns a simpler data structure for the (complex) data
    returned by Yelp. Only shows some of the most common
    data fields.
    '''
    def get_alias(item):
        return item['alias']
    simplified = []
    for item in data['businesses']:
        business = {
            'id': item['id'],
            'name': item['name'],
            'rating': item['rating'],
            'image_url': item['image_url'],
            'display_address': '., '.join(item['location']['display_address']),
            'coordinates': item['coordinates'],
            'review_count': item['review_count'],
            'share_url': item['url'].split('?')[0],
            'categories': ', '.join(list(map(get_alias, item['categories']))),
            'price': item.get('price'),
            'display_phone': item.get('display_phone'),
            'transactions': item.get('transactions')
        }
        simplified.append(business)
    return simplified

def _simplify_comments(data:list):
    '''
    Private function that simplifies Yelp's comments data structure.

    * data (list): The original data list returned by the Yelp API

    Returns a simpler data structure for the (complex) data
    returned by Yelp. Only shows some of the most common
    data fields.
    '''
    simplified = []
    for item in data['reviews']:
        review = {
            'id': item['id'],
            'rating': item['rating'],
            'text': item['text'].replace('\n', ' '),
            'time_created': item['time_created'].split(' ')[0],
            'url': item['url']
        }
        simplified.append(review)
    return simplified


def _generate_business_search_url(location:str, limit:int=10, term:str=None, categories:str=None, sort_by:str=None, price:str=None, open_now:str=None, attributes:str=None):
    # https://www.yelp.com/developers/documentation/v3/business_search
    '''
    Private function. Creates the URL that will be issued to the Yelp API:

    * location (str):   [Required] Location of the search
    * limit (int):      An integer indicating how many records to return. Max of 50.
    * term (str):       A search term
    * categories (str): One or more comma-delimited categories to filter by.
    * sort_by (str):    How to order search results.
        * Options are: `"best_match"`, `"rating"`, `"review_count"`, `"distance"`
    * price (str):      How expensive 1, 2, 3, 4 or comma-delimited string, e.g.: `"1,2"`
    * open_now (str):   Set to 'true' if you only want the open restaurants
    * `attributes` (`list` of `str`s): A list of one or more of the following filters: `hot_and_new`, `reservation`, `gender_neutral_restrooms`, `open_to_all`, `wheelchair_accessible`

    Returns a url (string).
    '''
    url = 'https://api.yelp.com/v3/businesses/search?location=' + \
        location + '&limit=' + str(limit)
    if term:
        url += '&term=' + term
    if categories:
        tokens = categories.split(',')
        all_categories = get_categories()
        for token in tokens:
            if token not in all_categories:
                raise Exception('"' + token + '" is not a valid category because it isn\'t in the yelp.get_categories() list. Please make sure that the following categories are valid (with a comma separating each of them): ' + categories)
        url += '&categories=' + categories

    if attributes:
        for attribute in attributes:
            if attribute not in ['hot_and_new', 'reservation', 'gender_neutral_restrooms', 'open_to_all', 'wheelchair_accessible']:
                raise Exception(attribute + " not in ['hot_and_new', 'reservation', 'gender_neutral_restrooms', 'open_to_all', 'wheelchair_accessible']")
        url += '&attributes=' + ",".join(attributes)

    if sort_by:
        if sort_by not in ['best_match', 'rating', 'review_count', 'distance']:
            raise Exception(sort_by + " not in ['best_match', 'rating', 'review_count', 'distance']")
        url += '&sort_by=' + sort_by

    if price:
        prices = []
        price = str(price)
        tokens = price.split(',')
        for token in tokens:
            token = token.strip()
            if token not in ['1', '2', '3', '4']:
                raise Exception('The price parameter can be 1, 2, 3, 4, or some comma-separated combination (e.g. 1,2,3). You used: ' + str(price))
            prices.append(token.strip())
        prices = sorted(prices)
        prices = ','.join(prices)
        url += '&price=' + prices  #1, 2, 3, 4 -or- 1,2 (for more than one)

    if open_now:
        url += '&open_now=true'

    return url

def get_businesses(location:str, limit:int=10, 
                   search_term:str=None, 
                   categories:str=None, 
                   sort_by:str=None, price:str=None, open_now:bool=None, attributes:list=None,
                   debug:bool = True,
                   simplify:bool=True):
    '''
    Searches for Yelp businesses based on various search criteria. 
    
    Args:
        location (`str`):   [Required] Location to search.
        limit (`int`):      An integer indicating how many records to return. Max of 50.
        search_term (`str`): A search term
        categories (`str`): One or more comma-delimited categories to filter by.
        sort_by (`str`):    How to order search results. Options are:
                            best_match, rating, review_count, distance. Note that the
                            rating option will be weighted by the number of reviews each
                            restaurant has.
        price (`str`):      How expensive 1, 2, 3, 4 or comma-delimited list, e.g.: 1,2
        open_now (`bool`):   Set to True if you only want the open restaurants
        attributes (`list`): A list of any one ore more of the following filters: `hot_and_new`, `reservation`, `gender_neutral_restrooms`, `open_to_all`, `wheelchair_accessible`
        debug (`bool`): Whether or not you want to see the debug messages printed out.       
        simplify (`bool`):  Indicates whether you want to simplify the data that is returned. Non-simplified data
                                will return a list of dictionaries.

    Returns:
        a `list` of businesses matching your search / ordering / limit criteria.
    '''

    # generate the URL query string based on the arguments passed in by the user
    url = _generate_business_search_url(
        location,
        limit=limit,
        term=search_term,
        categories=categories,
        sort_by=sort_by,
        price=price,
        open_now=open_now,
        attributes=attributes
    )
    if debug:
        print("DEBUG: Here's the request we're going to make.\n", url, "\nYou can't access it in a browser, but you can double check the inputs you gave the function are part of the URL.")

    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_businesses(data)

def generate_businesses_table(businesses:list):
    '''
    Generates a tabular representation of a *list* of businesses to be displayed in a plain textbox.

    Args:
        businesses (`list`): A list of dictionaries (where each dictionary represents a business).

    Returns:
        a `string` representation of a table.
    '''
    text = ''
    template = '{0:2} | {1:22.22} | {2:<30.30} | {3:<6} | {4:<10}\n'

    # header section:
    text += '-' * 85 + '\n'
    text += template.format(
        '', 'Name', 'Address', 'Rating', '# Reviews'
    )
    text += '-' * 85 + '\n'

    # data section:
    counter = 1
    for business in businesses:
        text += template.format(
            counter,
            business.get('name'),
            business.get('display_address'),
            business.get('rating'),
            business.get('review_count')
        )
        counter += 1
    text += '-' * 85 + '\n'
    return text


def get_reviews(business_id:str, simplify:bool=True):
    '''
    Retrieves a list of Yelp reviews for a particular business.
    
    Args:
        business_id (`str`): A character string corresponding to the business id. Example: `"0b6AU869xq6KXdK3NtVJnw"`
        simplify (`bool`): Indicates whether you want to simplify the data that is returned.

    Returns:
        a `list` of reviews (dictionaries).
    '''
    # https://www.yelp.com/developers/documentation/v3/business_reviews
    url = 'https://api.yelp.com/v3/businesses/' + business_id.strip() + '/reviews'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_comments(data)

def _get_business_display_text(business:dict):
    '''
    Private function. Generates a tabular representation of a business to be displayed in the terminal.

    * business (dict): A simplified dictionary representing a business.

    Returns a string representation of a table.
    '''
    line_width = 85
    d = {
        'Rating': business.get('rating'),
        'Price': business.get('price'),
        'Review Count': business.get('review_count'),
        'Address': business.get('display_address'),
        'Categories': business.get('categories'),
        'Learn More': business.get('share_url'),
    }
    content = '-' * line_width + '\n'
    content += business.get('name').upper() + '\n'
    content += '-' * line_width + '\n'
    for key in d:
        content += '{0:15} | {1}\n'.format(key + ':', d[key])
    content += '-' * line_width + '\n'
    return content

def _get_reviews_display_text(reviews:list):
    '''
    Private function. Generates a tabular representation of business reviews to be displayed in the terminal.

    * reviews (list of dictionaries): A list of simplified Yelp reviews (where each review is represented as a dictionary).

    Returns a string representation of a table.
    '''
    line_width = 85
    content = 'REVIEWS:\n'
    content += '-' * line_width + '\n'
    for review in reviews:
        content += '{0:10} {1}\n'.format('Date:', review.get('time_created'))
        content += '{0:10} {1}\n'.format('Rating:', review.get('rating'))
        content += textwrap.fill(review.get('text'), line_width) + '\n'
        content += '-' * line_width + '\n'
    return content

def _get_business_display_html(business:dict):
    '''
    Private function. Generates an HTML representation of a business.

    * business (dict): A simplified dictionary representing a business.

    Returns an HTML table (string).
    '''
    d = {
        'Name': business.get('name'),
        'Rating': business.get('rating'),
        'Price': business.get('price'),
        'Review Count': business.get('review_count'),
        'Address': business.get('display_address'),
        'Categories': business.get('categories'),
        'More Info': utilities.get_link_html(business.get('share_url')),
        'Image': utilities.get_image_html(business.get('image_url'))
    }
    rows = ''
    cell_css = 'style="padding:3px;border-bottom:solid 1px #CCC;border-right:solid 1px #CCC;"'
    for key in d:
        rows += '''
            <tr>
                <th {css}>{key}:</th>
                <td {css}>{value}</td>
            </tr>'''.format(css=cell_css, key=key, value=d[key])

    table_css = 'style="width:100%;border:solid 1px #CCC;border-collapse:collapse;margin-bottom:10px;"'
    return '''
        <table {css}>
            {rows}
        </table>'''.format(css=table_css, rows=rows)


def _get_reviews_display_html(reviews:list):
    '''
    Private function. Generates an HTML representation of business reviews.

    * reviews (list of dictionaries): A list of simplified Yelp reviews (where each review is represented as a dictionary).

    Returns an HTML table (string) of reviews.
    '''
    table_css = 'style="width:100%;border:solid 1px #CCC;border-collapse:collapse;margin-bottom:10px;"'
    cell1_css = 'style="min-width:100px;padding:3px;border-bottom:solid 1px #CCC;border-right:solid 1px #CCC;"'
    cell_css = 'style="padding:3px;border-bottom:solid 1px #CCC;border-right:solid 1px #CCC;"'
    review_rows = ''
    for review in reviews:
        review_rows += '''
            <tr>
                <td {cell1_css}>{date}</td>
                <td {css}>{rating}</td>
                <td {css}>{text}</td>
            </tr>'''.format(
            cell1_css=cell1_css,
            css=cell_css,
            date=review.get('time_created'),
            rating=review.get('rating'),
            text=review.get('text'),
        )
    return '''<table {table_css}>
        <tr>
            <th {cell_css}>Date</th>
            <th {cell_css}>Rating</th>
            <th {cell_css}>Comments</th>
        </tr>
        {rows}
    </table>'''.format(
        table_css=table_css,
        cell_css=cell_css,
        rows=review_rows
    )


def generate_business_table(business: dict, reviews: list = None, to_html=False):
    '''
    Makes a formatted table of a business and corresponding review.

    Args:
        business (`dict`): A dictionary that represents a business.
        reviews (`list`): List of reviews that correspond to the business
        to_html (`bool`): Whether you want to return an HTML representation (for email)
                     or a string representation (to print to the screen).

    Returns:
        a `str` with either a plain text or an HTML representation of a business + reviews.
    '''
    if not business:
        print('A business is required.')
        return

    if to_html:
        the_html = _get_business_display_html(business)
        if reviews:
            the_html += _get_reviews_display_html(reviews)
        return the_html
    else:
        the_text = _get_business_display_text(business)
        if reviews:
            the_text += _get_reviews_display_text(reviews)
        return the_text
