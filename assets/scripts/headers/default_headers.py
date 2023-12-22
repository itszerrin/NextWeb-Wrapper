from ...typing import Headers

def get_default_headers() -> Headers:

    """Get the default headers for the API request"""

    return {
        'POST': '/api/openai/v1/chat/completions HTTP/3',
        'Host': 'chat.3211000.xyz',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': 'text/event-stream',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://chat.3211000.xyz/',
        'Content-Type': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'Content-Length': '420',
        'Origin': 'https://chat.3211000.xyz',
        'Alt-Used': 'chat.3211000.xyz',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }